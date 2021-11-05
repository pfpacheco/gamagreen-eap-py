import re

from sqlalchemy.exc import DatabaseError

from com.brookgreen.gama.exe.app import db
from com.brookgreen.gama.orm.person import Person
from com.brookgreen.gama.orm.user import User
from com.brookgreen.gama.service.login.login_service_abstract import LoginServiceAbstract


class LoginService(LoginServiceAbstract):

    def __init__(self):
        super(LoginService, self).__init__()

        self.session = db.session()
        self.response = {}
        self.user = User()
        self.login_form = {}

    def sign_on(self, *args, **kwargs):
        try:
            if kwargs:
                self.login_form.update(
                    {
                        "email": kwargs["kwargs"].get("email"),
                        "password": kwargs["kwargs"].get("password")
                    }
                )
                if self.login_form != {}:
                    self.user = self.get_user_by_email(email=self.login_form.get("email"))
                    if self.user:
                        self.response = self.check_user_by_steps()
                    elif not self.user:
                        self.response = {"code": 404, "status": "NOT_FOUND", "message": "User not found!"}
                    return self.response
        except Exception as e:
            print("Error handling SignOn operation >> {}".format(e))

    def check_user_by_steps(self):
        if not self.user.is_employee:
            self.response = {"code": 403, "status": "FORBIDDEN", "message": "Access denied!"}
            return self.response
        elif not self.user.is_approved:
            if self.user.is_reproved:
                self.response = {"code": 403, "status": "FORBIDDEN",
                                 "message": "You are not allowed on this system!"}
                return self.response
            elif not self.user.is_reproved:
                self.response = {"code": 428, "status": "PRECONDITION_REQUIRED",
                                 "message": "You might be approved on this system!"}
                return self.response
        elif not self.user.is_allowed:
            self.response = {"code": 423, "status": "LOCKED", "message": "Your access is blocked!"}
            return self.response
        elif not self.user.is_not_first_access:
            self.response = {"code": 412, "status": "PRECONDITION_FAILED",
                             "message": "You have to change your password!"}
            return self.response
        else:
            self.response = self.check_is_user_enrolled()
            return self.response

    def check_is_user_enrolled(self):
        pw_hash = re.compile(self.user.pw_hash)
        password_matches = pw_hash.match(self.login_form.get("password"))
        if password_matches:
            try:
                self.user.incorrect_password_trials = 0
                self.session.add(self.user)
                self.session.commit()
                self.response = {"code": 202, "status": "ACCEPTED", "message": "ACCEPTED"}
            except DatabaseError as e:
                print("Error updating user in database >> {}".format(e))
        elif not password_matches:
            if self.user.incorrect_password_trials < 3:
                try:
                    self.user.incorrect_password_trials = self.user.incorrect_password_trials + 1
                    self.session.add(self.user)
                    self.session.commit()
                except DatabaseError as e:
                    print("Error updating user in database >> {}".format(e))
                self.response = {"code": 401, "status": "UNAUTHORIZED", "message": "Access denied!"}
            elif self.user.incorrect_password_trials == 3:
                self.response = {"code": 423, "status": "LOCKED", "message": "Your access is blocked!"}
        return self.response

    def get_user_by_email(self, email):
        try:
            user = self.session.query(User).filter(
                User.person_id.__eq__(Person.id).__and__(Person.email.__eq__(email))).first()
            return user
        except DatabaseError as e:
            print("Error retrieving User from database >> {}".format(e))

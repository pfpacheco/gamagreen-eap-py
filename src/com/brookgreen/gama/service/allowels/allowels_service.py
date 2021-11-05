from datetime import datetime

import pytz

from sqlalchemy.exc import DatabaseError

from com.brookgreen.gama.exe.app import db
from com.brookgreen.gama.orm.person import Person
from com.brookgreen.gama.orm.user import User
from com.brookgreen.gama.service.allowels.allowels_service_abstract import AllowelsServiceAbstract


class AllowelsService(AllowelsServiceAbstract):

    def __init__(self):
        super(AllowelsService, self).__init__()

        self.user_list = []
        self.response = {}
        self.session = db.session()
        self.allowels_form_items = []

    def get_list(self):
        try:
            users = self.session.query(User).all()
            if len(users) > 0:
                for user in users:
                    person = self.session.query(Person).filter(Person.id == user.person_id).one()
                    user = {
                        "id": user.id,
                        "is_approved": user.is_approved,
                        "is_reproved": user.is_reproved,
                        "date_of_creation": user.creation_dt,
                        "date_of_last_update": user.last_update,
                        "person": {
                            "person_id": person.id,
                            "person_name": person.name,
                            "person_email": person.email
                        }
                    }
                    self.user_list.append(user)
                self.response.update({
                    "code": 202, "status": 'ACCEPTED', "message": "OK", "body": self.user_list
                })
            else:
                self.response.update({
                    "code": 204, "status": "NO_CONTENT", "message": "EMPTY", "body": self.user_list
                })
        except Exception as e:
            print("Error on retrieving approved users >> ApprovalsService {}".format(e))
        return self.response

    def set_approved(self, *args, **kwargs):
        try:
            if kwargs:
                self.allowels_form_items = kwargs["kwargs"]
                if len(self.allowels_form_items) > 0:
                    for item in self.allowels_form_items:
                        user = self.session.query(User).filter(User.id.__eq__(item['id'])).one()

                        user.is_approved = True
                        user.is_reproved = False
                        user.is_allowed = True
                        user.last_update = datetime.now(tz=pytz.timezone("Europe/London"))

                        try:
                            self.session.add(user)
                            self.session.commit()

                        except DatabaseError as e:
                            self.session.rollback()
                            self.response.update({
                                "code": 500, "status": "INTERNAL_SERVER_ERROR", "message": "DATABASE_ERROR"
                            })
                            print("Error on persisting allowels information >> ApprovalsService {}".format(e))
                    self.response.update({
                        "code": 201, "status": "CREATED", "message": "OK"
                    })
                else:
                    self.response.update({
                        "code": 405, "message": "EMPTY_POST_NOT_ALLOWED"
                    })
        except Exception as e:
            print("Error on saving approved users >> ApprovalsService {}".format(e))
        return self.response

    def set_reproved(self, *args, **kwargs):
        try:
            if kwargs:
                self.allowels_form_items = kwargs["kwargs"]
                if len(self.allowels_form_items) > 0:
                    for item in self.allowels_form_items:
                        user = self.session.query(User).filter(User.id.__eq__(item['id'])).one()

                        user.is_approved = False
                        user.is_reproved = True
                        user.is_allowed = True
                        user.last_update = datetime.now(tz=pytz.timezone("Europe/London"))

                        try:
                            self.session.add(user)
                            self.session.commit()

                        except DatabaseError as e:
                            self.session.rollback()
                            self.response.update({
                                "code": 500, "status": "INTERNAL_SERVER_ERROR", "message": "DATABASE_ERROR"
                            })
                            print("Error on persisting reproved users >> ReprovalsService {}".format(e))
                    self.response.update({
                        "code": 201, "status": "CREATED", "message": "OK"
                    })
                else:
                    self.response.update({
                        "code": 405, "message": "EMPTY_POST_NOT_ALLOWED"
                    })
        except Exception as e:
            print("Error on saving reproved users >> ReprovesService {}".format(e))
        return self.response

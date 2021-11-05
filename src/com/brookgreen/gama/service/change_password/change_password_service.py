import os

from datetime import datetime

import pytz
from sqlalchemy.exc import DatabaseError

from sendgrid import Mail, SendGridAPIClient, SendGridException

from com.brookgreen.gama.exe.app import app, db
from com.brookgreen.gama.orm.person import Person
from com.brookgreen.gama.orm.user import User
from com.brookgreen.gama.service.change_password.change_password_service_abstract import ChangePasswordServiceAbstract


class ChangePasswordService(ChangePasswordServiceAbstract):

    def __init__(self):
        super(ChangePasswordService, self).__init__()

        self.response = {}
        self.session = db.session()
        self.user = None
        self.change_password_form = {}

    def change(self, *args, **kwargs):
        if kwargs["kwargs"]:
            self.change_password_form.update(
                {
                    "email": kwargs["kwargs"].get("email"),
                    "password": kwargs["kwargs"].get("password"),
                    "confirm_password": kwargs["kwargs"].get("confirm_password")
                }
            )

            if self.change_password_form:
                if self.change_password_form.get("password") == self.change_password_form.get("confirm_password"):

                    self.user = self.session.\
                        query(User).filter(User.person_id.
                                           __eq__(Person.id).
                                           __and__(Person.email.
                                                   __eq__(self.change_password_form.get("email")))).first()
                    self.user.is_not_first_access = True
                    self.user.incorrect_password_trials = 0
                    self.user.last_update = datetime.now(tz=pytz.timezone("Europe/London"))
                    self.user.pw_hash = self.change_password_form.get("password")
                    status = self.save_password(user=self.user)
                    if status:
                        self.response = {"code": 201, "message": "Password has been changed!"}
                        self.send_email()
                    else:
                        self.response = {"code": 500, "message": "Error changing the password!"}
        return self.response

    def save_password(self, user):
        try:
            self.session.add(user)
            self.session.commit()
            status = True
        except DatabaseError as e:
            self.session.rollback()
            status = False
            print("Error updating password for User in database >> {}".format(e))
        return status

    def send_email(self):
        try:
            """ Sender information """
            sender_address = os.environ.get("SMTP_ACCOUNT")
            sender_account_api_key = os.environ.get("SMTP_ACCOUNT_API_KEY")

            """ Setup MIME Multipart message """

            body = ""
            body += "<p>Your password has been changed!</p>"
            body += "<p>***********************************************</p>"
            body += "<p> password: " + self.change_password_form.get("password") + "</p>"
            body += "<p>***********************************************</p>"
            body += "<p>Cheers!</p><p>CF " + "IT Members </p><br><br><br><br>"
            body += "<p>*********************************************************************</p>"
            body += "<p>This is an automatic message, do not reply to this address!</p>"
            body += "<p>*********************************************************************</p>"

            """ Defining message on SendGrid API for SMTP """
            message = Mail(
                from_email=sender_address,
                to_emails=self.change_password_form.get("email"),
                subject="Email from " + app.name + " to " + self.change_password_form.get("email") +
                        " - Your user has been created!",
                html_content=body
            )

            """ Sending the message """
            send_grid_smtp = SendGridAPIClient(api_key=sender_account_api_key)
            send_grid_smtp.send(message)
            return True

        except SendGridException as error:
            print("Error on processing MIME-MULTIPART >> {}".format(error))
            return False

import os
import string
from datetime import datetime
from random import choice

import pytz
from sendgrid import SendGridAPIClient
from sendgrid import SendGridException
from sendgrid.helpers.mail import Mail
from sqlalchemy.exc import DatabaseError

from com.brookgreen.gama.exe.app import app, db
from com.brookgreen.gama.orm.person import Person
from com.brookgreen.gama.orm.user import User
from com.brookgreen.gama.service.recover.recover_password_service_abstract \
    import RecoverPasswordServiceAbstract


class RecoverPasswordService(RecoverPasswordServiceAbstract):

    def __init__(self):
        super(RecoverPasswordService, self).__init__()

        self.user = None
        self.response = {}
        self.password = ""
        self.session = db.session()
        self.recover_password_form = {}

    def recover_password(self, *args, **kwargs):
        if kwargs["kwargs"]:
            self.recover_password_form.update({
                "email": kwargs["kwargs"].get("email"),
            })
            if self.recover_password_form:
                self.user = self.session. \
                    query(User).filter(User.person_id.
                                       __eq__(Person.id).
                                       __and__(Person.email.
                                               __eq__(self.recover_password_form.get("email")))).first()
                self.user.is_not_first_access = False
                self.user.incorrect_password_trials = 0
                self.user.last_update = datetime.now(tz=pytz.timezone("Europe/London"))
                self.user.pw_hash = self.get_password()

                try:
                    self.session.add(self.user)
                    self.session.commit()
                    try:
                        self.send_email()
                        self.response.update(
                            {"code": 201, "status": "ACCEPTED", "message": "Password has been recovered!"}
                        )
                    except SendGridException as e:
                        self.session.rollback()
                        print("Error on sending email with recovered password >> RecoverPassword >> {}".format(e))
                except DatabaseError as e:
                    self.session.rollback()
                    self.response.update(
                        {"code": 500, "status": "ERROR", "message": "Password recovery fails!"}
                    )
                    print("Error on recovering password >> RecoverPassword >> {}".format(e))
        return self.response

    def get_password(self):

        for i in range(0, 2):
            self.password += "".join(choice(string.ascii_letters) + choice(string.ascii_uppercase) +
                                     choice(string.ascii_lowercase) + choice(string.digits))
        for i in range(1):
            self.password += self.password + "".join(choice(string.ascii_letters) + choice(string.ascii_uppercase) +
                                                     choice(string.ascii_lowercase) + choice(string.digits))
        return self.password

    def send_email(self):
        try:
            """ Sender information """
            sender_address = os.environ.get("SMTP_ACCOUNT")
            sender_account_api_key = os.environ.get("SMTP_ACCOUNT_API_KEY")

            """ Setup MIME Multipart message """

            body = ""
            body += "<p>Your password has been updated!</p>"
            body += "<p>***********************************************</p>"
            body += "<p> password: " + self.password + "</p>"
            body += "<p>***********************************************</p>"
            body += "<p>Cheers!</p><p>CF " + "IT Members </p><br><br><br><br>"
            body += "<p>*********************************************************************</p>"
            body += "<p>This is an automatic message, do not reply to this address!</p>"
            body += "<p>*********************************************************************</p>"

            """ Defining message on SendGrid API for SMTP """
            message = Mail(
                from_email=sender_address,
                to_emails=self.recover_password_form.get("email"),
                subject="Email from " + app.name + " to " + self.recover_password_form.get("email") +
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

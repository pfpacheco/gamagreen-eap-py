import os
import string
from datetime import datetime
from random import choice

import pytz
from celery import Celery
from celery.schedules import crontab
from dotenv import load_dotenv, find_dotenv
from sendgrid import SendGridAPIClient
from sendgrid import SendGridException
from sendgrid.helpers.mail import Mail
from sqlalchemy.exc import DatabaseError

from com.brookgreen.gama.exe.app import app, db
from com.brookgreen.gama.orm.person import Person
from com.brookgreen.gama.orm.user import User

load_dotenv(find_dotenv())

celery = Celery(app.import_name, broker=os.environ.get("BROKER_URL"))
celery.conf.beat_schedule = {
    "registration_task_runs_each_60_minutes": {
        "task": "tasks.registration_task",
        "schedule": crontab(minute="*/5")
    }
}
celery.conf.timezone = "Europe/London"


@celery.task(name="tasks.registration_task")
def registration_task():
    """ Select persons registered in the last hour """
    try:
        persons = db.session.query(Person).filter(Person.is_consumed.__eq__(False)).all()
        if persons is not None:
            for person in persons:
                user = User()
                try:
                    user.pw_hash = get_password()
                    user.is_allowed = True
                    user.is_approved = False
                    user.is_employee = True
                    user.is_not_first_access = False
                    user.incorrect_password_trials = 0
                    user.creation_dt = datetime.now(tz=pytz.timezone("Europe/London"))
                    user.last_update = datetime.now(tz=pytz.timezone("Europe/London"))
                    user.person_id = person.id
                    user.user_group_id = 8  # Not Defined Group - Approver will define the best option

                    db.session.add(user)

                    person.is_consumed = True
                    person.last_update = datetime.now(tz=pytz.timezone("Europe/London"))

                except DatabaseError as error:
                    raise "Error on processing new user >> {}".format(error)
                """ Send email within new passwords for user """

                status = send_email(person=person, password=user.pw_hash)
                if status:
                    try:
                        db.session.commit()
                    except DatabaseError as error:
                        print("Error on processing person update >> {}".format(error))
                else:
                    try:
                        db.session.rollback()
                    except DatabaseError as error:
                        print("Error on processing new user >> {}".format(error))
    except DatabaseError as _error:
        print("Error on processing registration_task >> {}".format(_error))


def get_password():
    password = ""
    for i in range(0, 2):
        password += "".join(choice(string.ascii_letters) + choice(string.ascii_uppercase)
                            + choice(string.ascii_lowercase) + choice(string.digits))
    for i in range(1):
        password += password + "".join(choice(string.ascii_letters) + choice(string.ascii_uppercase)
                                       + choice(string.ascii_lowercase) + choice(string.digits))
    return password


def send_email(person, password):
    try:
        """ Sender information """
        sender_address = os.environ.get("SMTP_ACCOUNT")
        sender_account_api_key = os.environ.get("SMTP_ACCOUNT_API_KEY")

        """ Setup MIME Multipart message """

        body = ""
        body += "<p>Hey " + person.name + ",</p><br><br><br>"
        body += "<p>Your password has been created!</p>"
        body += "<p>***********************************************</p>"
        body += "<p> password: " + password + "</p>"
        body += "<p>***********************************************</p>"
        body += "<br><p>You must wait an approval email " \
                "to access the system and change your password at first time!</p>"
        body += "<p>Cheers!</p><p>CF " + "IT Members </p><br><br><br><br>"
        body += "<p>*********************************************************************</p>"
        body += "<p>This is an automatic message, do not reply to this address!</p>"
        body += "<p>*********************************************************************</p>"

        """ Defining message on SendGrid API for SMTP """
        message = Mail(
            from_email=sender_address,
            to_emails=person.email,
            subject="Email from " + app.name + " to " + person.email + " - Your user has been created!",
            html_content=body
        )

        """ Sending the message """
        send_grid_smtp = SendGridAPIClient(api_key=sender_account_api_key)
        send_grid_smtp.send(message)
        return True

    except SendGridException as error:
        print("Error on processing MIME-MULTIPART >> {}".format(error))
        return False

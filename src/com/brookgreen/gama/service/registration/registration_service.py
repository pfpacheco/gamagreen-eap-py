import pytz
from datetime import datetime
from sqlalchemy.exc import DatabaseError
from com.brookgreen.gama.orm.person import Person
from com.brookgreen.gama.exe.app import db
from com.brookgreen.gama.service.registration.registration_service_abstract import RegistrationServiceAbstract


class RegistrationService(RegistrationServiceAbstract):

    def __init__(self):
        super(RegistrationService, self).__init__()

        self.response = {}
        self.session = db.session()
        self.person = Person()
        self.registration_form = {}

    def sign_up(self, *args, **kwargs):
        if kwargs["kwargs"]:
            self.registration_form.update({
                "name": kwargs["kwargs"].get("name"),
                "email": kwargs["kwargs"].get("email")
            })
            person = self.get_person_by_email(email=self.registration_form.get("email"))
            if person is None:
                status = self.save_person(person=self.registration_form)
                if status:
                    self.response = {"code": 201, "message": "CREATED"}
                elif not status:
                    self.response = {"code": 500, "message": "Error processing registration!"}
            else:
                self.response = {"code": 444, "message": "Already registered on system!"}
        return self.response

    def get_person_by_email(self, email):
        try:
            person = self.session.query(Person).filter(Person.email.__eq__(email)).first()
            return person
        except DatabaseError as e:
            print("Error retrieving User from database >> {}".format(e))

    def save_person(self, person):
        try:
            self.person.name = person["name"]
            self.person.email = person["email"]
            self.person.creation_dt = datetime.now(tz=pytz.timezone("Europe/London"))
            self.person.last_update = datetime.now(tz=pytz.timezone("Europe/London"))
            self.person.is_consumed = False

            self.session.add(self.person)
            self.session.commit()
            return True

        except DatabaseError as e:
            print("Error saving person on database >> {}".format(e))

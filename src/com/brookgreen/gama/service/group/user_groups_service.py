import pytz

from datetime import datetime

from sqlalchemy.exc import DatabaseError

from com.brookgreen.gama.exe.app import db

from com.brookgreen.gama.orm.user import User
from com.brookgreen.gama.orm.person import Person
from com.brookgreen.gama.orm.user_group import UserGroup

from com.brookgreen.gama.service.group.user_groups_service_abstract import UserGroupsServiceAbstract


class UserGroupsService(UserGroupsServiceAbstract):

    def __init__(self):
        super(UserGroupsService, self).__init__()
        self.response = {}
        self.session = db.session()
        self.user_groups_form_items = {}

    def get_list(self):
        user_list = []
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
                        "groups": self.get_groups(),
                        "person": {
                            "person_id": person.id,
                            "person_name": person.name,
                            "person_email": person.email
                        }
                    }
                    user_list.append(user)
                self.response.update({
                    "code": 202, "status": 'ACCEPTED', "message": "OK", "body": user_list
                })
            else:
                self.response.update({
                    "code": 204, "status": "NO_CONTENT", "message": "EMPTY"})
        except Exception as e:
            print("Error on retrieving users >> UserGroupsService {}".format(e))
        return self.response

    def get_groups(self):
        group_list = []
        try:
            groups = self.session.query(UserGroup).all()
            if len(groups) > 0:
                for group in groups:
                    _group_ = {
                        "id": group.id,
                        "group": group.group,
                        "description": group.description
                    }
                    group_list.append(_group_)
        except Exception as e:
            print("Error on retrieving groups >> UserGroupsService {}".format(e))
        return group_list

    def set_group(self, *args, **kwargs):
        try:
            if kwargs:
                self.user_groups_form_items = kwargs["kwargs"]
                if len(self.user_groups_form_items) > 0:
                    for group_item in self.user_groups_form_items:
                        user = self.session.query(User).filter(User.id.__eq__(group_item['id'])).one()

                        user.user_group_id = group_item["group"]
                        user.last_update = datetime.now(tz=pytz.timezone("Europe/London"))

                        try:
                            self.session.add(user)
                            self.session.commit()

                        except DatabaseError as e:
                            self.session.rollback()
                            self.response.update(
                                {
                                    "code": 500, "status": "INTERNAL_SERVER_ERROR", "message": "{}".format(e)
                                }
                            )
                    self.response.update({
                        "code": 201, "status": "CREATED", "message": "OK"
                    })
                else:
                    self.response.update(
                        {
                            "code": 405, "message": "EMPTY_POST_NOT_ALLOWED"
                        }
                    )
        except Exception as e:
            print("Error on saving user group >> UserGroupsService {}".format(e))
        return self.response

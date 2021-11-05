from flask import json

from com.brookgreen.gama.service.group.user_groups_service import UserGroupsService
from com.brookgreen.gama.factory.group.user_groups_service_factory_abstract import UserGroupsServiceFactoryAbstract


class UserGroupsServiceFactory(UserGroupsServiceFactoryAbstract):

    def __init__(self):
        super(UserGroupsServiceFactory, self).__init__()
        self.response = {}

    def get_list(self) -> json:
        """ Should call user groups service """
        user_groups_service = UserGroupsService()
        self.response = user_groups_service.get_list()
        return self.response

    def set_group(self, data) -> json:
        """ Should call user groups service """
        user_groups_service = UserGroupsService()
        self.response = user_groups_service.set_group(kwargs=data)
        return self.response

    @staticmethod
    def get_instance():
        try:
            instance = UserGroupsServiceFactory()
            return instance
        except Exception as e:
            print("Error on instantiating UserGroupsServiceFactory >> {}".format(e))

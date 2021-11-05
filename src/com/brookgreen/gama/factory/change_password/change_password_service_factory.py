import json

from com.brookgreen.gama.factory.change_password.change_password_service_factory_abstract \
    import ChangePasswordServiceFactoryAbstract
from com.brookgreen.gama.service.change_password.change_password_service import ChangePasswordService


class ChangePasswordServiceFactory(ChangePasswordServiceFactoryAbstract):

    def __init__(self):
        super(ChangePasswordServiceFactory, self).__init__()
        self.response = {}

    def change(self, data) -> json:
        try:
            """ Calling the service from here """
            change_password_service = ChangePasswordService()
            self.response = change_password_service.change(kwargs=data)
        except Exception as e:
            print("Error on factoring ChangePasswordService >> {}".format(e))
        return self.response

    @staticmethod
    def get_instance():
        try:
            instance = ChangePasswordService()
            return instance
        except Exception as e:
            print("Error on instantiating ChangePasswordService >> {}".format(e))

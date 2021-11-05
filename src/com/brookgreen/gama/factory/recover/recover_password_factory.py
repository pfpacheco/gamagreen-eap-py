from flask import json

from com.brookgreen.gama.factory.recover.recover_password_factory_abstract import RecoverPasswordFactoryAbstract
from com.brookgreen.gama.service.recover.recover_password_service import RecoverPasswordService


class RecoverPasswordFactory(RecoverPasswordFactoryAbstract):

    def __init__(self):
        super(RecoverPasswordFactory, self).__init__()
        self.response = {}

    def recover_password(self, data) -> json:
        try:
            recover_password_service = RecoverPasswordService()
            self.response = recover_password_service.recover_password(kwargs=data)
        except Exception as e:
            print("Error on factoring RecoverPassword operation >> {}".format(e))
        return self.response

    @staticmethod
    def get_instance():
        try:
            instance = RecoverPasswordFactory()
            return instance
        except Exception as e:
            print("Error on factoring RecoverPassword operation >> {}".format(e))

from flask import json
from com.brookgreen.gama.service.login.login_service import LoginService
from com.brookgreen.gama.factory.login.login_service_factory_abstract import LoginServiceFactoryAbstract


class LoginServiceFactory(LoginServiceFactoryAbstract):

    def __init__(self):
        super(LoginServiceFactory, self).__init__()
        self.response = {}

    def sign_on(self, data) -> json:
        try:
            login_service = LoginService()
            self.response = login_service.sign_on(args=data.get('args'), kwargs=data)
        except Exception as e:
            print("Error on factoring SignOn operation >> {}".format(e))
        return self.response

    @staticmethod
    def get_instance():
        try:
            instance = LoginServiceFactory()
            return instance
        except Exception as e:
            raise "Error on factoring LoginService >> {}".format(e)

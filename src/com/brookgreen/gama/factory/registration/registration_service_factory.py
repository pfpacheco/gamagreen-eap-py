from flask import json
from com.brookgreen.gama.service.registration.registration_service import RegistrationService
from com.brookgreen.gama.factory.registration.registration_service_factory_abstract \
    import RegistrationServiceFactoryAbstract


class RegistrationServiceFactory(RegistrationServiceFactoryAbstract):

    def __init__(self):
        super(RegistrationServiceFactory, self).__init__()
        self.response = {}

    def sign_up(self, data) -> json:
        try:
            registration_service = RegistrationService()
            self.response = registration_service.sign_up(kwargs=data)
        except Exception as e:
            print("Error on factoring RegistrationService >> {}".format(e))
        return self.response

    @staticmethod
    def get_instance():
        try:
            instance = RegistrationServiceFactory()
            return instance
        except Exception as e:
            print("Error on instantiating RegistrationService >> {}".format(e))

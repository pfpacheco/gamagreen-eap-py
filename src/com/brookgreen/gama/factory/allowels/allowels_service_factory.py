from flask import json

from com.brookgreen.gama.service.allowels.allowels_service import AllowelsService
from com.brookgreen.gama.factory.allowels.allowels_service_factory_abstract import AllowelsServiceFactoryAbstract


class AllowelsServiceFactory(AllowelsServiceFactoryAbstract):
    
    def __init__(self):
        super(AllowelsServiceFactory, self).__init__()
        self.response = {}

    def get_list(self) -> json:
        try:
            """ Should call allowels services and retrieves pending """
            allowels_service = AllowelsService()
            self.response = allowels_service.get_list()
        except Exception as e:
            print("Error on factoring AllowelsService >> {}".format(e))
        return self.response

    def set_approved(self, data) -> json:
        try:
            """ Should call allowels services and set approved or reproved """
            allowels_service = AllowelsService()
            self.response = allowels_service.set_approved(kwargs=data)
        except Exception as e:
            print("Error on factoring AllowelsService >> {}".format(e))
        return self.response

    def set_reproved(self, data) -> json:
        try:
            """ Should call allowels services and set approved or reproved """
            allowels_service = AllowelsService()
            self.response = allowels_service.set_reproved(kwargs=data)
        except Exception as e:
            print("Error on factoring AllowelsService >> {}".format(e))
        return self.response

    @staticmethod
    def get_instance():
        try:
            instance = AllowelsServiceFactory()
            return instance
        except Exception as e:
            print("Error on instantiating AllowelsService >> {}".format(e))

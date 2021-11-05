from __future__ import annotations
from abc import abstractmethod, ABCMeta
from flask import json


class RegistrationServiceFactoryAbstract(metaclass=ABCMeta):

    @abstractmethod
    def sign_up(self, data) -> json:
        raise NotImplementedError

    @staticmethod
    def get_instance():
        raise NotImplementedError


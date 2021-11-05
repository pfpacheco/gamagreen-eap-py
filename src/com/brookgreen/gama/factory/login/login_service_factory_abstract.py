from __future__ import annotations
from abc import ABCMeta, abstractmethod
from flask import json


class LoginServiceFactoryAbstract(metaclass=ABCMeta):

    @abstractmethod
    def sign_on(self, data) -> json:
        raise NotImplementedError

    @staticmethod
    def get_instance():
        raise NotImplementedError




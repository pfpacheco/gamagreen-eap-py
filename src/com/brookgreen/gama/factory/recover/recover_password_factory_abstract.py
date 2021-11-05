from __future__ import annotations
from abc import ABCMeta, abstractmethod
from flask import json


class RecoverPasswordFactoryAbstract(metaclass=ABCMeta):

    @abstractmethod
    def recover_password(self, data) -> json:
        raise NotImplementedError

    @staticmethod
    def get_instance():
        raise NotImplementedError

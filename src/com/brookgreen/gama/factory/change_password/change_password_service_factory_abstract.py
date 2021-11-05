from __future__ import annotations
from abc import ABCMeta, abstractmethod
from flask import json


class ChangePasswordServiceFactoryAbstract(metaclass=ABCMeta):

    @abstractmethod
    def change(self, data) -> json:
        raise NotImplementedError

    @staticmethod
    def get_instance():
        raise NotImplementedError

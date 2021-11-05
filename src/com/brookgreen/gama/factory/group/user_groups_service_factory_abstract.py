from __future__ import annotations
from abc import ABCMeta, abstractmethod
from flask import json


class UserGroupsServiceFactoryAbstract(metaclass=ABCMeta):

    @abstractmethod
    def get_list(self) -> json:
        raise NotImplementedError

    @abstractmethod
    def set_group(self, data) -> json:
        raise NotImplementedError

    @staticmethod
    def get_instance():
        raise NotImplementedError

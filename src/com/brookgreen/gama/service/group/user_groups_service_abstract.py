from __future__ import annotations
from abc import ABCMeta, abstractmethod


class UserGroupsServiceAbstract(metaclass=ABCMeta):

    @abstractmethod
    def get_list(self):
        raise NotImplementedError

    @abstractmethod
    def set_group(self, *args, **kwargs):
        raise NotImplementedError

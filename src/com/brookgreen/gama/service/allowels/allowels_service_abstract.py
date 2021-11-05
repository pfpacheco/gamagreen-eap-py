from __future__ import annotations
from abc import ABCMeta, abstractmethod


class AllowelsServiceAbstract(metaclass=ABCMeta):

    @abstractmethod
    def get_list(self):
        raise NotImplementedError

    @abstractmethod
    def set_approved(self, *args, **kwargs):
        raise NotImplementedError

    @abstractmethod
    def set_reproved(self, *args, **kwargs):
        raise NotImplementedError

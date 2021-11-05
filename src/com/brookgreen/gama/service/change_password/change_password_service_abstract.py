from __future__ import annotations
from abc import ABCMeta, abstractmethod


class ChangePasswordServiceAbstract(metaclass=ABCMeta):

    @abstractmethod
    def change(self, *args, **kwargs):
        raise NotImplementedError

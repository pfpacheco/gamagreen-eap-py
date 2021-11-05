from __future__ import annotations
from abc import ABCMeta, abstractmethod


class RegistrationServiceAbstract(metaclass=ABCMeta):

    @abstractmethod
    def sign_up(self, *args, **kwargs):
        raise NotImplementedError()

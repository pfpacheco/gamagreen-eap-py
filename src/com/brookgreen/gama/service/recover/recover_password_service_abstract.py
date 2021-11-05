from __future__ import annotations

from abc import ABCMeta, abstractmethod


class RecoverPasswordServiceAbstract(metaclass=ABCMeta):

    @abstractmethod
    def recover_password(self, *args, **kwargs):
        raise NotImplementedError

    @abstractmethod
    def get_password(self):
        raise NotImplementedError

    @abstractmethod
    def send_email(self):
        raise NotImplementedError

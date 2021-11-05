from __future__ import annotations
from abc import ABCMeta, abstractmethod


class LoginServiceAbstract(metaclass=ABCMeta):

    @abstractmethod
    def sign_on(self, *args, **kwargs):
        raise NotImplementedError()

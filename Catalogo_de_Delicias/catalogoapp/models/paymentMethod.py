import abc
from abc import ABCMeta

class PaymentMethod:
    __metaclass__ = ABCMeta

    @abc.abstractmethod
    def pagar(self, total): pass

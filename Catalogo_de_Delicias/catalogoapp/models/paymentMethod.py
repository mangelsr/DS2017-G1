import abc
from abc import ABCMeta

class PaymentMethod:
    __metaclass__ = ABCMeta

    @abc.abstractmethod
    def pagar(self, total): pass

    def __unicode__(self):
        return self.name

    def __str__(self):
        return self.name

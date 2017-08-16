from abc import ABCMeta

class PaymentMethod(metaclass=ABCMeta):

    @abtractmethod
    def pagar(self, total): pass

    def __unicode__(self):
        return self.name

    def __str__(self):
        return self.name

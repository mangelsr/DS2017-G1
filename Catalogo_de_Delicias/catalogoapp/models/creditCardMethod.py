from abc import ABCMeta

class CreditCardMethod(PaymentMethod):

    def __init__(self, cardNum, codCvc, expDate):
        PaymentMethod.__init__(self)
        self.cardNum = cardNum
        self.codCvc = codCvc
        self.expDate = expDate

    def __str__(self):
        return ("Tajeta #%d"%self.cardNum, "\nCódigo seguridad: %s**"%self.codCvc[0],
                "\nFecha expiración %s"%self.expDate))

    def pagar(self, total):
        return "Pago exitoso con tarjeta"

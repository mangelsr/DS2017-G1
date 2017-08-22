from .paymentMethod import PaymentMethod

class CreditCardMethod(PaymentMethod):

    def __init__(self, cardNum=None, codCvc=None, expDate=None):
        PaymentMethod.__init__(self)
        self.cardNum = cardNum
        self.codCvc = codCvc
        self.expDate = expDate

    def __str__(self):
        return "Tajeta #%d"%self.cardNum, "\nCódigo seguridad: ***", "\nFecha expiración %s"%self.expDate

    #'boolean es un booleano' ~ Viviana Laurido, estudiante de ing en computacion, ESPOL, 2017
    #boolean es True si la tarjeta está vigente, False si está expirada
    def pagar(self, total, boolean):
        if boolean:
            return "Pago de $%.2f con tarjeta realizado exitosamente."%total
        raise ValueError("Hay problemas con el pago, seleccione nuevamente una opción.")

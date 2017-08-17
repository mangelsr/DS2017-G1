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

    """boolean es un booleano que recibe de la función que verifica la
    información con el banco para ver si se puede realizar la transacción"""
    #La funcion mencionada retorna True si la transacción es procesada existosamente, False si no
    def pagar(self, total, boolean):
        if (boolean)
            return "Pago realizado con tarjeta exitosamente."
        return "Hay problemas con el pago, seleccione nuevamente una opción."

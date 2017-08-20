from .paymentMethod import PaymentMethod

class CarnetMethod(PaymentMethod):

    def __init__(self, numMatricula, user, password):
        PaymentMethod.__init__(self)
        self.numMatricula = numMatricula
        self.user = user
        self.password = password

    def __str__(self):
        return ("Matrícula #%d"%self.numMatricula, "\nUsuario: %s"%self.user,
                "\nContraseña: ******")

    #'boolean es un booleano' ~ Viviana Laurido, estudiante de ing en computacion, ESPOL, 2017
    #boolean es True si tiene saldo suficiente, False si no
    def pagar(self, total, boolean):
        if boolean:
            return "Pago de $%.2f realizado exitosamente con su carnet estudiantil."%total
        return "Hay problemas con el pago, seleccione nuevamente una opción."

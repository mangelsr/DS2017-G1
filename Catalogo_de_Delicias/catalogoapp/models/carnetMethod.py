from abc import ABCMeta

class CarnetMethod(PaymentMethod):

    def __init__(self, numMatricula, user, password):
        PaymentMethod.__init__(self)
        self.numMatricula = numMatricula
        self.user = user
        self.password = password

    def __str__(self):
        return ("Matrícula #%d"%self.numMatricula, "\nUsuario: %s"%self.user,
                "\nContraseña: ******")

    def pagar(self, total):
        return "Pago exitoso con carnet"

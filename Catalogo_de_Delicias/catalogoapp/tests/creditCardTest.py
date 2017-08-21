from django.test import TestCase

from catalogoapp.models.creditCardMethod import CreditCardMethod

class CreditCardMethodTestCase(TestCase):
    #Prueba con tarjetas de credito vigentes
    def test_tarjetas_vigentes(self):
        creditCard1 = CreditCardMethod(cardNum= 1706631163, codCvc=493, expDate="abril 2018")
        creditCard2 = CreditCardMethod(cardNum= 1700047733, codCvc=579, expDate="julio 2018")
        self.assertEqual(creditCard1.pagar(5.00, True), "Pago de $5.00 con tarjeta realizado exitosamente.")
        self.assertEqual(creditCard2.pagar(6.00, True), "Pago de $6.00 con tarjeta realizado exitosamente.")

    #Prueba con tarjetas de credito expiradas
    def test_tarjetas_expiradas(self):
        creditCard1 = CreditCardMethod(cardNum= 1706631163, codCvc=493, expDate="abril 2017")
        creditCard2 = CreditCardMethod(cardNum= 1700047733, codCvc=579, expDate="julio 2017")
        self.assertEqual(creditCard1.pagar(5.00, False), "Hay problemas con el pago, seleccione nuevamente una opción.")
        self.assertEqual(creditCard2.pagar(6.00, False), "Hay problemas con el pago, seleccione nuevamente una opción.")

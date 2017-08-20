from django.test import TestCase

from catalogoapp.models.creditCardMethod import CreditCardMethod
from catalogoapp.models.carnetMethod import CarnetMethod

#Pruebas para tarjetas de crédito
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

#Pruebas para carnet estudiantil
class CarnetMethodTestCase(TestCase):
    #Prueba con pedidos cuyo total es menor o igual al saldo del carnet
    def test_saldo_suficiente(self):
        carnet1 = CarnetMethod(numMatricula= "201505995", user="vlaurido", password="abcd1234")
        carnet2 = CarnetMethod(numMatricula= "201505935", user="mangel", password="1234abcd")
        self.assertEqual(carnet1.pagar(5.00, True), "Pago de $5.00 realizado exitosamente con su carnet estudiantil.")
        self.assertEqual(carnet2.pagar(6.00, True),  "Pago de $6.00 realizado exitosamente con su carnet estudiantil.")

    #Prueba con pedidos cuyo total es mayor al saldo del carnet
    def test_saldo_insuficiente(self):
        carnet1 = CarnetMethod(numMatricula= "201505995", user="vlaurido", password="abcd1234")
        carnet2 = CarnetMethod(numMatricula= "201505935", user="mangel", password="1234abcd")
        self.assertEqual(carnet1.pagar(5.00, False), "Hay problemas con el pago, seleccione nuevamente una opción.")
        self.assertEqual(carnet2.pagar(6.00, False), "Hay problemas con el pago, seleccione nuevamente una opción.")

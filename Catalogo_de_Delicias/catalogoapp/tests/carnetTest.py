from django.test import TestCase

from catalogoapp.models.carnetMethod import CarnetMethod

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

from django.test import TestCase

from catalogoapp.models.order import Order

class OrderTestCase(TestCase):
    #Prueba calculando el total esperado de un almuerzo estudiantil
    def test_total_lunchEstudiantil(self):
        #code here

    #Prueba calculando el total esperado de un almuerzo ejecutivo
    def test_total_lunchEjecutivo(self):
        #code here

    #Prueba calculando el total esperado de un almuerzo ejecutivo con bebida
    def test_total_lunchEjecutivo_bebida(self):
        #code here

    #Prueba calculando el total esperado de un almuerzo ejecutivo con postre
    def test_total_lunchEjecutivo_postre(self):
        #code here

    #Prueba calculando el total esperado de un almuerzo ejecutivo con bebida y postre
    def test_total_lunchEjecutivo_ambos(self):
        #code here

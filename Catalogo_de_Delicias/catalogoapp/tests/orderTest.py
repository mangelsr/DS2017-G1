from django.test import TestCase

from datetime import date

from catalogoapp.models.order import Order
from catalogoapp.models.lunch import Lunch
from catalogoapp.models.executiveLunch import ExecutiveLunch


class OrderTestCase(TestCase):
    #Prueba calculando el total esperado de un almuerzo estudiantil
    def test_total_lunchEstudiantil(self):
        orders = Order.objects.filter(include_juice=False,include_dessert=False)
        lunch = None
        for order in orders:
            if not hasattr(order.lunch,"executivelunch"):
                lunch = order

        self.assertEqual(lunch.calculateCost(lunch.lunch, False, False), 2.50)

    #Prueba calculando el total esperado de un almuerzo ejecutivo
    def test_total_lunchEjecutivo(self):
        orders = Order.objects.filter(include_juice=False,include_dessert=False)
        executiveLunch = None
        for order in orders:
            if hasattr(order.lunch,"executivelunch"):
                executivelunch = order

        self.assertEqual(executiveLunch.calculateCost(executiveLunch.lunch, False, False), 3.00)

    #Prueba calculando el total esperado de un almuerzo ejecutivo con bebida
    def test_total_lunchEjecutivo_bebida(self):
        order = Order.objects.filter(include_juice=True)[0]
        self.assertEqual(order.calculateCost(order.lunch, False, True), 3.50)

    #Prueba calculando el total esperado de un almuerzo ejecutivo con postre
    def test_total_lunchEjecutivo_postre(self):
        order = Order.objects.filter(include_dessert=True)[0]
        self.assertEqual(order.calculateCost(order.lunch, True, False), 3.75)

    #Prueba calculando el total esperado de un almuerzo ejecutivo con bebida y postre
    def test_total_lunchEjecutivo_ambos(self):
        order = Order.objects.self.filter(include_juice=True,include_dessert=True)[0]
        self.assertEqual(order.calculateCost(order.lunch, True, True), 4.25)

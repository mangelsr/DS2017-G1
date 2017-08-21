from django import forms

from catalogoapp.models.order import Order
from catalogoapp.models.schedule import Schedule

class OrderForm(forms.ModelForm):

    include_juice = forms.BooleanField(required=False, label='Adicional de jugo')
    include_dessert = forms.BooleanField(required=False,label='Adicional de postre')
    schedule = forms.ModelChoiceField(queryset=Schedule.objects.all(), label='Horario de retiro')
    PAYMENT_METHODS = (
        ("Tarjeta de credito", "Tarjeta de credito"),
        ("Carnet inteligente", "Carnet inteligente"),
        ("Efectivo", "Efectivo")
    )
    payment = forms.ChoiceField(widget=forms.RadioSelect,choices=PAYMENT_METHODS, label='Metodo de pago')

    class Meta:

        model = Order

        fields = [
            'include_juice',
            'include_dessert',
            'schedule',
            'payment',
        ]
from django import forms

from catalogoapp.models.order import Order
from catalogoapp.models.schedule import Schedule

class OrderForm(forms.ModelForm):

    customer = forms.CharField(widget=forms.HiddenInput())
    lunch = forms.CharField(widget=forms.HiddenInput())
    include_juice = forms.BooleanField(required=False, label='Adicional de jugo')
    include_dessert = forms.BooleanField(required=False,label='Adicional de postre')
    schedule = forms.ModelChoiceField(queryset=Schedule.objects.all(), label='Horario de retiro')
    cost = forms.CharField(widget=forms.HiddenInput())

    class Meta:

        model = Order

        fields = [
            'customer',
            'lunch',
            'include_juice',
            'include_dessert',
            'schedule',
            'cost',
        ]
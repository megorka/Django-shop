from django.forms import forms
from orders.models import Order

class OrderCreateForm(forms.ModelForms):
    username = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'form-control py-4',
        'placeholder': 'Введите имя пользователя'
    }))
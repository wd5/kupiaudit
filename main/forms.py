          # -*- coding: utf-8 -*-
from django.forms.models import BaseInlineFormSet
from django import forms
from django.forms import ModelForm
from cabinet.models import Order

class ClientForm(forms.Form):
    name = forms.CharField(max_length=100, label="Имя")
    email = forms.EmailField(max_length=100)

class OrderForm(ModelForm):
    class Meta:
        model = Order
        exclude = ('client', 'is_processed', 'pocket')

class BaseClientFormset(BaseInlineFormSet):
    def clean(self):
        self.validate_unique()
        if not self.forms[0].has_changed():
            raise forms.ValidationError("Сайт должен быть заполнен")
          # -*- coding: utf-8 -*-
from django import forms
from django.forms import ModelForm
from cabinet.models import Order
from django.contrib.auth.models import User

class ClientForm(forms.Form):
    name = forms.CharField(max_length=100, label="Имя")
    email = forms.EmailField(max_length=100)
    domen = forms.URLField(max_length=100, label="Сайт")
    contacts = forms.CharField(label="Контакты", widget=forms.Textarea, required=False)
    keywords = forms.CharField(label="Ключевые слова", widget=forms.Textarea, required=False)
    reason = forms.CharField(label="Причина обращения", widget=forms.Textarea, required=False)
    comment = forms.CharField(label="Комментарий", widget=forms.Textarea, required=False)

    def clean_email(self):
        data = self.cleaned_data['email']
        if User.objects.filter(username=data):
            raise forms.ValidationError("Пользователь с таким email уже есть")
        return data
    
class OrderForm(ModelForm):
    class Meta:
        model = Order
        exclude = ('client', 'is_processed', 'pocket')

    def clean_email(self):
        data = self.cleaned_data['email']
        if User.objects.get(username=data):
            raise forms.ValidationError("Пользователь с таким email уже есть")
        return data

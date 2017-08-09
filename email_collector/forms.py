from django import forms
from django.forms import ModelForm

from .models import Subscribe


class SubscribeForm(ModelForm):

    class Meta:
        model = Subscribe
        fields = '__all__'

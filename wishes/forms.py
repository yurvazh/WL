from django import forms

from django.urls import reverse

class ReserveForm (forms.Form):
    r_field = forms.BooleanField()

from django.contrib.auth.models import User
from django.shortcuts import render


from django.views.generic import CreateView, ListView

from django.contrib.auth.forms import UserCreationForm

class SignUpView (CreateView):
    form_class = UserCreationForm
    success_url = '/auth/login/'
    template_name = "users/signup.html"



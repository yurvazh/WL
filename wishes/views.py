from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from django.template import loader
from django.views.generic import DetailView, ListView
from django.views.generic import CreateView, UpdateView, DeleteView
from django.contrib.auth.models import Permission, User
from django.contrib.auth.mixins import PermissionRequiredMixin
from django.views.decorators.csrf import csrf_exempt, requires_csrf_token, csrf_protect
from .models import Present

# Create your views here.

def index(request):
    return HttpResponse("hello")

class PresentsView (ListView):
    model = Present
    template_name = "wishes/all_presents.html"

class PresentDetailView (DetailView):
    model = Present
    template_name = 'wishes/present_details.html'

def index1(request):
    return HttpResponse("тимофей пропиши delete")
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
    template = loader.get_template('wishes/index.html')
    return HttpResponse(template.render())

class PresentsView (ListView):
    model = Present
    template_name = "wishes/all_presents.html"

class PresentDetailView (DetailView):
    model = Present
    template_name = 'wishes/present_details.html'

def show_wishlist (request, us_id):
    all_wishes = Present.objects.all()
    wishes_by_id = []
    for pr in all_wishes:
        if (pr.creator == us_id):
            wishes_by_id.append(pr)
    context = {
        "WL" : wishes_by_id
    }
    return render(request, 'wishes/Wl.html', {"wl" : wishes_by_id})



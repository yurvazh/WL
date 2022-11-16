from django import forms
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from django.template import loader
from django.views.generic import DetailView, ListView
from django.views.generic import CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import Permission, User
from django.contrib.auth.mixins import PermissionRequiredMixin
from django.views.decorators.csrf import csrf_exempt, requires_csrf_token, csrf_protect
from .models import Present
from .forms import ReserveForm
# Create your views here.

def index(request):
    template = loader.get_template('wishes/index.html')
    return HttpResponse(template.render())

class PresentsView (ListView):
    model = Present
    template_name = "wishes/all_presents.html"

class PresentUpdateView (UpdateView):
    model = Present
    fields = ["reserved"]

class PresentCreateView (LoginRequiredMixin, CreateView):
    model = Present
    fields = ["title"]
    template_name = "wishes/present_create_form.html"

    def form_valid(self, form):
        form.instance.creator = 2
        return super().form_valid(form)

def presentdetailview (request, p_id):
    #if ((self.request.user).is_authenticated):
      #  return HttpResponse("ehagriouvbesr")
    present = get_object_or_404(Present, pk=p_id)
    if request.GET:
        temp = request.GET['r_field']
        if (str(temp) == "on"):
            present.reserved = True
    return render(request, 'wishes/present_details.html', {'present' : present, 'f' : PresentUpdateView(pk=p_id)})



def show_wishlist (request, us_id):
    all_wishes = Present.objects.all()
    wishes_by_id = []
    for pr in all_wishes:
        if (pr.creator == us_id):
            wishes_by_id.append(pr)
    context = {
        "WL": wishes_by_id,
        "uid" : us_id
    }
    return render(request, 'wishes/Wl.html', {"wl" : wishes_by_id, "uid" : us_id, "f" : ReserveForm()})



class PresentDeleteView (DeleteView):
    model = Present
    success_url = '/wishes'
    template_name = "wishes/present_confirm_delete.html"
from django.shortcuts import render
from django.forms import formset_factory
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from .models import VideoCard
from .forms import VideoCardForm
from django.urls import reverse_lazy
from django.forms import modelformset_factory

def home(request):
    return render(request, 'home.html')

class VDList(ListView):
    model = VideoCard
    template_name = 'home.html'
    context_object_name = 'vds'
    paginate_by = 3

class VDCreate(CreateView):
    model = VideoCard
    template_name = 'create.html'
    form_class = VideoCardForm
    success_url = reverse_lazy('home')

    

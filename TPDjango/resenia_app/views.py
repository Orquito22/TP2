from django.shortcuts import render

# Create your views here.

from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import View

from django.views.generic.list import ListView
from django.views.generic.edit import DeleteView, UpdateView, CreateView
from django.views.generic.detail import DetailView


from .models import Resenia

# Create your views here.


class ReseniaBaseView(View):
    template_name = 'resenia.html'
    model = Resenia
    fields = '__all__'
    success_url = reverse_lazy('resenia:resenia')


class ReseniaListView(ReseniaBaseView,ListView):
    """
    ESTO ME PERMITE CREAR UNA VISTA CON LAS RESEÑAS
    """


   

class ReseniaCreateView(ReseniaBaseView,CreateView):
    template_name = "resenia_create.html"
    extra_context = {
        "tipo": "Crear Reseña"
    }


class ReseniaEditView(ReseniaBaseView,UpdateView):
    template_name = "resenia_edit.html"
    extra_context = {
        "tipo": "Actualizar Reseña"
    }

class ReseniaDeleteView(ReseniaBaseView,DeleteView):
    template_name = "resenia_delete.html"
    extra_context = {
        "tipo": "Borrar Reseña"
    }

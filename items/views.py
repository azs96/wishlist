from django.shortcuts import render
from django.views.generic import CreateView, DeleteView, DetailView, ListView, UpdateView

from items.models import Item

# Create your views here.
class ItemListView(ListView):
  model = Item


class ItemCreateView(CreateView):
  model = Item
  fields = ['name', 'price', 'memo']
  success_url = "/"

class ItemDetailView(DetailView):
  model = Item

class ItemUpdateView(UpdateView):
  model = Item
  fields = ['name', 'price', 'memo']
  success_url = "/"

class ItemDeleteView(DeleteView):
  model = Item
  success_url = "/"
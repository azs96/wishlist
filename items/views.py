from django.shortcuts import render
from django.views.generic import ListView,CreateView

from items.models import Item

# Create your views here.
class ItemListView(ListView):
  model = Item


class ItemCreateView(CreateView):
  model = Item
  fields = ['name', 'price', 'memo']
  success_url = "/"
from django.shortcuts import render
from django.urls import reverse, reverse_lazy
from django.views.generic import CreateView, DeleteView, DetailView, ListView, UpdateView

from items.models import Item

# Create your views here.
class ItemListView(ListView):
  model = Item


class ItemCreateView(CreateView):
  model = Item
  fields = ['name', 'price', 'memo']
  success_url = reverse_lazy('item:index')

class ItemDetailView(DetailView):
  model = Item

class ItemUpdateView(UpdateView):
  model = Item
  fields = ['name', 'price', 'memo']

  def get_success_url(self):
    pk = self.kwargs.get('pk')
    return reverse('item:detail', kwargs={'pk': pk})

class ItemDeleteView(DeleteView):
  model = Item
  success_url = reverse_lazy('item:index')
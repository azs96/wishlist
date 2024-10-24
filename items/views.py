from django.contrib import messages
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

  def form_valid(self, form):
    messages.success(self.request, 'Registration Completed')
    return super().form_valid(form)

  def form_invalid(self, form):
    messages.error(self.request, 'Registration Failed')
    return super().form_invalid(form)

class ItemDetailView(DetailView):
  model = Item

class ItemUpdateView(UpdateView):
  model = Item
  fields = ['name', 'price', 'memo']

  def get_success_url(self):
    pk = self.kwargs.get('pk')
    return reverse('item:detail', kwargs={'pk': pk})
  
  def form_valid(self, form):
    messages.success(self.request, 'Update Completed')
    return super().form_valid(form)
  
  def form_invalid(self, form):
    messages.error(self.request, 'Update Failed')
    return super().form_invalid(form)

class ItemDeleteView(DeleteView):
  model = Item
  success_url = reverse_lazy('item:index')

  def form_valid(self, form):
    messages.success(self.request, 'Deletion Completed') # メッセージを表示
    return super().form_valid(form)
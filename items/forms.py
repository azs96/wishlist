from django import forms
from .models import Item, Tag

class ItemForm(forms.ModelForm):
  tags = forms.ModelMultipleChoiceField(
    queryset = Tag.objects.all(),
    widget = forms.CheckboxSelectMultiple,
    label = 'tags',
    required = False
  )

  class Meta:
    model = Item
    fields = ['name', 'memo', 'price', 'image', 'tags']
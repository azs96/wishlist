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

class ItemSearchForm(forms.Form):
  q = forms.CharField(required=False, label='Seach Words')
  tags = forms.ModelMultipleChoiceField(
    queryset = Tag.objects.all(),
    widget = forms.CheckboxSelectMultiple,
    label = 'tags',
    required = False
  )
  show_purchased = forms.BooleanField(
    required=False,
    label = "Show Purchased Items"
  )

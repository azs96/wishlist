from django.urls import path

from .views import (
  ItemListView, ItemCreateView,
  ItemDetailView, ItemUpdateView, ItemDeleteView, TagCreateView, TagDeleteView, TagListView, TagUpdateView,
  mark_as_purchased, mark_as_not_purchased
)

app_name = "item"

urlpatterns = [
    path('', ItemListView.as_view(), name="index"),
    path('create', ItemCreateView.as_view(), name="create"),
    path('<int:pk>/update', ItemUpdateView.as_view(), name="update"),
    path('<int:pk>/delete', ItemDeleteView.as_view(), name="delete"),
    path('<int:pk>', ItemDetailView.as_view(), name="detail"),
    path('<int:pk>/mark_as_purchased', mark_as_purchased, name="mark_as_purchased"),
    path('<int:pk>/mark_as_not_purchased', mark_as_not_purchased, name="mark_as_not_purchased"),
    path('tag', TagListView.as_view(), name="tag-index"),
    path('tag/<int:pk>/update', TagUpdateView.as_view(), name="tag-update"),
    path('tag/create', TagCreateView.as_view(), name="tag-create"),
    path('tag/<int:pk>/delete', TagDeleteView.as_view(), name="tag-delete"),
]
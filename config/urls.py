"""
URL configuration for config project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

from items.views import ItemCreateView, ItemDeleteView, ItemDetailView, ItemListView, ItemUpdateView
from lib.views import IndexTemplateView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('item/', ItemListView.as_view(), name="item-index"),
    path('item/create', ItemCreateView.as_view(), name="item-create"),
    path('item/<int:pk>', ItemDetailView.as_view(), name="item-detail"),
    path('item/<int:pk>/update', ItemUpdateView.as_view(), name="item-update"),
    path('item/<int:pk>/delete', ItemDeleteView.as_view(), name="item-delete"),
    path('', IndexTemplateView.as_view(), name="index"),
]

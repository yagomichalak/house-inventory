from django.urls import path, include
from . import views

app_name = 'inventory'

urlpatterns = [
    path('', views.InventoryView.as_view(), name='inventory'),
    path('add-item/', views.add_inventory_item, name='add_item'),
    path('remove-item/<int:pk>', views.remove_inventory_item, name='remove_item'),
]
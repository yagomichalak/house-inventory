from django.shortcuts import render
from django.views.generic import ListView
from . import models
from . import forms
from utils import utils

class InventoryView(ListView):
    """ View for the home page. """

    model = models.Inventory
    template_name = 'inventory/inventories.html'
    context_object_name = 'inventorylist'

    def get_context_data(self, **kwargs):
        context = super(InventoryView, self).get_context_data(**kwargs)


        all_objs = models.Inventory.objects.filter()
        new_dict = utils.group_item_dicts_by_cat(*all_objs, category="category_name")
        context['inventory_categories'] = new_dict

        context['form'] = forms.InventoryItemForm(data=self.request.POST)
        context['current'] = 'inventory'
        return context
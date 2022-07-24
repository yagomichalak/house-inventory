from django.http import JsonResponse, QueryDict, HttpResponseRedirect, HttpResponse
from django.views.generic import ListView
from django.shortcuts import get_object_or_404
from . import models
from . import forms
from utils import utils
import requests
from typing import Dict, Union

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

def add_inventory_item(request) -> requests.Response:
    """ Creates an inventory item.
    :param request: The request. """

    data = qdict_to_dict(request._post)

    # Creates an Inventory Item
    item = models.Inventory.objects.create(
        name=data.get("name"),
        price=data.get("price"),
        measure_unit=data.get("measure_unit"),
        category_name=data.get("category_name")
    )
    print(item)

    return HttpResponseRedirect('/inventory/')

def remove_inventory_item(request, pk: int) -> requests.Response:
    """ Removes an item from the inventory.
    :param request: The request.
    :param pk: The item's primary key. """

    # Deletes inventory item from Django's DB
    item = get_object_or_404(models.Inventory, pk=pk)
    item.delete()
    print(item)

    return HttpResponseRedirect('/inventory/')


def qdict_to_dict(qdict: QueryDict) -> Dict[str, Union[str, int, float]]:
    """ Converts a Django QueryDict to a Python dict.

    Single-value fields are put in directly, and for multi-value fields, a list
    of all values is stored at the field's key.
    :param qdict: The query dict to convert to dict.

    """
    return {k: v[0] if len(v) == 1 else v for k, v in qdict.lists()}

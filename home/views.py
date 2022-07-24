from msilib.schema import ListView
from django.shortcuts import render
from . import models
from django.views.generic import ListView

class HomeOverview(ListView):
    """ View for the home page. """

    model = models.HomeOverview
    template_name = 'home/overview.html'
    context_object_name = 'homeoverview'
from django.shortcuts import render
from django.views.generic import TemplateView

class HomePage(TemplateView):
    template_name = 'pages/home.html'


# Create your views here.

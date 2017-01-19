from django.shortcuts import render
from django.views import generic


# Create your views here.
class Indexview(generic.TemplateView):
    template_name = "public/index.html"

from django.shortcuts import render
from django.views.generic import TemplateView

class Index(TemplateView):
    template_name = "index.html"

class Contact(TemplateView):
    template_name = "contact.html"

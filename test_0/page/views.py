from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

from django.views.generic import TemplateView

# function based views
# def homePageView(request):
#     return HttpResponse("Hello, World!")

# Class-Based Views
class HomePageView(TemplateView):
    template_name = "home.html"    

class AboutPageView(TemplateView):  # new
    template_name = "about.html"
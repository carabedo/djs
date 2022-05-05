# pages/urls.py
from django.urls import path
from .views import HomePageView, AboutPageView 

urlpatterns = [

    path("about/", AboutPageView.as_view(), name="about"),  # new

    path("", HomePageView.as_view(), name="home"),
]


# Our URL pattern has three parts:

# a Python regular expression for the empty string ""
# a reference to the view called homePageView
# an optional named URL pattern called "home"
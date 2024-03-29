"""cfehome URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
from resturants.views import (
    home,
    home1,
    home2,
    ContactView,
    ContactTemplateView,
    AboutTemplateView,
    resturants_listview,
    MexicanResturantListView,
    AsianturantListView,
    ResturantDetaiView,
)
from django.views.generic import TemplateView

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", home),
    path("about/", AboutTemplateView.as_view()),
    path("contact/", ContactTemplateView.as_view()),
    path("resturants/", resturants_listview),
    path("resturants/mexican/", MexicanResturantListView.as_view()),
    path("resturants/asian/", AsianturantListView.as_view()),
    path("resturants/<int:pk>", ResturantDetaiView.as_view()),
]

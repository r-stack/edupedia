# -*- coding: utf-8 -*-
from django.conf.urls import patterns, include, url
from django.views.generic import TemplateView
from epsearch import views
from epsearch.views import SearchView



urlpatterns = patterns('',
  url(r'^$', TemplateView.as_view(template_name="epsearch/index.html"), name="index"),
  url(r'^search/$', SearchView.as_view(), name="search"),
)
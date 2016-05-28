# -*- coding: utf-8 -*-
from django.conf.urls import patterns, include, url
from django.views.generic import TemplateView
from epsearch import views



urlpatterns = patterns('',
  url(r'^$', TemplateView.as_view(template_name="nicoboard/index.html"), name="index"),
#  url(r'^$', IndexView.as_view(), name="index"),
)
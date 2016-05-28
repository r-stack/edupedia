from django.shortcuts import render
from django.views.generic import TemplateView

import hakipedia
from epsearch.models import Page
# Create your views here.
class IndexView(TemplateView):
    template_name = "index.html"
    
    def post(self, request, *args, **kwargs):
        print "post"
        
        body = hakipedia.fetch_wiki()
        body.split()
        
        
        return self.get(request, *args, **kwargs)
        
        
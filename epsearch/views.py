#encoding=utf-8
import logging

from django.shortcuts import render
from django.views.generic import TemplateView

from epsearch import docomo_analys
from epsearch.hakipedia import fetch_wiki
from epsearch.keyword_to_image_url import GoogleImageConverter, GoogleMapConverter
from epsearch.models import Page, Sentence


L = logging.getLogger(__name__)


class SearchView(TemplateView):
    template_name = "epsearch/search2.html"

    def get(self, request, *args, **kwargs):
        context = self.get_context_data(**kwargs)
        context["page"] = load_page(pagename=request.GET.get("k"),
                                    force=request.GET.get("f"))
        context["sentences"] = context["page"].sentence_set.all()
        return self.render_to_response(context)




CONVERT_MAP = {
       "PSN":GoogleImageConverter,
       "LOC":GoogleMapConverter,
       }

def load_page(pagename, limit=5, force=False):
    if not pagename:
        return
    pagename = pagename.strip()
    L.debug( u"[S] load_page: %s" % pagename )
    try:
        if force:
            Page.objects.filter(url=pagename).delete()
        page = Page.objects.get(url=pagename)
    except Page.DoesNotExist:
        page = process_data(pagename, limit)

    return page

def process_data(pagename, limit=5):
    pagename = pagename.strip()
    L.debug( u"[S] process_data: %s" % pagename )
    page = Page()
    page.url = pagename
    page.save()

    body = fetch_wiki(pagename)

    lines = body.split(u"。")
    cnt = 0;
    for line in lines:
        if limit > 0 and cnt > limit:
            L.debug( "limit sentence")
            break
        cnt = cnt + 1
        sen = Sentence()
        sen.page = page
        sen.body = line + u"。"
        sen.save()
        terms = docomo_analys.analysys(sen.body)
        for term in terms:
            term.sentence = sen
            term.save()
            converter = CONVERT_MAP.get(term.term_class)
            if not converter:
                continue
            term.result, term.comment = converter().convert_term(term.body)
            term.save()
    L.debug("[E] process_data")
    return page

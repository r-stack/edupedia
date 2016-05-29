# -*- coding: utf-8 -*-
# last modified:   May 30, 2016 by @kwbt69

from django.conf import settings
from googleapiclient.discovery import build
from epsearch import BaseConverter

GOOGLE_API_KEY = settings.GOOGLE_API_KEY
GOOGLE_SEARCH_ENGINE_ID = settings.GOOGLE_SEARCH_ENGINE_ID


class GoogleImageConverter(BaseConverter):
    api_key = GOOGLE_API_KEY
    
    
    def convert_term(self, term):

        service = build("customsearch", "v1", developerKey=self.api_key)
        
        request = service.cse().list(
            q = term,
            cx = GOOGLE_SEARCH_ENGINE_ID,
            fileType = 'png,jpg',
            imgSize = 'large',
            imgType = 'face',
            lr = 'lang_ja',
            num = '1',
            searchType = 'image')

        res = request.execute()
        items = res.get("items", [])
        if len(items):
            link = items[0].get("link")
        else:
            link = ""
        return link, res


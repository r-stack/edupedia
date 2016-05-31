# -*- coding: utf-8 -*-
# @Author: kwbt69
# @Date:   2016-05-30T23:14:06+09:00
# @Last modified by:   kwbt69
# @Last modified time: 2016-06-01T01:18:44+09:00

import urllib
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


class GoogleMapConverter(BaseConverter):

    def convert_term(self, term):

        items = []
        items.append("https://maps.googleapis.com/maps/api/staticmap?center=")
        items.append(term)
        items.append("&markers=")
        items.append(term)
        items.append("&size=800x600&sensor=false&zoom=7")

        return ''.join(items), ''
#       return urllib.quote(''.join(items))

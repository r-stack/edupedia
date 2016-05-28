# -*- coding: utf-8 -*-
# last modified <17:56:38 JST 05/28/2016 @kwbt69>


from googleapiclient.discovery import build
from epsearch import BaseConverter


class GoogleImageConverter(BaseConverter):
    api_key = 'AIzaSyBkRpJPVgCK3BO3kNTip93-kRNarrdYg2A'

    
    def convert_term(self, term):

        service = build("customsearch", "v1", developerKey=self.api_key)
        
        request = service.cse().list(
            q = term,
            cx = '004575836146253961634:ahvjukvxrc8',
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


# -*- coding: utf-8 -*-
# last modified <17:56:38 JST 05/28/2016 @kwbt69>

from edupedia.epsearch.models import Term
from googleapiclient.discovery import build

api_key = 'AIzaSyBkRpJPVgCK3BO3kNTip93-kRNarrdYg2A'

    
def keyword_to_image_url(term):

    service = build("customsearch", "v1", developerKey=api_key)
    
    request = service.cse().list(
        q = term.body,
        cx = '004575836146253961634:ahvjukvxrc8',
        fileType = 'png,jpg',
        imgSize = 'large',
        imgType = 'face',
        lr = 'lang_ja',
        num = '1',
        searchType = 'image')

    term.response = request.execute()




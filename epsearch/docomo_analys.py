# -*- coding: utf-8 -*-
import os
from django.conf import settings
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "edupedia.settings")

import logging

import requests

from epsearch import models

L = logging.getLogger(__name__)

def analysys(sentence):

    key = settings.DOCOMO_API_KEY
    headers = {'content-type': 'application/x-www-form-urlencoded '}
    apiurl = settings.DOCOMO_GOO_LANG_ANALYSIS_ENDPOINT
    response = requests.post(
        apiurl,
        params={'APIKEY': key,
                'sentence': sentence},
        headers=headers)

    L.debug(response.json())

    terms = []
    for ne in response.json()['ne_list']:
        L.debug(ne)
        term = models.Term()

        term.body = ne[0]
        term.term_class = ne[1]

        terms.append(term)

    return terms


def main():

    sample = '甲斐の守護を務めた甲斐源氏武田家第18代・武田信虎の嫡男。先代・信虎期に武田氏は戦国大名化し国内統一を達成し、信玄も体制を継承して隣国・信濃に侵攻する。'

    result = analysys(sample)
    L.debug(len(result))
    L.debug(result)

if __name__ == '__main__':
    main()

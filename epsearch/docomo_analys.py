# -*- coding: utf-8 -*-
import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "edupedia.settings")

import requests

from epsearch import models

def analysys(sentence):

    key = '6734506772503357725245703873375844693535414954595a756e362e4f30582f764748426f4c4c615138'
    key = '4e6f766d784b35464f66574e2f5a334d586a6c316e42724e5a384c62364335437734497235777a396d4534'
    headers = {'content-type': 'application/x-www-form-urlencoded '}
    apiurl = 'https://api.apigw.smt.docomo.ne.jp/gooLanguageAnalysis/v1/entity'
    apiurl = 'https://api.apigw.smt.docomo.ne.jp/gooLanguageAnalysisCorp/v1/entity'
    response = requests.post(
        apiurl,
        params={'APIKEY': key,
                'sentence': sentence},
        headers=headers)

    print(response.json())

    terms = []
    for ne in response.json()['ne_list']:
        print(ne)
        term = models.Term()

        term.body = ne[0]
        term.term_class = ne[1]

        terms.append(term)

    return terms


def main():

    sample = '甲斐の守護を務めた甲斐源氏武田家第18代・武田信虎の嫡男。先代・信虎期に武田氏は戦国大名化し国内統一を達成し、信玄も体制を継承して隣国・信濃に侵攻する。'

    result = _analysys(sample)
    print(len(result))
    print(result)

if __name__ == '__main__':
    main()

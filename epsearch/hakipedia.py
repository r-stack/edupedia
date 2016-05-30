# encoding=utf-8

'''
Created on 2016/05/28

@author: 20008112
'''
# coding: utf-8

import json
import logging
import urllib
import urllib2

import WikipediaExtractor

L = logging.getLogger(__name__)

URL = 'http://ja.wikipedia.org/w/api.php?'
BASIC_PARAMETERS = {'action': 'query',
                   'format': 'xml'}






class WikiHandler(object):
    def __init__(self, parameters, titles=None, url=URL):
        self._url = url if url.endswith('?') else url + '?'

        self._parameters = {}
        self._parameters.update(BASIC_PARAMETERS)
        self._parameters.update(parameters)

        if titles:
            self._parameters['titles'] = titles

        self.rawdata = self._urlfetch(self._parameters)

    def _urlfetch(self, parameters):
        parameters_list = []

        for key, val in parameters.items():
            L.debug (key + ', ' + val)
            if isinstance(val, basestring):
                val = val.encode('utf-8')
                pass
            else:
                val = str(val)

            val = urllib.quote(val)
            parameters_list.append('='.join([key, val]))

        url = self._url + '&'.join(parameters_list)

        L.debug('Accessing...\n', url)

        return urllib2.urlopen(url, timeout=20)



def fetch_wiki(pagename=u'武田信玄'):
    parameters = {
        'format': 'json',
        'prop': 'revisions',
        'rvprop': 'content'
    }
    
    page = WikiHandler(parameters, pagename)
    # L.debug(page.rawdata.read())
    result_json = json.loads(page.rawdata.read())
    # L.debug(page.rawdata.read())
    #    with open("tmp.txt", "w") as f:
    #        f.write(json.dumps(result_json, indent=2))
    
    revisions = result_json.pop('query').pop('pages').items()[0][1].pop('revisions')
    current = revisions[0]['*']
    
    global escape_doc
    escape_doc = False
    
    lines = current.split()
    text = WikipediaExtractor.Extractor(1, "titleA", lines).clean()
    return text


        



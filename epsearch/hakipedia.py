# encoding=utf-8

'''
Created on 2016/05/28

@author: 20008112
'''
# coding: utf-8

import json
import urllib
import urllib2
import re
from xml.dom.minidom import parse as parseXML
import WikipediaExtractor
from epsearch.models import Sentence, Page
from epsearch import docomo_analys

URL = 'http://ja.wikipedia.org/w/api.php?'
BASIC_PARAMETERS = {'action': 'query',
                   'format': 'xml'}



# Match external links (space separates second optional parameter)
externalLink = re.compile(r'\[\w+[^ ]*? (.*?)]')
externalLinkNoAnchor = re.compile(r'\[\w+[&\]]*\]')

# Matches bold/italic
bold_italic = re.compile(r"'''''(.*?)'''''")
bold = re.compile(r"'''(.*?)'''")
italic_quote = re.compile(r"''\"([^\"]*?)\"''")
italic = re.compile(r"''(.*?)''")
quote_quote = re.compile(r'""([^"]*?)""')

# Matches space
spaces = re.compile(r' {2,}')

# Matches dots
dots = re.compile(r'\.{4,}')


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
           print (key + ', ' + val)
           if isinstance(val, basestring):
               val = val.encode('utf-8')
               pass
           else:
               val = str(val)

           val = urllib.quote(val)
           parameters_list.append('='.join([key, val]))

       url = self._url + '&'.join(parameters_list)

       print 'Accessing...\n', url

       return urllib2.urlopen(url, timeout=20)


import WikipediaExtractor

def fetch_wiki(pagename=u'武田信玄'):
   parameters = {
       'format': 'json',
       'prop': 'revisions',
       'rvprop': 'content'
   }

   page = WikiHandler(parameters, pagename)
   # print(page.rawdata.read())
   result_json = json.loads(page.rawdata.read())
   # print(page.rawdata.read())
#    with open("tmp.txt", "w") as f:
#        f.write(json.dumps(result_json, indent=2))

   revisions = result_json.pop('query').pop('pages').items()[0][1].pop('revisions')
   current = revisions[0]['*']
   
   global escape_doc
   escape_doc = False
   
   lines = current.split()
   text = WikipediaExtractor.Extractor(1,"titleA",lines).clean()
   return text

def main(pagename, limit=50):
    pagename = pagename.strip()
    page = Page()
    page.url = pagename
    page.save()
    
    body = fetch_wiki(pagename)
    print body
    lines = body.split(u"。")
    cnt = 0;
    for line in lines:
        if limit > 0 and cnt > limit:
            print "limit sentence"
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
        



if __name__ == '__main__':
   print main(u'武田信玄')
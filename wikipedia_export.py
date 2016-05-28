#coding:utf-8
import json, urllib2

url = 'https://ja.wikipedia.org/w/api.php?format=json&action=query&prop=revisions&rvprop=content&titles=%e3%83%89%e3%83%a9%e3%82%b4%e3%83%b3%e3%83%9c%e3%83%bc%e3%83%ab%e3%81%ae%e4%b8%96%e7%95%8c%e3%81%ab%e3%81%8a%e3%81%91%e3%82%8b%e5%b9%b4%e8%a1%a8'
try:
    r = urllib2.urlopen(url)
    root = json.loads(r.read())
    revisions = root['query']['pages']['902331']['revisions']
    for rev in revisions:
        results = rev['*'].split()
        for result in results:
            if result.startswith(':'):
                continue
            elif result.startswith(';'):
                continue
            elif result.startswith('='):
                continue
            elif result.startswith('{'):
                continue
            elif result.startswith('|'):
                continue
            print result
#            if result.count(U'エイジ'):
#                print result

finally:
    r.close()

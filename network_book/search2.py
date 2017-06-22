#!/usr/bin/env python
# Python Network Programming - CH1 - search2.py

import urllib, urllib2

try:
    import json
except ImportError: #default error class: response to trying to run on Python 2.5
    import simplejson as json

params = {'q':'207 N. Defiance St, Archbold, OH', 'output':'json', 'oe':'utf8'}
url = 'https://www.google.co.uk/#' + urllib.urlencode(params)

raw_reply = urllib2.urlopen(url).read()
#reply = json.loads(raw_reply)

# print reply
print raw_reply
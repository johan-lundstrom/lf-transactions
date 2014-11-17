#!/usr/bin/python
# -*- coding: utf-8 -*-

"""An attemt to gather Länsförsäkringar account history to be presented in charts etc.

Sources of inspiration:

https://github.com/liato/android-bankdroid/blob/master/app/src/main/java/com/liato/bankdroid/banking/banks/lansforsakringar/Lansforsakringar.java

http://blog.sallarp.com/lansforsakringar-api.html
"""

import requests
import hashlib
import json
import collections

url = 'https://mobil.lansforsakringar.se/appoutlet/security/client'
r = requests.get(url)
j = r.json()
n = j['number']
p = j['numberPair']

offset = (1000 * 20 / 4) + 100 * (18 / 3) + 10 * (2 / 2) + 6
m = n + offset
h = hex(m)[2:]
s = hashlib.sha1(h).hexdigest()

assert len(s) == 40

#header = {"Content-type": "application/json; charset=UTF-8"}
data = {"originalChallenge":n,"hash":s,"challengePair":p}
#data2 = collections.OrderedDict([("originalChallenge", n), ("hash", s), ("challengePair", p)])
dump = json.dumps(data)

#r2 = requests.post(url, data=dump)

print r2.status_code
print r2.headers

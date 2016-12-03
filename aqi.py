#!/usr/bin/python

import urllib2
import json

req = urllib2.Request('https://waqi.info/api/feed/@1451/now.json')
req.add_header('user-agent', 'Mozilla/5.0')
req.add_header('origin', 'http://aqicn.org')
req.add_header('referer', 'http://aqicn.org/city/all/')
data = urllib2.urlopen(req).read()
result = json.loads(data)
# print result
urllib2.urlopen('https://maker.ifttt.com/trigger/aqi_beijing/with/key/dAQW2GcyRqhfLeXHFs1Tn5?value1=' + str(result['rxs']['obs'][0]['msg']['aqi']))

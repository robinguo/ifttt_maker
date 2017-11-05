#!/usr/bin/python

import urllib2
import json
import time

req = urllib2.Request('http://feed.aqicn.org/xservices/refresh:1451?_' + str(time.time()))
data = urllib2.urlopen(req).read()
result = json.loads(data)
# print result
urllib2.urlopen('https://maker.ifttt.com/trigger/aqi_beijing/with/key/dAQW2GcyRqhfLeXHFs1Tn5?value1=' + str(result['aqiv']))

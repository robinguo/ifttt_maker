#!/usr/bin/python

import urllib2
import json

req = urllib2.Request('https://api.waqi.info/feed/beijing/?token=2c22270e805a1277556ece6875e209383ad86a75')
data = urllib2.urlopen(req).read()
result = json.loads(data)
# print result
urllib2.urlopen('https://maker.ifttt.com/trigger/aqi_beijing/with/key/dAQW2GcyRqhfLeXHFs1Tn5?value1=' + str(result['data']['aqi']))

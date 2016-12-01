#!/usr/bin/python

import urllib2
import json

data = urllib2.urlopen('https://waqi.info/api/feed/@1451/obs.en.json').read()
result = json.loads(data)
urllib2.urlopen('https://maker.ifttt.com/trigger/aqi_beijing/with/key/dAQW2GcyRqhfLeXHFs1Tn5?value1=' + str(result['rxs']['obs'][0]['msg']['aqi']))

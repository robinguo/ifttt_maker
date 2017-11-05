import json
import urllib2

data = urllib2.urlopen('https://blockchain.info/ticker').read()
results = json.loads(data)
urllib2.urlopen('https://maker.ifttt.com/trigger/btcc_ticker/with/key/dAQW2GcyRqhfLeXHFs1Tn5?value1=' + str(results['USD']['last']) + '&value2=' + str(results['USD']['symbol']))

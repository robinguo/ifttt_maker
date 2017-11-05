import json
import urllib2

data = urllib2.urlopen('https://api.coinmarketcap.com/v1/ticker/ethereum/').read()
results = json.loads(data)
urllib2.urlopen('https://maker.ifttt.com/trigger/eth_ticker/with/key/dAQW2GcyRqhfLeXHFs1Tn5?value1=' + str(results[0]['price_usd']) + '&value2=' + str(results[0]['price_usd']))

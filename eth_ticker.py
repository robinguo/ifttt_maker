import json
import urllib2

data = urllib2.urlopen('https://yunbi.com/api/v2/tickers/ethcny.json').read()
results = json.loads(data)
urllib2.urlopen('https://maker.ifttt.com/trigger/eth_ticker/with/key/dAQW2GcyRqhfLeXHFs1Tn5?value1=' + str(results['ticker']['last']) + '&value2=' + str(results['ticker']['vol']))

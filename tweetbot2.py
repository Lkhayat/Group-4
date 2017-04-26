from twython import Twython
import csv

CONSUMER_KEY = 'W7c3yGpde3tiF4Qk1JUVTazVX'
CONSUMER_SECRET = 'VVvY5r7aku0sHSTNngOcBTeFF4noHmM0CnG7XXs9FX6i4AEKi0'
ACCESS_TOKEN = '855555686448627712-zsx8Wz3iAW03dHqNE2ph6eJeBEJud08'
ACCESS_TOKEN_SECRET = 'LfWQVoFKnOHhjxKJulvfj1XgDVPMKBXIsrddG3iGHAb54'

twitter = Twython(CONSUMER_KEY, CONSUMER_SECRET, ACCESS_TOKEN, ACCESS_TOKEN_SECRET)

search = twitter.search(q='YOUR SEARCH TERM HERE', count="100")
tweets = search['statuses']

with open ('data.csv', 'w') as fp:
    a = csv.writer(fp)
    # add a header row
    a.writerow(('Search Term', 'Tweet Text', 'URL'))

    for result in tweets:
        try:
            url = result['entities']['urls'][0]['expanded_url']
        except:
            url = None
        text=[['propublica', result['text'].encode('utf-8'), url]]
        a.writerows((text))
from twython import Twython
import csv
CONSUMER_KEY = 'W7c3yGpde3tiF4Qk1JUVTazVX'
CONSUMER_SECRET = 'VVvY5r7aku0sHSTNngOcBTeFF4noHmM0CnG7XXs9FX6i4AEKi0'
ACCESS_TOKEN = '855555686448627712-zsx8Wz3iAW03dHqNE2ph6eJeBEJud08'
ACCESS_TOKEN_SECRET = 'LfWQVoFKnOHhjxKJulvfj1XgDVPMKBXIsrddG3iGHAb54'

twitter = Twython(CONSUMER_KEY, CONSUMER_SECRET, ACCESS_TOKEN, ACCESS_TOKEN_SECRET)

search = twitter.search(q='GW Colonials', count="100")
tweets = search['statuses']


with open ('data.csv', 'w') as fp:
    a = csv.writer(fp)
    # add a header row
    a.writerow(('GW Colonials', 'Tweet Text', 'URL'))
    
    for result in tweets:
        try:
            url = result['entities']['urls'][0]['expanded_url']
        except:
            url = None
        text=[['propublica', result['text'].encode('utf-8'), url]]
        a.writerows((text))
        
        
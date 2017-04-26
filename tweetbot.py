from twython import Twython, TwythonError

CONSUMER_KEY = 'W7c3yGpde3tiF4Qk1JUVTazVX'
CONSUMER_SECRET = 'VVvY5r7aku0sHSTNngOcBTeFF4noHmM0CnG7XXs9FX6i4AEKi0'
ACCESS_TOKEN = '855555686448627712-zsx8Wz3iAW03dHqNE2ph6eJeBEJud08'
ACCESS_TOKEN_SECRET = 'LfWQVoFKnOHhjxKJulvfj1XgDVPMKBXIsrddG3iGHAb54'

twitter = Twython(CONSUMER_KEY, CONSUMER_SECRET, ACCESS_TOKEN, ACCESS_TOKEN_SECRET)

try:
    twitter.update_status(status='See how easy this was?')
except TwythonError as e:
    print e

# read from csv

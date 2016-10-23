import requests
import json
import logging

class XboxLive:
    XBOX_API_URL = 'https://xboxapi.com'

    def __init__(self, api_key):
        self._api_key = api_key
        self._auth_header = { 'X-AUTH': self._api_key }
    
    # Fetches all the friends for the Gamertag associated with api_key
    def call_api(self, endpoint):
        request_url = '{address}{endpoint}'.format(address=XBOX_API_URL, endpoint=endpoint)

        try:
            r = requests.get(request_url, headers=self._auth_header)
            r.raise_for_status()
            return json.loads(r.text)
            
        except requests.HTTPError:  
            logging.critical('Unable to call %s', request_url, exc_info=True)
        except requests.ConnectionError:
            logging.critical('Unable to connect to XboxAPI at address %s', request_url, exc_info=True)

    
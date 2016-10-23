import logging
import json
from src.xboxliveapi import XboxLive

class SlackBoxLive:
    def __init__(self, api_key, user_id):
        self._friends = []
        self._xbox_api = XboxLive(api_key)
        self._user_id = self._get_user_id() if user_id is None else user_id

    # Fetches all the friends for the Gamertag associated with api_key
    def _get_friends(self):
        self._friends_raw = self._xbox_api.call_api('/v1/{user_id}/friends'.format(user_id=self._user_id))

    # Creates a dictionary of { Gamertag: xuid }
    def _parse_friends(self):
        for friend in self._friends_raw:
            friend_status = { 'Gamertag': friend['Gamertag'], 'Id': friend['id'] }
            self._friends.append(friend_status)

    def _get_user_id(self):
        resp = self._xbox_api.call_api('/v2/accountXuid')
        return resp['xuid']

    def _find_friends_presense(self):
        #{ 
        #    "xuid":<ID>,
        #    "state":"Offline",
        #    "lastSeen":
        #        { 
        #            "deviceType": "XboxOne",
        #            "titleId": <titleId>,
        #            "titleName":"Home",
        #            "timestamp":"2016-10-21T06:48:56.008978Z"
        #        }
        #}
        for friend in self._friends:
            endpoint = '/v2/{id}/presence'.format(id=friend['Id'])
            presence = self._xbox_api.call_api(endpoint)
            friend['State'] = presence['state']

    # TODO: This is the core service that will monitor friends
    def _monitor(self):
        pass

    


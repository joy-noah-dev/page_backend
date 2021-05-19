import requests
import json
from config import RIOT_API_KEY


def api_wrapper(func):
    def wrapper(self, *args, **kwargs):
        """"""
        response = func(self, *args, **kwargs)
        if response.status_code == 200:
            return json.loads(response.text)
        else:
            raise Exception
    return wrapper


class RiotService:
    def __init__(self, region="americas"):
        self.__api_key = RIOT_API_KEY
        self.__host = f"https://{region}.api.riotgames.com"

    @api_wrapper
    def get_account_by_id(self, player_uuid):
        uri = f"{self.__host}/riot/account/v1/accounts/by-puuid/{player_uuid}?api_key={self.__api_key}"
        return requests.get(uri)

    @api_wrapper
    def get_account_by_data(self, game_name, tag_line):
        uri = f"{self.__host}/riot/account/v1/accounts/by-riot-id/{game_name}/{tag_line}?api_key={self.__api_key}"
        return requests.get(uri)

    @api_wrapper
    def get_ranked_leader_boards(self):
        uri = f"{self.__host}/lor/ranked/v1/leaderboards?api_key={self.__api_key}"
        return requests.get(uri)

    @api_wrapper
    def get_match(self, match_id):
        uri = f"{self.__host}/lor/match/v1/matches/{match_id}?api_key={self.__api_key}"
        return requests.get(uri)

    @api_wrapper
    def get_matches(self, player_uuid):
        uri = f"{self.__host}/lor/match/v1/matches/by-puuid/{player_uuid}/ids?api_key={self.__api_key}"
        return requests.get(uri)

    @api_wrapper
    def get_server_status(self):
        uri = f"{self.__host}/lor/status/v1/platform-data?api_key={self.__api_key}"
        return requests.get(uri)
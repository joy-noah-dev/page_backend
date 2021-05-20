from utils.riot_service_utils import RiotService


class LorMatchesController:
    @staticmethod
    def get_user_lor_matches(game_name, server_tag):
        """"""
        matches_data = []
        riot = RiotService()
        user = riot.get_account_by_data(game_name, server_tag)
        matches = riot.get_matches(user["puuid"])
        for match in matches[0:10]:
            matches_data.append(riot.get_match(match))
        return matches_data
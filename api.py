# External packages
from flask_restful import Api

from resources.check_resource import CheckResource
from resources.lor_matches_resource import LorMatchesResource
from resources.lor_deck_resource import LorDeckResource


def set_up_api(app):
    api = Api(app)

    api.add_resource(CheckResource, '/')
    api.add_resource(LorMatchesResource, '/LOR/matches/<game_name>/<server_tag>')
    api.add_resource(LorDeckResource, '/LOR/deck/decode/<deck_string>')
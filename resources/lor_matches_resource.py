from flask import jsonify
from flask_restful import Resource
from controllers.lor_matches_controller import LorMatchesController


class LorMatchesResource(Resource):
    """
    Lor matches API Endpoints
    """
    def get(self, game_name, server_tag):
        """
        Return a list of games for the given user
        """
        return jsonify(LorMatchesController.get_user_lor_matches(game_name, server_tag))
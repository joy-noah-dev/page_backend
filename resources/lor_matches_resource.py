from flask import jsonify
from flask_restful import Resource
from controllers.lor_matches_controller import LorMatchesController


class LorMatchesResource(Resource):
    """
    Check API Endpoints
    """
    def get(self, game_name, server_tag):
        """
        Return It's working to identify service status
        """
        return jsonify(LorMatchesController.get_user_lor_matches(game_name, server_tag))
from flask_restful import Resource
from controllers.lor_deck_controller import LorDeckController


class LorDeckResource(Resource):
    """
    Check API Endpoints
    """
    def get(self, deck_string):
        """
        Return It's working to identify service status
        """
        return LorDeckController().decode_deck(deck_string)

    def post(self):
        """"""
        return "It`s working"
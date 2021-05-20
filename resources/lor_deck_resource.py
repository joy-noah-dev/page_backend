from flask_restful import Resource
from controllers.lor_deck_controller import LorDeckController


class LorDeckResource(Resource):
    """
    Lor deck API resource
    """
    def get(self, deck_string):
        """
        Return a list of the cards on a deck with all metadata
        """
        return LorDeckController().decode_deck(deck_string)

from flask_restful import Resource
from utils.lor_deck_utils import LORDeckUtils


class LorAllCardsResource(Resource):
    """
    Check API Endpoints
    """
    def get(self):
        """
        Return It's working to identify service status
        """
        return LORDeckUtils().get_sets_list()
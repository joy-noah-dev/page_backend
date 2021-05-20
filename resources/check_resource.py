from flask_restful import Resource


class CheckResource(Resource):
    """
    Check API Endpoints
    """
    def get(self):
        """
        Return It's working to identify service status
        """
        return "It's working"
from os import environ
from dotenv import load_dotenv

load_dotenv()

NUMBER_OF_SETS = int(environ.get('NUMBER_OF_SETS'))
RIOT_API_KEY = environ.get('RIOT_API_KEY')
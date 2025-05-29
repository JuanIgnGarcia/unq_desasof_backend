import os
from dotenv import load_dotenv

load_dotenv()

# ML
BASE_URL = "https://api.mercadolibre.com"
CLIENT_ID = os.environ.get("CLIENT_ID")
CLIENT_SECRET = os.environ.get("CLIENT_SECRET")
REFRESH_TOKEN = os.environ.get("REFRESH_TOKEN")
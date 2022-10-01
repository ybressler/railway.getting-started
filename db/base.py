import os

ATLAS_DATA_API_KEY = os.environ.get("ATLAS_DATA_API_KEY")
DATA_API_BASE_URL = os.environ.get("DATA_API_BASE_URL")

headers = {
  'Content-Type': 'application/json',
  'Access-Control-Request-Headers': '*',
  'api-key': ATLAS_DATA_API_KEY
}

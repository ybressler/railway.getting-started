import json
import requests


payload = json.dumps({
    "collection": "tech_roles",
    "database": "superblocks",
    "dataSource": "Cluster0",
    "projection": {
        "_id": 1
    }
})
headers = {
  'Content-Type': 'application/json',
  'Access-Control-Request-Headers': '*',
  'api-key': "FOO"
}

response = requests.request("POST", url, headers=headers, data=payload)

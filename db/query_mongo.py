import json
import requests

from typing import List

from .base import DATA_API_BASE_URL, headers


def get_tech_roles() -> dict:
    """
    Gets all of the tech roles in the db
    """

    if not DATA_API_BASE_URL:
        return {
            "msg": "Environment is not set up to connect with Mongo Atlas"
        }

    url = f'{DATA_API_BASE_URL}/find'

    request_body = {
        "dataSource": "Cluster0",
        "database": "superblocks",
        "collection": "tech_roles",
        "projection": {
            "_id": 0,
            "role_name": 1
        },
        "sort": {
            "role_name": 1
        }
    }

    payload = json.dumps(request_body)
    response = requests.request("POST", url, headers=headers, data=payload)

    if response.status_code != 200:
        raise ValueError("Did not get good response back")

    data = response.json()
    records: List[dict] = data['documents']
    role_names: List[str] = [x["role_name"] for x in records if x["role_name"]]

    # Some fun stuff
    longest_name = max(role_names, key=len)
    shortest_name = min(role_names, key=len)

    # Otherwise
    return {
        "nice_message": f"There are {len(role_names):,} distinct tech role names",
        "n_roles": len(role_names),
        "role_names": role_names,
        "shortest_name": {
            "n_chars": len(shortest_name),
            "role_name": shortest_name
        },
        "longest_name": {
            "n_chars": len(longest_name),
            "role_name": longest_name
        }
    }

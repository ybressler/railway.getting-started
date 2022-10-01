"""
Entry point for this application

References:
    1. Artists Who Code [Superblocks App](https://app.superblocks.com/applications/9e80434c-64a6-480f-bac3-0093f0139dbf/pages/ecb00eea-214d-4877-8c62-f88f999b5f94)
"""
import os
from functools import lru_cache
from fastapi import FastAPI

import config  # Loads env variables
from db import base, query_mongo


app = FastAPI()


@app.get("/")
def hello():
    secret_value = os.environ.get('SECRET_VALUE', 'not set')
    return f"Hello from Railway. {secret_value=}"


@app.get("/data/summary")
def superblocks_db_summary():
    """
    Returns a summary of the superblocks database.
    The one being used in the Artists Who Code thingy.[1]
    """

    return query_mongo.get_tech_roles()

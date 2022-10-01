"""
Entry point for this application

References:
    1. Artists Who Code [Superblocks App](https://app.superblocks.com/applications/9e80434c-64a6-480f-bac3-0093f0139dbf/pages/ecb00eea-214d-4877-8c62-f88f999b5f94)
"""
import os
from fastapi import FastAPI, Query

import config  # Loads env variables
from db import base, query_mongo


app = FastAPI()


@app.get("/")
def hello() -> str:
    """Entry point to the API"""
    secret_value = os.environ.get('SECRET_VALUE', 'not set')
    return f"Hello from Railway. {secret_value=}"

@app.get("/fun")
def hello_fun(
        name: str = "Mr. Pickles",
        loud: bool = True,
        n_echo: int = Query(
            default=10,
            ge=1,
            le=100,
            description="Choose how many times you want your name repeated!"
            )
        ) -> str:
    """
    A fun way to say hello
    """

    greeting = f'Hello {name}'

    # Limit to 5 exclamation points
    n_ex = 5

    if loud:
        greeting = greeting.upper() + '!' * (n_ex)

    result = [greeting for i in range(n_echo)]

    if loud:
        return ' '.join(result)
    else:
        return ', '.join(result)


@app.get("/data/summary")
def superblocks_db_summary() -> dict:
    """
    Returns a summary of the superblocks database.
    The one being used in the Artists Who Code thingy.[1]
    """

    return query_mongo.get_tech_roles()

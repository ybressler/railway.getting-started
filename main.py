import os
from fastapi import FastAPI


from db import base, query_mongo


app = FastAPI()

@app.get("/")
def hello():
    foo = os.environ.get('FOO')
    return f"Hello from my Deta Micro. {foo=}"


@app.get("/superblocks/db-summary")
def superblocks_db_summary():
    """
    Returns a summary of the superblocks database. (The one
    being used in the Artists Who Code thingy.)
    """

    return query_mongo.get_tech_roles()

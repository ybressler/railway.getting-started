# Getting Started with Railway

Super simple way to deploy code to [Railway](https://railway.app/)

# Getting started
### 1. Create a virtual environment and install requirements
```bash
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

### 2. Load/Store Secrets
1. Create a `.env` file with the following values:

  i. Fun stuff
```bash
SECRET_VALUE=pickles
```
ii. Enable [Mongo Atlas Data API](https://www.mongodb.com/docs/atlas/api/data-api/).
This is optional, it does some cool stuff in `db/query_mongo.py`
```bash
DATA_API_BASE_URL="https://data.mongodb-api.com/app/data-oyuuc/endpoint/data/v1/action"
ATLAS_DATA_API_KEY="MY_SECRET_API_KEY"
```

2. Now add load secrets to your environment by running:
```bash
source .env
```

### 3. Run locally
Test locally with the following
```
uvicorn main:app --reload --port 8000
```

### 4. You're all done! 🎉

---

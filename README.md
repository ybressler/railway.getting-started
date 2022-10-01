# Getting Started with Railway

Super simple way to deploy code to [Railway](https://railway.app/)

View this deployed API here: https://railwaygetting-started-production.up.railway.app/docs

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

# Deploying to Railway
You can do this easily from their UI. Or you can do it from the CLI.
I will be doing it from the CLI.

> Unfortunately, Railway's CLI is still a work in progress and there are several
gaps here. Notwithstanding, here's how you'll go about doing things.



1. Install Railway CLI
```bash
brew install railway
```

2. Login to railway
```bash
railway login
```
3. Initialize your project
* Choose a blank project (template)
* Choose a nifty name
* Say `yes` to loading in your `.env`
```bash
railway init
```

4. Build your app
```
railway up --detach
```
Your app will not work yet. You'll need to do the following
manual steps in the browser.

5. Open your railway app in the browser:
```
railway open
```
6. Navigate to your project's settings. Under `Deploy` section,
update the `Start Command` to the following:
```
uvicorn main:app --host 0.0.0.0 --port $PORT
```
7. Within your project's settings, under `Environment`, under `Domains`
select `⚡️ Generate Domain`. This will autogenerate a domain
for your app. Give it a minute.

8. Try visiting your app's endpoint. If it works, you are done.
If it doesn't work, check the logs and debug.

9. Bonus, configure railway to create deployments only when relevant files
are changed. Settings, under `Build` >> `Watch Paths` update to the following:
```
# Ignore all Markdown files
**
!/*.md
```

## Connect your app to a github repo for continous deployment
This is a nice feature.
1. Navigate to your project's settings, under `General` section,
under `Service Source` click `Connect Repo`. The rest should be pretty
self explanatory.

----

Have fun building!

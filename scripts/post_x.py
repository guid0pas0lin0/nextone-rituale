import os, json, tweepy, random
api = tweepy.Client(bearer_token=os.environ["X_BEARER"],
                    consumer_key=os.environ["X_KEY"],
                    consumer_secret=os.environ["X_SECRET"],
                    access_token=os.environ["X_AT"],
                    access_token_secret=os.environ["X_ATS"])
conf = json.load(open("data/confessions.json"))
c = random.choice(conf[-20:])
txt = f'Confessione #{c["id"]}: {c["text"][:220]} • Entra nel cerchio → https://tuodominio'
api.create_tweet(text=txt)

import tweepy
from constants import *
import fire
import pandas as pd
from urllib.parse import urlparse


def twitter(file):
    auth = tweepy.OAuth1UserHandler(
        consumer_key=CONSUMER_KEY,
        consumer_secret=CONSUMER_SECRET,
        access_token=ACCESS_TOKEN,
        access_token_secret=ACCESS_TOKEN_SECRET
    )

    api = tweepy.API(auth, wait_on_rate_limit=True)

    df = pd.read_excel(file, engine='openpyxl')

    for row in range(len(df)):

        msg = ""
        for col in range(len(df.iloc[0])):
            content = df.iloc[row, col]
            if col == 0:
                if pd.isnull(content):
                    return
                name = urlparse(content).path[1:]
                print(name)
                user = api.get_user(screen_name=name)
            elif content == 0:
                try:
                    api.send_direct_message(int(user.id_str), msg)
                    msg = ""
                except:
                    print('could not send message')
            elif pd.isnull(content):
                msg += " "
            else:
                msg += content


if __name__ == '__main__':
    fire.Fire()

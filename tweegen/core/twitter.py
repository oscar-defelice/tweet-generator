import fire
import tweepy
from tqdm import tqdm
from pathlib import Path

from tweegen.log import log
from tweegen import config as cfg


@log("Connect to the API")
def _connect():
    auth = tweepy.OAuthHandler(cfg.CONSUMER_KEY, cfg.CONSUMER_SECRET)
    auth.set_access_token(cfg.ACCESS_TOKEN, cfg.ACCESS_TOKEN_SECRET)
    Path(cfg.DATA_DIR).mkdir(exist_ok=True)
    return tweepy.API(auth)


def _clean(txt):
    return " ".join(
        [
            w if not w.endswith("...") else w[:-3]
            for w in txt.split()
            if not w.startswith("http") and not w.startswith("@")
        ]
    )


@log("Download tweets")
def _download_tweets(api, name):
    path = Path(cfg.DATA_DIR) / name
    path.mkdir(exist_ok=True)
    user = api.get_user(name)
    for tweet in tqdm(
        tweepy.Cursor(
            api.user_timeline,
            screen_name=name,
            tweet_mode="extended",
            include_rts=False,
            wait_on_rate_limit=True,
        ).items(),
        total=user.statuses_count,
    ):
        if tweet:
            with open(path / "tweets.txt", "a") as f:
                f.write(_clean(tweet.full_text) + cfg.SEP_WORD)


def download(name="BernieSanders"):
    api = _connect()
    _download_tweets(api, name)


if __name__ == "__main__":
    fire.Fire()

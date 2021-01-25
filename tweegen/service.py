import tweepy
import random
from transformers import pipeline

import tweegen.config as cfg
from tweegen.log import log



@log("Model loading")
def _load_model():
    return pipeline('text-generation',
                    model = cfg.MODEL_DIR,
                    tokenizer = 'gpt2',
                    config = {'max_length': 280})


def _split(text):
    return text.split(cfg.SEP_WORD)

def _generate():
    model = _load_model()
    tweet_lines = model(cfg.INPUT_TEXT,
                    num_return_sequences = cfg.RETURN_SEQUENCES)

    tweets = []
    for tweet_dict in tweet_lines:
        tweets.append(tweet_dict['generated_text'])

    return tweets


@log("Tweets generating")
def generate():
    return _generate()


@log("Tweets uploading")
def upload(tweets):
    auth = tweepy.OAuthHandler(cfg.CONSUMER_KEY, cfg.CONSUMER_SECRET)
    auth.set_access_token(cfg.ACCESS_TOKEN, cfg.ACCESS_TOKEN_SECRET)
    api = tweepy.API(auth)
    api.update_status(random.choice(tweets))

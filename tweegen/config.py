import os

PROJECT_NAME = "tweegen"
VERSION = "0.1"
PORT = int(os.getenv("PORT"))
LOG_LEVEL = os.getenv("LOG_LEVEL")

DATA_DIR = "data"
DATA = "data/tweets.txt"
SEP_WORD = "<|endoftext|>"

CONSUMER_KEY = os.getenv("CONSUMER_KEY")
CONSUMER_SECRET = os.getenv("CONSUMER_SECRET")
ACCESS_TOKEN = os.getenv("ACCESS_TOKEN")
ACCESS_TOKEN_SECRET = os.getenv("ACCESS_TOKEN_SECRET")

PRETRAINED_MODEL = os.getenv("PRETRAINED_MODEL", "gpt2")
MODEL_DIR = "models/gpt2-tweetgen"
STEPS = int(os.getenv("STEPS", 500))
BATCH_SIZE = int(os.getenv("BATCH_SIZE", 8))
EPOCHS = float(os.getenv("EPOCHS", 3))
TEMPERATURE = float(os.getenv("TEMPERATURE", 0.8))
INPUT_TEXT = os.getenv("INPUT_TEXT", "")
RETURN_SEQUENCES = int(os.getenv("RETURN_SEQUENCES", 25))

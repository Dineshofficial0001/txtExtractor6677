import os

class Config(object):
    BOT_TOKEN = os.environ.get("BOT_TOKEN", "7213487523:AAFm5fsOfp_kvmrLFZFLRFCCWs1LLHjiE88")
    API_ID = int(os.environ.get("API_ID", "23006024"))
    API_HASH = os.environ.get("API_HASH", "19fd942576cb0075faebf9eb5ceb31db")
    AUTH_USERS = os.environ.get("AUTH_USERS", "7611091609") 

import os

class Config(object):
     
    BOT_TOKEN = os.environ.get("BOT_TOKEN", "7257283749:AAGucFXFNpw0l27vbAK8UklfVHKuaf440Zo")
    API_ID = int(os.environ.get("API_ID","28885508" ))
    API_HASH = os.environ.get("API_HASH", "890e501add0327b997000bad81b10f43")
    #Add your channel id. For force Subscribe.
    CHANNEL = os.environ.get("CHANNEL", "")
    #Skip or add your proxy from https://github.com/rg3/youtube-dl/issues/1091#issuecomment-230163061
    HTTP_PROXY = ''

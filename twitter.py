from twitter import OAuth, Twitter
from datetime import datetime, time
import pytz, random

TOKEN = "SECRET"
TOKEN_KEY = "SECRET"
API_KEY = "SECRET"
API_SECRET = "SECRET"

MY_TZ = pytz.timezone('Europe/Stockholm')
now = datetime.now(MY_TZ).time()
retries = 0
def get_current_hour(timestamp):
    if timestamp.hour == 0 or timestamp.hour == 12:
        return 12
    return timestamp.hour % 12

def compose_tweet(timestamp):
    number_of_rings = get_current_hour(timestamp)
    # Creates a tweet, e.g. "BONG BONG BONG #03:00
    alert_sound = get_bell_sound(retries)
    tweet = " ".join([alert_sound] * number_of_rings)
    hashtag = "#%s:%s" %(str(timestamp.hour).zfill(2), str(timestamp.minute).zfill(2))
    return "%s %s" %(tweet, hashtag)

def send_tweet(tweet):
    global retries
    auth = OAuth(TOKEN, TOKEN_KEY, API_KEY, API_SECRET)
    t = Twitter(auth=auth)
    try:
        t.statuses.update(status=tweet)
        retries = 0
    except:
        retries += 1
        if retries <= 7:
            main()
        else:
            raise

def get_bell_sound(index):
    sounds = ('BONG', 'DONG', 'DING', 'BING-BONG', 'RING', 'PING', 'JINGLE', 'DING-DONG')
    #rand_item = random.choice(sounds)
    return sounds[index]

def main(timestamp = now):
    send_tweet(compose_tweet(timestamp))

if __name__ == "__main__":
    main()

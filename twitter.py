from twitter import OAuth, Twitter
from datetime import datetime, time
import pytz

TOKEN = "SECRET"
TOKEN_KEY = "SECRET"
API_KEY = "SECRET"
API_SECRET = "SECRET"

MY_TZ = pytz.timezone('Europe/Stockholm')
now = datetime.now(MY_TZ).time()
def get_current_hour(timestamp):
    return timestamp.hour % 12

def compose_tweet(timestamp):
    number_of_rings = get_current_hour(timestamp)
    # Creates a tweet, e.g. "BONG BONG BONG #03:00
    alert_sound = "BONG"
    tweet = " ".join([alert_sound] * number_of_rings)
    hashtag = "#%s:%s" %(str(timestamp.hour).zfill(2), str(timestamp.minute).zfill(2))
    return "%s %s" %(tweet, hashtag)

def send_tweet(tweet):
    auth = OAuth(TOKEN, TOKEN_KEY, API_KEY, API_SECRET)
    t = Twitter(auth=auth)
    t.statuses.update(status=tweet)

def main(timestamp = now):
    time.sleep(15)
    send_tweet(compose_tweet(timestamp))

if __name__ == "__main__":
    main()

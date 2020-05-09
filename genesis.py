import tweepy
import time
import feedparser

# Auth to Twitter
auth = tweepy.OAuthHandler("XXXXXXXXXXXXXXXXXXXXXXXXX", "XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX")
auth.set_access_token("XXXXXXXXXXXXXXXXXX-XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX", "XXXXXXXXXXXXXXXXXXXXXXXXXXXXXX")

tweepy = tweepy.API(auth)

# Verify credentials
try:
    tweepy.verify_credentials()
    print("Authentication OK")
except:
    print("Error during authentication")


# Source of information
source = "https://securityaffairs.co/wordpress/feed"
# Time in seconds (24 hours)
time_sec = 86400


def update_status():
    """ Get data from source """

    data = feedparser.parse(source)

    title = data.entries[0].title
    link = data.entries[0].link

    tweet = (title + " - " + link)
    tweepy.update_status(tweet)

    print("[#] Tweet sent: {}".format(tweet))

while True:
    update_status()
    time.sleep(time_sec)

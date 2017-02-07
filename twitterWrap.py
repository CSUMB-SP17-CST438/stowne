# twitterApi

# this file authorizes the app to use twitters API using tweepy,
# and defines the function pickTweet(searchPhrase) which uses
# tweepy's search method to find tweets relevent to the search
# phrase. PickTweet(searchPhrase) also uses the global list
# 'recentScreenNames' to ensure that no author is quoted twice in
# ten page loads.
#
# pickTweets(searchPhrase) returns a tweepy tweet object, and the
# list of recently used screen names in a dictionary.



import tweepy
import random
import os



# Base URL for linking to tweets
# the tweet id is appended to obtain the attribution link
twitterComStatuses = "https://twitter.com/statuses/"

# Twitter limits tweets returned per search.
twitterMaxPerPage = 100

# keep track of screen names of authors of recently used tweets
# used somewhat like a queue.
recentScreenNames = []


consumer_key        = os.getenv("TWITTER_CONSUMER_KEY")
consumer_key_secret = os.getenv("TWITTER_CONSUMER_KEY_SECRET")
access_token        = os.getenv("TWITTER_ACCESS_TOKEN")
access_token_secret = os.getenv("TWITTER_ACCESS_TOKEN_SECRET")

# tweepy authorization object.
authorization = tweepy.OAuthHandler(
    consumer_key,
    consumer_key_secret
)

# set up access token and access token secret.
authorization.set_access_token(
    access_token,
    access_token_secret
)

# tweepy API object talks to twitter for me.
twitterApi = tweepy.API(
    authorization
)

# Picks the next tweet to use using twitter search API through tweepy.
# Also makes sure that the same author isn't used twice in ten page loads.
def pickTweet(searchPhrase):
    
    # loop until new screen name is found and tweet returned.
    while True:
        
        # get next tweet object from tweepy.
        nextTweet = twitterApi.search(
            q=searchPhrase, 
            count=twitterMaxPerPage,
            lang='en'
        )[random.randint(0, twitterMaxPerPage-1)]
        
        # if screen name is already in the list, start over.
        if nextTweet.user.screen_name in recentScreenNames:
            continue
        
        # if screen name not in list, add to queue, drop least recently used.
        elif len(recentScreenNames) == 10:
            for i in range(0, len(recentScreenNames)-1):
                recentScreenNames[i] = recentScreenNames[i+1]
            recentScreenNames[9] = nextTweet.user.screen_name
            
        # if queue not full, simply add screen name to it.
        else:
            recentScreenNames.append(nextTweet.user.screen_name)
        
        # at this point the tweet is from a user who hasn't been quoted
        # for at least ten page loads. 
        return nextTweet
               
   
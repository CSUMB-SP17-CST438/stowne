import requests_oauthlib
import requests
import json
import random

class TwitterApi:
    def __init__(self, consumer_key, consumer_secret, access_token, access_token_secret):
        self.search_API_URL = 'https://api.twitter.com/1.1/search/tweets.json?'
        self.authorization = requests_oauthlib.OAuth1(
            consumer_key,
            consumer_secret,
            access_token,
            access_token_secret
        )
        
    # for private use
    def requestGet(self, url):
        response = requests.get(url, auth=self.authorization)
        return response.json()
        
    # for private use
    def prepareSearch_API_URL(self, searchPhrase):
        return self.search_API_URL + "q=" + searchPhrase
        
    # for public use
    def search(self, searchPhrase):
        url = self.prepareSearch_API_URL(searchPhrase)
        return self.requestGet(url)
        
    def test(self, searchPhrase):
        searchResults = self.search(searchPhrase)
        print(json.dumps(searchResults["statuses"][0], indent = 5))
        
    def randomTweetAbout(self, searchPhrase):
        searchResults = self.search(searchPhrase)
        statuseCount = len(searchResults["statuses"])
        randomIndex = random.randint(0, statuseCount-1)
        tweetText = searchResults["statuses"][randomIndex]["text"]
        author = searchResults["statuses"][randomIndex]["user"]["screen_name"]
        return {
            "text" : tweetText,
            "screen_name" : author
        }
            
        
        
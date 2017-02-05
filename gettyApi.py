import requests
import json
import random

  

    
    
class GettyApi:
    def __init__(self, apiKey):
        # I don't like long lines
        self.search_API_URL = 'https://api.gettyimages.com/'
        self.search_API_URL += 'v3/search/images?fields=id,'
        self.search_API_URL += 'title,thumb,referral_destin'
        self.search_API_URL += 'ations&sort_order=best'
        self.headers = {
            "Api-Key":apiKey
        }
        
    def prepareSearch_API_URL(self, searchPhrase):
        return self.search_API_URL + "&phrase=" + searchPhrase
        
    def requestGet(self, url):
        response = requests.get(url, headers = self.headers)
        return response.json()
        
    def search(self, searchPhrase):
        url = self.prepareSearch_API_URL(searchPhrase)
        return self.requestGet(url)
        
    def randomPictureURLAbout(self, searchPhrase):
        searchResults = self.search(searchPhrase)
        imageCount = len(searchResults["images"])
        randomIndex = random.randint(0, imageCount-1)
        return searchResults["images"][randomIndex]["display_sizes"][0]["uri"]
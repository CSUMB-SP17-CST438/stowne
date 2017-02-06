import requests
import json
import random

  

    
    
class GettyApi:
    def __init__(self, apiKey):
        self.maxResultCount = 4769
        self.maxResultsPerPage = 100
        self.maxPageNumber = self.maxResultCount/self.maxResultsPerPage
        # I don't like long lines
        self.search_API_URL = 'https://api.gettyimages.com/'
        self.search_API_URL += 'v3/search/images?'
        self.headers = {
            "Api-Key":apiKey
        }
        
    def prepareSearch_API_URL(self, searchPhrase, pageNumber=1, pageSize=100, numberOfPeople='none'):
        readyURL = self.search_API_URL
        readyURL += "number_of_people="+str(numberOfPeople)
        readyURL += "&page=" + str(pageNumber)
        readyURL += "&page_size=" + str(pageSize)
        readyURL += "&phrase=" + str(searchPhrase)
        print("\n\n"+readyURL+"\n\n")
        return readyURL
        
    def requestGet(self, url):
        response = requests.get(url, headers = self.headers)
        return response.json()
        
    def search(self, searchPhrase, pageNumber=1, pageSize=100):
        url = self.prepareSearch_API_URL(searchPhrase, pageNumber, pageSize)
        return self.requestGet(url)
        
    def randomPictureURLAbout(self, searchPhrase):
        RandomPageNumber = random.randint(1, self.maxPageNumber)
        searchResults = self.search(searchPhrase, RandomPageNumber)
        imageCount = len(searchResults["images"])
        randomIndex = random.randint(0, imageCount-1)
        return searchResults["images"][randomIndex]["display_sizes"][0]["uri"]
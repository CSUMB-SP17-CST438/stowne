# gettyWrap.py

import requests
import json
import random
import os

  

apiKey = os.getenv("GETTY_API_KEY")

gettyRequestHeaders = {
    "Api-Key":apiKey
}

# I needed a way of easily manipulating the search url.
class GettySearchURL:
    
    def __init__(self, **searchParameters):
        self.baseURL = 'https://api.gettyimages.com/v3/search/images?'
        self.searchParameters = {}
        self.setSearchParameters(**searchParameters)
    
    # For tweeking the search parameters. All matching keys are
    # updated, non-matching keys are added to self.searchParameters,
    # and keys not specified in the argument are unchanged.
    def setSearchParameters(self, **searchParameters):
        for parameter in searchParameters:
            self.searchParameters[parameter] = searchParameters[parameter]
        
    # concatonates all the search parameters with getty specific syntax.
    def getUrl(self):
        
        urlAppendage = ""
        for parameter in self.searchParameters:
            if self.searchParameters[parameter]:
                if len(str(self.searchParameters[parameter])) >= 0:
                    urlAppendage += parameter + "=" + str(self.searchParameters[parameter]) + "&"
                    
        return self.baseURL + urlAppendage[0:len(urlAppendage)-1]
        
    # clones this instance in such a way that altering the clone will not alter this instance.
    def copy(self):
        new = GettySearchURL()
        for parameter in self.searchParameters:
            new.searchParameters[parameter] = self.searchParameters[parameter]
        return new
    
# Does a test request and inspects the meta data to see how
# many pages are available with this url.
def calculateMaxPageNumber(gettySearchURL):
    
    # for this gettySearchURL object as it is, the max page size is
    # given by results/pageSize
    copyUrl = gettySearchURL.copy()
    copyUrl.setSearchParameters(page=1)
    response = requests.get(copyUrl.getUrl(), headers = gettyRequestHeaders)
    try: return int(int(response.json()["result_count"]) / int(copyUrl.searchParameters["page_size"]))
    except: return 0
    
    
# Tweeks some search parameters to match my theme, 
# makes the get request to getty with a random page number
# and returns the image uri.
def pickImage(searchPhrase):
    
    # uses page size of one because when page size is one,
    # results_count and page count are the same. Makes it easy.
    url = GettySearchURL(
        number_of_people = "none",
        orientations     = "Vertical",
        page             = 1,
        page_size        = 1,
        phrase           = searchPhrase,
        sort_order       = "most_popular"
    )
    
    maxPageNumber = calculateMaxPageNumber(url)
    randomPageNumber = random.randint(0, maxPageNumber)
    url.setSearchParameters(page=randomPageNumber)
    
    print("\n\n"+url.getUrl()+"\n\n")
    
    response = requests.get(url.getUrl(), headers = gettyRequestHeaders)
    
    # try again if failure
    try: return response.json()["images"][0]["display_sizes"][0]["uri"]
    except KeyError: return pickImage(searchPhrase)
    

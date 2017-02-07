# gettyWrap.py

import requests
import json
import random

  
"""
apiKey = os.getenv("API_KEY")
"""

apiKey = "hj2v7u3jn846ejpkhup5kjzy"
apiGettyimagesComV3SearchImages = 'https://api.gettyimages.com/v3/search/images'

gettyRequestHeaders = {
    "Api-Key":apiKey
}

# getty restricts the results per page to 100 :/
gettyMaxPerPage = 100

# This is the highest page number allowed for a page size of 100.
# Page number is determined by how many search hits there were and
# the resultsPerPage parameter. 
gettyMaxPageNumber = 45

def buildURL(
    searchPhrase,
    sortOrder = "most_popular",
    pageNumber=1,
    pageSize=gettyMaxPerPage,
    numberOfPeople="none",
    orientations="Vertical"
):
    readyURL = apiGettyimagesComV3SearchImages
    readyURL += "?phrase=" + str(searchPhrase)
    readyURL += "&page=" + str(pageNumber)
    readyURL += "&page_size=" + str(pageSize)
    readyURL += "&orientations=" + str(orientations)
    readyURL += "&number_of_people=" + str(numberOfPeople)
    readyURL += "&sort_order=" + str(sortOrder)
    return readyURL
    
def pickImage(searchPhrase):
    randomPageNumber = random.randint(0, gettyMaxPageNumber)
    url = buildURL(searchPhrase, pageNumber = randomPageNumber)
    searchResults = requests.get(url, headers = gettyRequestHeaders)
    jsonBody = searchResults.json()
    imageCount = len(jsonBody["images"])
    randomImageIndex = random.randint(0, imageCount-1)
    return jsonBody["images"][randomImageIndex]["display_sizes"][0]["uri"]
    
    
    

    
    

 # https://api.gettyimages.com:443/v3/search/images?number_of_people=none&orientations=Vertical&page=100&page_size=100&phrase=mountain&sort_order=most_popular
 # api.gettyimages.com/v3/search/images?phrase=mountain&page=1&page_size=100&orientations=Vertical&number_of_people=none&sort_order=most_popular
import requests
import json
import random


apiKey = "8c4qkbna6f4qhzhrtvkghxa2"
secret = "SVfMs3NTrgnKDaZtW68EefNhJa3DNbDSHFNhtUcy3fMk7"

# I don't like long lines
url = 'https://api.gettyimages.com/'
url += 'v3/search/images?fields=id,'
url += 'title,thumb,referral_destin'
url += 'ations&sort_order=best'

headers = {
    "Api-Key":apiKey
}

    
# adds search phrase to url
def appendSearchPhrase(searchPhrase):
    return url + "&phrase=" + searchPhrase

# selects an image at random from the ["image"] array
# from between the indecis 0 and len(["image"])-1
def chooseImageUri(json_body):
    imageIndex = random.randint(0, len(json_body["images"]))
    
    return json_body["images"][imageIndex]["display_sizes"][0]["uri"]

# for use outside this file, give a search term,
# get an image uri
def getImageUri(searchPhrase):
    requestingFrom = appendSearchPhrase(searchPhrase)
    response = requests.get(requestingFrom, headers = headers)
    return chooseImageUri(response.json())
    
    
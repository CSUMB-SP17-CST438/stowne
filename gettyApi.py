import requests
import json


ApiKey = "8c4qkbna6f4qhzhrtvkghxa2"
Secret = "SVfMs3NTrgnKDaZtW68EefNhJa3DNbDSHFNhtUcy3fMk7"
url = 'https://api.gettyimages.com/v3/search/images?fields=id,title,thumb,referral_destinations&sort_order=best&phrase=cats'

headers = {
    "Api-Key":"8c4qkbna6f4qhzhrtvkghxa2"
}

url = 'https://api.gettyimages.com/v3/search/images?fields=id,title,thumb,referral_destinations&sort_order=best'
def appendSearchTermToUrl(searchTerm):
    return url + "&phrase=" + searchTerm

def getJson(searchTerm):
    newUrl = appendSearchTermToUrl(searchTerm)
    response = requests.get(newUrl, headers = headers)
    json_body = response.json()
    return json_body
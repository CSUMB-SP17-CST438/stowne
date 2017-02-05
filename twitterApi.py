import requests_oauthlib
import requests
import json

url = 'https://dev.twitter.com/rest/public/search'

oauth = requests_oauthlib.OAuth1(
 "<API_KEY>",
 "<API_SECRET>",
 "<ACCESS_TOKEN>",
 "<ACCESS_TOKEN_SECRET>"
)

response = requests.get(url, auth=oauth)
json_body = response.json()
print json.dumps(json_body, indent=2)
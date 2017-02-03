import flask
import requests
import os
import gettyApi


app = flask.Flask(__name__)


@app.route('/')
def index():
    json_body = gettyApi.getJson("dogs")
    return json_body["images"][0]["display_sizes"][0]["uri"]
    

app.run(
   port=int(os.getenv('PORT', 8080)),
   host=os.getenv('IP', '0.0.0.0')
)
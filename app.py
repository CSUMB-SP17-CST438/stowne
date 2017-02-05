import flask
import requests
import os
import gettyApi


app = flask.Flask(__name__)


@app.route('/')
def index():
    tweet = "this is another tweet"
    uri = gettyApi.getImageUri("cat")
    return flask.render_template(
        'imageAndTweet.html',
        imageUri = uri,
        tweet = tweet
    )
    

app.run(
   port=int(os.getenv('PORT', 8080)),
   host=os.getenv('IP', '0.0.0.0'),
   debug=True
)
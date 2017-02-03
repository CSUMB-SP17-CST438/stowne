import flask
import requests
import os


app = flask.Flask(__name__)


@app.route('/')
def index():
    return "hello world"
    

app.run(
   port=int(os.getenv('PORT', 8080)),
   host=os.getenv('IP', '0.0.0.0')
)
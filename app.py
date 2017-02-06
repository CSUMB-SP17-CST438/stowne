import flask
import requests
import os
import gettyApi
import twitterApi
import json

# don't forget to turn these into environment variables in your heroku environment
t_consumer_key = 'KPWCE4qO3TKU2fIKYeacuZKAZ'
t_consumer_secret = '7HIgkgBGPrSxy44j8E8DGRNBQE6A119XwVIF2HslPJaDAnEzwt'
t_access_token = '827358906426892288-lfA3YmDL7hamYcCN27Caui3HticmoPc'
t_access_token_secret = 'EgtoCilWxy8OVVS5qfokqEW1pLVlXrnnQ3tQkbRqXKZ6D'
g_apiKey = "8c4qkbna6f4qhzhrtvkghxa2"
g_secret = "SVfMs3NTrgnKDaZtW68EefNhJa3DNbDSHFNhtUcy3fMk7"
###################################################################################
  


app = flask.Flask(
    __name__
)

twitter_api = twitterApi.TwitterApi(
    t_consumer_key,
    t_consumer_secret,
    t_access_token,
    t_access_token_secret
)

getty_api = gettyApi.GettyApi(
    g_apiKey    
)




@app.route('/')
def index():
    
    nextTweet = twitter_api.randomTweetAbout("earth porn")
    nextImage = getty_api.randomPictureURLAbout("earth porn")
    
    return flask.render_template(
        "imageAndTweet.html",
        imageUri = nextImage,
        tweet = nextTweet["text"],
        screen_name = nextTweet["screen_name"]
    )
    

app.run(
   port=int(os.getenv('PORT', 8080)),
   host=os.getenv('IP', '0.0.0.0'),
   debug=True
)

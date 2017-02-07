# app.py

# app.y defines what to do when a request to see the index '/' page comes in.

import os
import flask
import random
import gettyWrap
import twitterWrap



# Globals for theme selection
twitterSearchPhrases = [
    "motherearth",
    "protect environment",
    "clean energy"
]
gettyImSearchPhrases = [
    "mountain",
    "ocean",
    "sunset"
]

# flask object that does some sort of magic
superBitchenWebApp = flask.Flask(
    __name__
)

@superBitchenWebApp.route('/')
def index():
    
    nextTwitterSearchPhraseIndex = random.randint(0, len(twitterSearchPhrases)-1)
    nextGettyImSearchPhraseIndex = random.randint(0, len(gettyImSearchPhrases)-1)
    nextTweet = twitterWrap.pickTweet(twitterSearchPhrases[nextTwitterSearchPhraseIndex])
    nextImage = gettyWrap.pickImage(gettyImSearchPhrases[nextGettyImSearchPhraseIndex])
    
    return flask.render_template(
        "imageAndTweet.html",
        imageUri = nextImage,
        tweet = nextTweet.text,
        screen_name = nextTweet.user.screen_name,
        attributionLink = twitterWrap.twitterComStatuses+nextTweet.id_str,
        screen_name_debug_list = " || ".join(reversed(twitterWrap.recentScreenNames))
    )

    

superBitchenWebApp.run(
   port=int(os.getenv('PORT', 8080)),
   host=os.getenv('IP', '0.0.0.0'),
   debug=True
)

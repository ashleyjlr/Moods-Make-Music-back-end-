import os
from flask import Flask, request
from airium_generator import generate_page

import random

app = Flask(__name__)


@app.route('/', methods=['POST'])
def home():
    if request.method == 'POST':
        mood = str(request.form['mood'])

        return str(if_i_feel_then(mood.lower()))

mylist = []

mydict_happy = {}
mydict_happy["Girls Just Wanna Have Fun by Cyndi Lauper"] = "https://www.youtube.com/watch?v=apGh9uDfSTY"
mydict_happy["Cool by Gwen Stefani"] = "https://www.youtube.com/watch?v=apGh9uDfSTY"
mydict_happy["Dynamite by BTS"] = " https://www.youtube.com/watch?v=NvK9APEhcdk"
mydict_happy["Dance Baby by Boy Pablo"] = "https://www.youtube.com/watch?v=sC0IWVEq4o0" 
mydict_happy["Best Song Ever by One Direction"] = "https://www.youtube.com/watch?v=-zCF1-emakY" 

mydict_sad = {}
mydict_sad["All Too Well by Taylor Swift"] = " https://www.youtube.com/watch?v=F8Jxo15Vfic" 
mydict_sad["Talking to The Moon by Bruno Mars"] = "https://www.youtube.com/watch?v=CsKpw6ppj5I"
mydict_sad["1999 by Beabadoobee"] = "https://www.youtube.com/watch?v=951Dm0vS6Wk"
mydict_sad["Bubblegum by Clairo"] = "https://www.youtube.com/watch?v=4ptgVKcTYsE"
mydict_sad["instagram by DEAN"] = "https://www.youtube.com/watch?v=lq3NLUN8DDc"

mydict_mad = {}
mydict_mad["Potential Break Up Song by Aly and Aj"] = "https://youtu.be/GN_58vHQKh4"
mydict_mad["7 Things I Hate About You by Miley Cyrus"] = "https://youtu.be/Hr0Wv5DJhuk"
mydict_mad["Maniac by Conan Gray"] = "https://youtu.be/-E-_IRJU5w0"
mydict_mad["Dead to Me by Kali Uchis"] = "https://youtu.be/OcUDK4kAUIw"
mydict_mad["Ain't it Fun by Paramore"] = "https://youtu.be/2IA7QExh-NQ"

mydict_tired = {}
mydict_tired["Dreamy Night by Lily Pichu"] = " https://youtu.be/DXuNJ267Vss"
mydict_tired["pov by Ariana Grande"] = "https://youtu.be/nQJEp-k-ogs"
mydict_tired["Why by Dominic Fike"] = " https://youtu.be/5mILqcNQ5hE"
mydict_tired["Ivy by Frank Ocean"] = "https://youtu.be/AE005nZeF-A"
mydict_tired["She's a Baby by ZICO"] = "https://youtu.be/ohSpvSGXfhY "


m_happy = [
    "Girls Just Wanna Have Fun by Cyndi Lauper", "Cool by Gwen Stefani",
    "Dynamite by BTS", "Dance Baby by Boy Pablo",
    "Best Song Ever by One Direction"
]
m_sad = [
    "All Too Well by Taylor Swift", "Talking to The Moon by Bruno Mars",
    "1999 by Beabadoobee", "Bubblegum by Clairo", "instagram by DEAN"
]
m_mad = [
    "Potential Break Up Song by Aly and Aj",
    "7 Things I Hate About You by Miley Cyrus", "Maniac by Conan Gray",
    "Dead to Me by Kali Uchis", "Ain't it Fun by Paramore"
]
m_tired = [
    "Dreamy Night by Lily Pichu", "pov by Ariana Grande",
    "Why by Dominic Fike", "Ivy by Frank Ocean", "She's a Baby by ZICO"
]


def if_i_feel_then(mood):
    if mood in ["happy", "excited", "cheery"]:
      [song, url] = random.choice(list(mydict_happy.items()))
      return generate_page("Since you're feeling " + mood +
                             ", you may want to listen to: " +
                             song + ". This is the url: ", url)
    if mood in ["sad", "upset", "unhappy"]:
      [song, url] = random.choice(list(mydict_sad.items()))
      return generate_page("Since you're feeling " + mood +
                             ", you may want to listen to: "  +
                             song + ". This is the url: ", url)
    if mood in ["angry", "mad", "frustrated"]:
      [song, url] = random.choice(list(mydict_mad.items()))
      return generate_page("Since you're feeling " + mood +
                             ", you may want to listen to: "  +
                             song + ". This is the url: ", url)
    if mood in ["tired", "sleepy", "exhausted"]:
      [song, url] = random.choice(list(mydict_tired.items()))
      return generate_page("Since you're feeling " + mood +
                             ", you may want to listen to: "  +
                             song + ". This is the url: ", url)
    return 'idk'


def run():
    print('starting flask...')
    app.secret_key = os.urandom(12)
    app.run(host='0.0.0.0', port=8080)


run()

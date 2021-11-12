import datetime
from flask import Flask, render_template, request
#from pymongo import MongoClient


app = Flask(__name__)
    #client = MongoClient("mongodb+srv://roxy:roxychen1996@cryptocurrency-recomman.mi0oh.mongodb.net/test")
    #app.db = client.recommendation

@app.route("/")
def home():  
    kwargs = {
        "coinjar_buy_bit": 128,
        "coinjar_sell_bit": 130,
        "paybis_buy_bit": 120,
        "paybis_sell_bit": 121,
        "coinjar_buy_eth": 128,
        "coinjar_sell_eth": 130,
        "paybis_buy_eth": 120,
        "paybis_sell_eth": 121,
    }
    return render_template("home.html",**kwargs)
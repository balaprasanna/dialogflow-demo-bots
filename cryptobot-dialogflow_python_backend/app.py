from flask import Flask, Response, request
import json

import requests

## UTIL Functions Begins :

def get(url):
    resp = requests.get(url)
    if resp.ok:
        return resp.json()

def construct_coin_dct():
    url = "https://api.coinmarketcap.com/v2/ticker/"
    data = get(url)
    coindct = {}

    for k,v in data["data"].items(): 
        coin_id = k
        coin_name = v["name"].lower()
        coindct [ coin_name ] = coin_id
    return coindct

def getprice(coinname, coindct):
    
    coinname = coinname.lower()
    coinid = coindct[coinname] #refering to global coindct

    url = f"https://api.coinmarketcap.com/v2/ticker/{coinid}"
    data = get(url)

    #parse the price info from the resp
    price = data["data"]["quotes"]["USD"]["price"]
    return "{:.2f}".format(price)

## UTIL Functions Ends :

app = Flask(__name__)

coin_dct = construct_coin_dct()

def getPriceIntentHandler(coinname):
    coinname = "".join( coinname.split() )
    price = getprice(coinname, coin_dct)
    return f"The price of {coinname} is {price}"

@app.route("/", methods = ["POST"])
def main():
    
    req = request.get_json(silent=True, force=True)
    print(req)
    intent_name = req["queryResult"]["intent"]["displayName"]

    if intent_name == "GetPriceIntent":
        coinname = req["queryResult"]["parameters"]["coinname"]
        resp_text = getPriceIntentHandler(coinname)
    else:
        resp_text = "Unable to find a matching intent. Try again."

    resp = {
        "fulfillmentText": resp_text
    }

    return Response(json.dumps(resp), status=200, content_type="application/json")

app.run(host='0.0.0.0', port=5000, debug=True)

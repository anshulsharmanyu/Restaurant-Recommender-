import getrecipe

from flask import Flask, request
from twilio.twiml.messaging_response import MessagingResponse, Message
from twilio.rest import Client
import urllib
import requests
from random import randint

# Account SID and Auth Token from www.twilio.com/console
client = Client('AC14dec95859e2f7bbfe87f47536d1e471', 'bb8cf2f2f568bc4d18f31894c293f33c')
app = Flask(__name__)

# A route to respond to SMS messages and kick off a phone call.
@app.route('/sms', methods=['GET', 'POST'])
def inbound_sms():
    response = MessagingResponse()
    food_item = urllib.quote(request.form['Body'])
    recipe = getrecipe.get_recipe(food_item)
    ingridients = ['\n']

    for i in range(len(recipe[3])):
        ingridients[0] += (recipe[3][i].encode("utf-8"))
        ingridients[0] += ("\n")

    response.message("\nName \n"+recipe[0].encode("utf-8") +"\n Recipe Link \n"
     + recipe[1].encode("utf-8")
     + "\n Calories - " 
     + str(recipe[2]).encode("utf-8") 
     + "\n"+ingridients[0])

    return str(response)

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)
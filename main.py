# Ako nemate flask onda:
# pip install -r requirements.txt --> naredba u terminalu
# pip3 install requests
import json
import requests
from flask import Flask, render_template

app = Flask(__name__)

@app.route("/", methods=["GET"])
def index():
    # pripremamo varijable

    url = "https://matchilling-chuck-norris-jokes-v1.p.rapidapi.com/jokes/random"

    headers = {
        'accept': "application/json",
        'x-rapidapi-key': "8efcb9dc50msh0340ec163bd6d95p165210jsnc4a89e5a6cb0",
        'x-rapidapi-host': "matchilling-chuck-norris-jokes-v1.p.rapidapi.com"
        }

    response = requests.request("GET", url, headers=headers)
    response2 = requests.request("GET", url, headers=headers)
    response3 = requests.request("GET", url, headers=headers)
    response4 = requests.request("GET", url, headers=headers)
    response5 = requests.request("GET", url, headers=headers)
    response6 = requests.request("GET", url, headers=headers)
    return render_template("index.html", response=response.json(), response2=response2.json(), response3=response3.json(), response4=response4.json(), response5=response5.json(), response6=response6.json())
 


if __name__ == "__main__":
    app.run()
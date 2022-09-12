import json
import requests
import datetime
from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/", methods= ["GET","POST"])
def wind():
    if request.method == "POST":
        city = request.form["city"]
        print(city)
        api = "72f64709e6048704e11459b58577961a"
        url = "http://api.openweathermap.org/data/2.5/weather?q="+city+"&appid="+api+"&units=metric"
        print(url)

        response = requests.get(url).json()
        print(response)

        if response["cod"] == 200:
            data = {"temp":response["main"]["temp"],
                    "name":response["name"],
                    "lon":response["coord"]["lon"],
                    "lat":response["coord"]["lat"],
                    "sunrise":datetime.datetime.fromtimestamp(response.get('sys')['sunrise']),
                    "status":200}
            return render_template("home.html",data=data)
        elif response["cod"] == "404":
            data= {"message":response["message"], "status":404}
            return render_template("home.html", data=data)
        else:
            data = None
            return render_template("home.html", data=data)
    else:
        data = None
        return render_template("home.html", data=data)

app.run()
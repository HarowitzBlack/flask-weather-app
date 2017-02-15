from flask import Flask,request
from flask import render_template
from Extractor import Wex


def GetWeatherData(searchquery):
    weather = Wex.WexWeather(searchquery,"396cbf110cc7bd1bd3087f317643a83f")
    data = weather.WexGetWeather()
    city = weather.GetCityNames()
    data += city
    print(data)
    return data

app = Flask(__name__)

@app.route('/')
def startup():
    weatherInfo = ['None']*5
    return render_template('startpage.html',data = weatherInfo)

@app.route('/',methods=['POST','GET'])
def startpage():
    error_msg = None
    #weatherInfo = ['21','rain']
    if request.method == 'POST':
        searchQ = request.form['inptbox']
        weatherInfo = GetWeatherData(searchQ)
        return render_template('startpage.html',data=weatherInfo)
    else:
        return render_template('error.html',error="")


if __name__ == '__main__':
    app.run(threaded=True)

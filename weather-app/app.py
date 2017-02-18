from flask import Flask,request
from flask import render_template
from Extractor import Wex



def ChangeImg(data):
    '''
    returns the weather icon based on the weather
    '''
    Weather_conditions = ['Clear','Rain','Sunny','Clouds']
    for x in Weather_conditions:
        if x == data[0]:
            return x
    return 'Clouds'

def BuildImgPath(image_name):
    '''
    Builds the path for the image icon in the static folder
    '''
    image_path = "/static/{0}.png".format(image_name)
    return image_path

def GetWeatherData(searchquery):
    '''
    Sends a request to the OpenWeather server and it returns a weather object.
    Uses an external tool to extract place mentions and request the weather of that place.
    '''
    weather = Wex.WexWeather(searchquery,"396cbf110cc7bd1bd3087f317643a83f")
    # adds the data to the data list
    data = weather.WexGetWeather() + weather.GetCityNames()
    # Changes the weather icon based on the current weather
    ImageName = ChangeImg(data)
    # Builds the path to the image icon
    imagePath = BuildImgPath(ImageName)
    data.append(imagePath)
    return data

app = Flask(__name__)

@app.route('/')
def startup():
    weatherInfo = []
    return render_template('startpage.html',data = weatherInfo)

@app.route('/',methods=['POST'])
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

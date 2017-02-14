from flask import Flask,request
from flask import render_template

app = Flask(__name__)


@app.route('/',methods=['POST','GET'])
def startpage():
    error_msg = None
    if request.method == 'GET':
        return render_template('startpage.html')
    else:
        error_msg = "eat Your shit asshole!"
        return render_template('error.html',error=error_msg)

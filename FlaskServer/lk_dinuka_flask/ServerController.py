from flask import Flask, render_template, request, session
from flask_cors import CORS
import Services as service

# reload(sys)
# sys.setdefaultencoding('utf8')

app = Flask(__name__)
app.config['SECRET_KEY'] = 'the quick brown fox jumps over the lazy dog'
app.config['CORS_HEADERS'] = 'Content-Type'
CORS(app)


@app.route("/", methods=['POST', 'GET'])
def getRoot():
    printLog('info', 'root')
    try:
        return render_template("home.html")
    except Exception as e:
        printLog('error', e)


@app.route("/userLogin/<username>/<password>", methods=['POST', 'GET'])
def login(username=None, password=None):
    printLog('info', username+" "+password)
    try:
        if service.validateUser(username=username, password=password):
            printLog('info', "user validated")
            return render_template('home.html')
    except Exception as e:
        printLog('error', e)


@app.route("/getMethod", methods=['POST', 'GET'])
def getMethod():
    printLog('info', 'Client Request on /getMethod')
    try:
        return "successful return statement"
    except Exception as e:
        printLog('error', e)
        return "unsuccessful return statement"


@app.route("/getHtml", methods=['POST', 'GET'])
def getHtml():
    printLog('info', 'Client Request on /getHtml')
    try:
        return render_template("index.html")
    except Exception as e:
        printLog('error', e)
        return "unsuccessful return statement"


@app.route('/getParamBasic/<username>/<password>')
def getParamBasic(username=None, password=None):
    try:
        return "name is : " + username + " " + password
    except Exception as e:
        printLog('error', e)


@app.route("/getParamAdv", methods=['POST', 'GET'])
def getParamAdv(msg=None):
    printLog('info', 'Client Request on /getParam')
    try:
        # request parameters
        msg = request.args['msg']
        # session parameters
        msg = session['msg']
        return msg
    except Exception as e:
        printLog('error', e)
        return "unsuccessful return statement"


def printLog(level, message):
    if level == 'info':
        print "[INFO]: ", message
    elif level == 'error':
        print "[ERROR]: ", message
    elif level == 'process':
        print "[PROCESS]: ", message


if __name__ == "__main__":
    try:
        app.run(host='0.0.0.0', debug=False, port=3651, threaded=True)
    except Exception as e:
        print(e)

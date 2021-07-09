from flask import Flask, render_template, request

from suds.client import Client

app = Flask(__name__)

@app.route('/', methods=['POST', 'GET'])
def hello_world():
    if request.method == 'POST':
        try:
            url = 'http://127.0.0.1:9876/ForschService.asmx?wsdl'
            client = Client(url)
            client.options.location = 'http://127.0.0.1:9876/ForschService.asmx'
            result = client.service.Evaluate(request.form['code'])
        except Exception as e:
            result = "Error communicating with Forsch server: " + str(e)
        return render_template('index.html', result=result)
    else:
        return render_template('index.html')

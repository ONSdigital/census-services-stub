import json

from structlog import PrintLogger  # added by EC

from flask import Flask
from iac_stub import Iac_Stub
from flask import Response

app = Flask(__name__)


@app.route('/')
def hello():
    return "Hello from Census Services Stub!"

"""The value of <section> can be any iac that the user enters. However, the response will ignore the value of <section>
 and instead take the iac value to be this fixed iac value: b4t7g3xby5bx"""
@app.route('/iacs/<section>')
def show_iac_data(section):
    PrintLogger().info("Now in the show_iac_data function. Section is: " + section)
    my_iac_stub = Iac_Stub()
    data = Iac_Stub.get_iac_stub(my_iac_stub)
    PrintLogger().info("Data returned successfully")
    data_as_json = json.dumps(data, separators=(',', ':'))
    return Response(data_as_json, mimetype='application/json')

if __name__ == '__main__':
    app.run(host='localhost', port=8121)

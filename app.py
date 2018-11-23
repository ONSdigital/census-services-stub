import json

from structlog import PrintLogger  # added by EC

from flask import Flask
from flask import Response
from iac_stub import Iac_Stub
from case_stub import Case_Stub

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

  
@app.route('/cases/0337c579-ce9d-4357-a620-5e4c565cfac1')
def show_case_data():
    PrintLogger().info("Now in the show_case_data function")
    my_case_stub = Case_Stub()
    data = Case_Stub.get_case_stub(my_case_stub)
    PrintLogger().info("Data returned successfully")
    return Response(json.dumps(data, separators=(',', ':')), mimetype='application/json')

  
"""The port below needs to be changed depending on which stub we're using, as follows:
iac is port 8121, 
case is port 8171"""
if __name__ == '__main__':
    app.run(host='localhost', port=8121)

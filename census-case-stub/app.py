import json

from structlog import PrintLogger  # added by EC

from flask import Flask, request
from flask import Response
from iac_stub import Iac_Stub
from case_stub import Case_Stub

app = Flask(__name__)


@app.route('/')
def hello():
    return "Hello from Census Case Stub!"


@app.route('/cases/0337c579-ce9d-4357-a620-5e4c565cfac1')
def show_case_data():
    PrintLogger().info("Now in the show_case_data function")
    my_case_stub = Case_Stub()
    data = Case_Stub.get_case_stub(my_case_stub)
    PrintLogger().info("Data returned successfully")
    data_as_json = json.dumps(data, separators=(',', ':'))
    return Response(data_as_json, mimetype='application/json')


@app.route('/cases/0337c579-ce9d-4357-a620-5e4c565cfac1/events', methods=['GET', 'POST'])
def result():
    PrintLogger().info("Now in the result function")
    PrintLogger().info("The request is: " + str(request))
    my_case_stub = Case_Stub()
    data = Case_Stub.get_reponse_for_eq_stub(my_case_stub)
    data_as_json = json.dumps(data, separators=(',', ':'))
    PrintLogger().info("Now returning the response to forward to EQ")
    return Response(data_as_json, mimetype='application/json')


if __name__ == '__main__':
    app.run(host='localhost', port=8171)

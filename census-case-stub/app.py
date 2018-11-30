import json

from structlog import PrintLogger  # added by EC

from flask import Flask, request
from flask import Response
from iac_stub import Iac_Stub
from case_stub import Case_Stub

app = Flask(__name__)


@app.route('/')
def hello():
    """Print text to show that the application is responding"""
    return "Hello from Census Case Stub!"


@app.route('/cases/<section>')
def show_case_data(section):
    """Show the fixed case json data that is produced by this case stub. The json data should be shown at the URL http://localhost:8171/cases/<section>
    The value of <section> will be the case UUID that corresponds to the IAC that the user enters. However the fixed json response will ignore
    the value of <section>, for the case UUID, and instead take the case UUID to be this fixed value: 0337c579-ce9d-4357-a620-5e4c565cfac1
    """
    PrintLogger().info("Now in the show_case_data function. Section is: " + section)
    my_case_stub = Case_Stub()
    data = Case_Stub.get_case_stub(my_case_stub)
    PrintLogger().info("Data returned successfully")
    data_as_json = json.dumps(data, separators=(',', ':'))
    return Response(data_as_json, mimetype='application/json')


@app.route('/cases/<section>/events', methods=['GET', 'POST'])
def result(section):
    """Accept a POST request and then respond to a GET request by showing some fixed json data to be forwarded to the EQ service. Both the POST and
    GET requests are handled by the URL http://localhost:8171/cases/<section>/events. The value of <section> will be the case UUID that corresponds
    to the IAC that the user enters."""
    PrintLogger().info("Now in the result function. Section is: " + section)
    my_case_stub = Case_Stub()
    data = Case_Stub.get_reponse_for_eq_stub(my_case_stub)
    data_as_json = json.dumps(data, separators=(',', ':'))
    PrintLogger().info("Now returning the response to forward to EQ")
    return Response(data_as_json, mimetype='application/json')


if __name__ == '__main__':
    app.run(host='localhost', port=8171)

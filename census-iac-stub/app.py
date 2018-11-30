import json

from structlog import PrintLogger  # added by EC

from flask import Flask
from flask import Response
from iac_stub import Iac_Stub

app = Flask(__name__)


@app.route('/')
def hello():
    """Print text to show that the application is responding"""
    return "Hello from Census IAC Stub!"


@app.route('/iacs/<section>')
def show_iac_data(section):
    """Show the fixed IAC json data that is produced by this iac stub. The json data should be shown at the URL http://localhost:8121/iacs/<section>
    The value of <section> can be any iac that the user enters.
    """
    PrintLogger().info("Now in the show_iac_data function. Section is: " + section)
    my_iac_stub = Iac_Stub()
    data = Iac_Stub.get_iac_stub(my_iac_stub, section) # get the fixed response as a dictionary object
    PrintLogger().info("Data returned successfully")
    data_as_json = json.dumps(data, separators=(',', ':')) # convert the dictionary object to a json object
    return Response(data_as_json, mimetype='application/json')


if __name__ == '__main__':
    app.run(host='localhost', port=8121)

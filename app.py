import json

from structlog import PrintLogger  # added by EC

from flask import Flask
from iac_stub import Iac_Stub

app = Flask(__name__)


@app.route('/')
def hello():
    return "Hello from Census Services Stub!"


@app.route('/iacs/b4t7g3xby5bx')
def show_iac_data():
    PrintLogger().info("Now in the show_iac_data function")
    my_iac_stub = Iac_Stub()
    data = Iac_Stub.get_iac_stub(my_iac_stub)
    PrintLogger().info("Data returned successfully")
    return json.dumps(data)

# @app.route('/iacs/b4t7g3xby5bx')
# def stub_iac_data():
# 	PrintLogger().info("Now in the stub_iac_data function")
# 	iac_fixed_response = {'caseId': '0337c579-ce9d-4357-a620-5e4c565cfac1',
# 						  'caseRef': '1000000000000002',
# 						  'iac': 'b4t7g3xby5bx',
# 						  'active': True}
# 	PrintLogger().info("Nearly through the stub_iac_data function")
# 	return json.dumps(iac_fixed_response)

if __name__ == '__main__':
    app.run(host='localhost', port=8121)

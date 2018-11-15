from structlog import PrintLogger #added by EC

from flask import Flask
from iac_stub import Iac_Stub
app = Flask(__name__)


@app.route('/')
def hello():
	return "Hello again from Census IAC Stub!"

@app.route('/iacs/b4t7g3xby5bx')
def show_iac_data():
	PrintLogger().info("Now in the show_iac_data function")
	my_iac_stub = Iac_Stub()
	data = Iac_Stub.get_iac_stub(my_iac_stub)
	PrintLogger().info("Data returned successfully")
	return data

if __name__ == '__main__':
	app.run(host='localhost', port=8121)
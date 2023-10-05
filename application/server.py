''' Server and routes '''

from flask import Flask
from flask.views import MethodView

HELLO_WORLD = "Hello World!"

class HelloWorldView(MethodView):
    ''' Simple route to return hello world string '''
    def get(self):
        ''' get string '''
        return HELLO_WORLD


class Server:
    ''' Program server '''
    def __init__(self):
        self.app = Flask(__name__)
        hello_view = HelloWorldView.as_view('hello_world')
        self.app.add_url_rule('/', view_func=hello_view, methods=['GET'])

    def run(self):
        ''' Run server '''
        self.app.run(debug=True)

    def get_app(self):
        ''' Get server Flask app object '''
        return self.app

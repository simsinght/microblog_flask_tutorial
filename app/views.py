"""The views are the handlers that respond to requests from web
browsers or other clients. In Flask handlers are written as Python
functions. Each view function is mapped to one or more request URLs"""

from app import app

@app.route('/')
@app.route('/index')
def index():
    return "Hello, World!"

from flask import Flask
from flask_cors import CORS
import database
from resources.pelud import pelud_api

DEBUG = True
HOST = '127.0.0.1'
PORT = '5000'

app = Flask(__name__)
app.register_blueprint(pelud_api)
cors = CORS(app)
#možemo definirati url i ovdje

@app.route('/')
def hello_world():
    return 'Hello World!'


if __name__ == '__main__':
    database.initialize()
    # app.run(debug=DEBUG, host=HOST, port=PORT, ssl_context='adhoc')
    app.run(debug=DEBUG, host=HOST, port=PORT,)

from flask import Flask
import os


app = Flask(__name__)


@app.route('/')
def index():
    var = os.environ['TEST_ENV_VAR']
    return 'hello, world with CI/CD ' + var 

from Revolt import Revolt
import json

from flask import Flask
from flask import Flask , make_response , request
from flask_httpauth import HTTPBasicAuth

app = Flask(__name__)
auth = HTTPBasicAuth()

users = {
    'Us3r': 'P@ssw()rd'
}


@auth.verify_password
def verify_password(username, password):
    if not (username and password):
        return False
    return users.get(username) == password


@app.route('/')
@auth.login_required
def index():
    return "Hello, %s!" % auth.username()


@app.route('/nest/<levels>', methods=['POST'])
@auth.login_required
def nest(levels):
    ## Instantiating Nest()
    revolt = Revolt()
    arguments = levels.split(",")
    input_data = request.get_json(silent=True)
    output_dict = revolt.get_dict(input_data, arguments)

    ## Making sure the browser will interpret
    ## the json format correctly
    response = make_response(json.dumps(output_dict, indent=2, sort_keys=True))
    response.headers['content-type'] = 'application/json'

    return response

if __name__ == '__main__':
    app.run(debug=True)

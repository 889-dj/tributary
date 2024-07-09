# import the flask web framework
from flask import Flask

# create a Flask server, and allow us to interact with it using the app variable
app = Flask(__name__)


# define an endpoint which accepts POST requests, and is reachable from the /record endpoint
@app.route('/record', methods=['POST'])
def record_engine_temperature():
    # every time the /record endpoint is called, the code in this block is executed
    pass
    
    # return a json payload, and a 200 status code to the client
    return {"success": True}, 200


# practically identical to the above
@app.route('/collect', methods=['POST'])
def collect_engine_temperature():
    return {"success": True}, 200
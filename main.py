from flask import *
import json, time

app = Flask(__name__)

@app.route('/', methods=['GET'])
def home_page():
    data_set = {'Page': 'Home', 'Message': 'Successfully loaded the Home page', 'Timestamp':time.time()}
    json_dump = json.dumps(data_set)


    return json_dump

@app.route('/request/', methods=['GET'])
def request_page():
    user_query = str(request.args.get('user')) #/user/?user=anyuser

   
    data_set = {'Page': 'Request', 'Message': 'Successfully got the request for {user_query}', 'Timestamp':time.time()}
    json_dump = json.dumps(data_set)


    return json_dump


@app.route('/dumb/', methods=['GET'])
def dumb_page():
    user_query = str(request.args.get('user')) #/user/?user=anyuser

   
    data_set = {'Page': 'Dumb', 'Message': 'Successfully got the dumb for {user_query}', 'Timestamp':time.time()}
    json_dump = json.dumps(data_set)


    return json_dump

if __name__ == '__main__':
    app.run(port=7777) #any port u want doesn't matter
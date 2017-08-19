from flask import Flask,request, json
from flask.json import jsonify
from datetime import datetime
from flask.wrappers import Response
from flask_cors import CORS, cross_origin
import os

app = Flask(__name__)

wsgi_app = app.wsgi_app

@app.route('/')
def root():
    return app.send_static_file('index.html')

class Psaas():
    @app.route('/orders', methods=['GET'])
    def renderblog():
        DATA_FILENAME = os.path.join(app.static_folder, 'data.json')
        with open(DATA_FILENAME) as json_file:
            data = json.load(json_file)
            print (data)
            return jsonify({'orders':data})


   
    @app.route("/orders", methods=['POST'])
    def create_task():
        DATA_FILENAME = os.path.join(app.static_folder, 'data.json')
        with open(DATA_FILENAME) as json_file:
            orders=json.load(json_file)
        with open(DATA_FILENAME, mode='w', encoding='utf-8') as json_file:
            json.dump([], json_file)
        with open(DATA_FILENAME, mode='w', encoding='utf-8') as json_file:
            if not request.json or not 'ordered_by' in request.json:
                    abort(400)
            order = {
                'id': orders[-1]['id'] + 1,
                'ordered_on': datetime.now(),
                'ordered_by': request.json['ordered_by'],
                'items': request.json.get('items', ""),
                'count': request.json.get('count', "")
                }
            orders.append(order)
            json.dump(orders, json_file)
            print (orders)
            return jsonify({'orders': orders}), 201

if __name__ == '__main__':
    app.run()
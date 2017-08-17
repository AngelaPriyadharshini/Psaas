from flask import Flask,request, json
from flask.json import jsonify
from datetime import datetime
from flask.wrappers import Response
from flask_cors import CORS, cross_origin
import MySQLdb

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:mySQLp@ssw0rd@localhost/db_psaas'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['MYSQL_DATABASE_USER'] = 'root'
app.config['MYSQL_DATABASE_PASSWORD'] = 'mySQLp@ssw0rd'
app.config['MYSQL_DATABASE_DB'] = 'db_psaas'
app.config['MYSQL_DATABASE_HOST'] = 'localhost'

wsgi_app = app.wsgi_app

@app.route('/')
def root():
    return app.send_static_file('index.html')

class Psaas():
    @app.route('/orders', methods=['GET'])
    def get():
        if request.method == 'GET':
            db = MySQLdb.connect("localhost","root","mySQLp@ssw0rd","db_psaas" )
            cursor = db.cursor()
            cursor.execute("SELECT * from party_orders")
            rows = cursor.fetchall()
            orders = []
            for result in rows:
                orders.append({
                'id':result[0],
                'ordered_on':result[1],
                'ordered_by':result[2],
                'items':result[3],
                'count':result[4]
            })
        return jsonify({'orders':orders})

   
    @app.route("/orders", methods=['POST'])
    def add():
        jsdata = request.get_json(force=True)
        print(jsdata)
        db = MySQLdb.connect("localhost","root","mySQLp@ssw0rd","db_psaas" )
        cursor = db.cursor()
        cursor.execute("INSERT INTO party_orders (OrderedOn, OrderedBy, Item, Count) VALUES (%s,%s,%s,%s)", (datetime.now(),jsdata['ordered_by'], jsdata['items'], jsdata['count']))
        db.commit()
        return Response(jsdata)  

if __name__ == '__main__':
    app.run()
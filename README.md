# colin1118
python_flask demon
from flask import Flask,json,jsonify,request, send_from_directory
from flask_pymongo import PyMongo
import flask
#from flask_cors import CORS
app = Flask(__name__)
#CORS(app)
mongodb_client = PyMongo(app, uri="mongodb://localhost:27017/admin")
db = mongodb_client.db
app.config["MONGO_URI"] = "mongodb://localhost:27017/admin"
mongodb_client = PyMongo(app)
db = mongodb_client.db
# Dashboard
@app.route("/")
def Dashboard():
 #db.todos.insert_one({'title': "todo title", 'body': "todo body"})
 return "success"

@app.route("/add_many")
def add_many():
    # db.todos.insert_many([
    #     {'_id': 1, 'title': "todo title one ", 'body': "todo body one "},
    #     {'_id': 2, 'title': "todo title two", 'body': "todo body two"},
    #     {'_id': 3, 'title': "todo title three", 'body': "todo body three"},
    #     {'_id': 4, 'title': "todo title four", 'body': "todo body four"},
    #     {'_id': 5, 'title': "todo title five", 'body': "todo body five"},
    #     {'_id': 1, 'title': "todo title six", 'body': "todo body six"},
    #     ])
    return flask.jsonify(message="success")


@app.route("/find")
def home():
    todos =db.todos.find()
    #print('print : '+todos)
    for todos in todos:
       print(todos)
    #return jsonify({"title":"todo title"})
    visitors_list = list(todos)
    #return json.dumps([todo for todo in todos])
    #return json.dumps(visitors_list)
    return jsonify({"status": 200, "visitors": visitors_list}), 200
@app.route("/get_todo/<int:todoId>")
def insert_one(todoId):
    todo = db.todos.find_one({"_id": todoId})
    return todo

app.run(port='5000')
#if __name__ == "__main__":
  

import os
from flask import Flask, render_template, redirect, request, url_for
from flask_pymongo import PyMongo
from bson.objectid import ObjectId
if os.path.exists("env.py"):
    import env


app = Flask(__name__)


secret_key = os.environ.get('secret_key')

app.config['MONGO_DBNAME'] = 'dino-index'
app.config['MONGO_URI'] = os.environ.get('MONGO_URI')

mongo = PyMongo(app)


@app.route('/')
@app.route('/get_dinoInfo')
def get_dinoInfo():
    return render_template('main-page.html', dinoInfo=mongo.db.dinoInfo.find())


@app.route("/add_info")
def add_info():
    return render_template("add_info.html")


if __name__ == '__main__':
    app.run(host=os.environ.get('IP'),
            port=int(os.environ.get('PORT')),
            debug=True)

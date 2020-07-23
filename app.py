import os
from flask import Flask, render_template, redirect, request, url_for
from flask_pymongo import PyMongo
from bson.objectid import ObjectId


app = Flask(__name__)


app.config['MONGO_DBNAME'] = 'dino-index'
app.config['MONGO_URI'] = 'mongo "mongodb+srv://cluster0.pgi7y.mongodb.net/dino-index" --username dinoguy'


mongo = PyMongo(app)


@app.route('/')
@app.route('/get_dinoInfo')
def get_dinoInfo():
    return render_template('info.html', dinoInfo=mongo.db.dinoInfo.find())


if __name__ == '__main__':
    app.run(host=os.environ.get('IP'),
            port=int(os.environ.get('PORT')),
            debug=True)

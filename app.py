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
@app.route('/index')
def index():
    return render_template('index.html', dinoInfo=mongo.db.dinoInfo.find())


@app.route('/main_page')
def main_page():
    return render_template('main_page.html', dinoInfo=mongo.db.dinoInfo.find())


@app.route('/final_page')
def final_page():
    return render_template(
        'final_page.html', dinoInfo=mongo.db.dinoInfo.find())


@app.route('/add_info', methods=["GET", "POST"])
def add_info():
    if request.method == "POST":
        info = {
            "name": request.form.get("name"),
            "time_period": request.form.get("time_period"),
            "diet": request.form.get("diet"),
            "height": request.form.get("height"),
            "speed": request.form.get("speed"),
            "discovered_in": request.form.get("discovered_in")
        }
        mongo.db.dinoInfo.insert_one(info)
        return redirect(url_for("main_page"))

    return render_template('add_info.html', dinoInfo=mongo.db.dinoInfo.find())


if __name__ == '__main__':
    app.run(host=os.environ.get('IP'),
            port=int(os.environ.get('PORT')),
            debug=True)

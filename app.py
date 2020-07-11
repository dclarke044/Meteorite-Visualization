
import datetime as dt
import numpy as np
import pandas as pd
 

import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func
from flask import Flask, render_template, redirect, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from models import create_classes

from config import username, password

#https://stackabuse.com/using-sqlalchemy-with-flask-and-postgresql/
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = f'postgresql://{username}:{password}@localhost:5432/meteorites_db'
db = SQLAlchemy(app)
meteorites = create_classes(db)
migrate = Migrate(app, db)

@app.route('/')
def home():
    return render_template('index.html')

@app.route("/bar")
def bar():
        return "BAR"

@app.route("/bubble")
def bubble():
        return "BUBBLE"

@app.route("/map")
def map():
        return "MAP"

@app.route("/data")
def data():
        return "DATA"

@app.route("/raw_data")
def data_pull():
        results = db.session.query(meteorites.id, meteorites.name, meteorites.recclass, meteorites.mass, meteorites.fall, meteorites.year, meteorites.reclat, meteorites.reclong, meteorites.maincategory).all()

        id = [result[0] for result in results]
        name = [result[1] for result in results]
        recclass = [result[2] for result in results]
        mass = [result[3] for result in results]
        fall = [result[4] for result in results]
        year = [result[5] for result in results]
        reclat = [result[6] for result in results]
        reclong = [result[7] for result in results]
        maincategory = [result[8] for result in results]

        data = [{'id':id,
                'name':name,
                'recclass':recclass,
                'mass':mass,
                'fall':fall,
                'year':year,
                'reclat':reclat,
                'reclong':reclong,
                'maincategory':maincategory}]

        data = jsonify(data)

        return data

if __name__ == '__main__':
    app.run()
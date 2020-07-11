
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

# engine = create_engine(f'postgresql://{username}:{password}@localhost:5432/meteorites_db')
# connection = engine.connect()

# Import results
results = db.session.query(meteorites.id, meteorites.name).all()

id = [result[0] for result in results]
name = [result[1] for result in results]

data = [{'id':id,
        'name':name}]

data = jsonify(data)

print(data)

# @app.route('/')
# def home():
#     return render_template('index.html')

# @app.route("/bar")
# def bar():
#     results = db.session.query(meteorites).all()

#     # hover_text = [result[0] for result in results]
#     # lat = [result[1] for result in results]
#     # lon = [result[2] for result in results]

#     # pet_data = [{
#     #     "type": "scattergeo",
#     #     "locationmode": "USA-states",
#     #     "lat": lat,
#     #     "lon": lon,
#     #     "text": hover_text,
#     #     "hoverinfo": "text",
#     #     "marker": {
#     #         "size": 50,
#     #         "line": {
#     #             "color": "rgb(8,8,8)",
#     #             "width": 1
#     #         },
#     #     }
#     # }]

#     return jsonify(results)


# if __name__ == '__main__':
#     app.run()
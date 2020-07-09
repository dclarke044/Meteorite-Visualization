
import datetime as dt
import numpy as np
import pandas as pd

import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func
from flask import Flask, render_template, redirect, jsonify

from config import username, password

app = Flask(__name__)

engine = create_engine(f'postgresql://{username}:{password}@localhost:5432/meteorites_db')
connection = engine.connect()

@app.route('/')
def home():
    return render_template('index.html')


if __name__ == '__main__':
    app.run()
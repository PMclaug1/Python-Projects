import json
from flask_app import app
from flask import redirect, render_template
import os



@app.route('/')
def index():
   return render_template('index.html')


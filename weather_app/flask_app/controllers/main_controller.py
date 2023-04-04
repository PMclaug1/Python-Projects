import json
from flask_app import app
from flask import redirect, render_template
from flask import Flask



@app.route('/members')
def members():
   return {"members": ["Member1", "Member2", "Member3"]}


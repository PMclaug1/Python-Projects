import json
from flask_app import app
from flask import redirect, render_template



# here will be for returing api call with SQL
@app.route('/members')
def members():
   return {"members": ["Member1", "Member2", "Member3"]}


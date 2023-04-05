from flask import Flask
from flask_cors import CORS

app = Flask(__name__)
CORS(app)
app.secret_key ="no secretos"
DATABASE = 'python_weather'
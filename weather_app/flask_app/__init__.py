from flask import Flask

app = Flask(__name__)
app.secret_key ="no secretos"
DATABASE = 'python_weather'
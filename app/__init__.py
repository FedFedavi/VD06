from flask import Flask

app = Flask(__name__)
app.config['SECRET_KEY'] = 'you-will-newer-guess'

from app import routes
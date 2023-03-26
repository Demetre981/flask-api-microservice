from flask import Flask
from flask_login import LoginManager


app = Flask(__name__)
app.secret_key ="eWPrsDUYC8Qcx8ESFLa3qTgN"

login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = "login"


from app import routes

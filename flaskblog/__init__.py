# __init__.py

# Dependencies
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager


app = Flask(__name__)

app.config['SECRET_KEY'] = 'e94f492957e9be802f10ca325ee12cb3'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'

db = SQLAlchemy(app)

# used for protecting user passwords
bcrypt = Bcrypt(app)

# log in manager
login_manager = LoginManager(app)
#redirect and alert if someone tries to access account page while not logged in
login_manager.login_view = 'login'
login_manager.login_message_category = 'info'

from flaskblog import routes
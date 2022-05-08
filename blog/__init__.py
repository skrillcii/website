# Standard imports
import logging
from os.path import abspath, dirname, exists, join
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager

# Initialize logging
logging.basicConfig(filename='blog.log', level=logging.DEBUG)

# Initialize app
app = Flask(__name__)
app.config['SECRET_KEY'] = '5791628bb0b13ce0c676dfde280ba245'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize database
db = SQLAlchemy(app)
if exists(join(dirname(abspath(__file__)), 'site.db')):
    logging.info('Database site.db exists!')
    logging.info('Skip database site.db creation.')
else:
    logging.info('Creating database site.db...')
    db.create_all()
    logging.info('Created database site.db!')

# Initialize authentication
bcrypt = Bcrypt(app)
login_manager = LoginManager(app)
login_manager.login_view = 'login'
login_manager.login_message_category = 'info'


from blog import routes

from flask import Flask, session, redirect, url_for, flash, request
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Import extensions from models
from models import db, bcrypt

def create_app():
    app = Flask(__name__)

    # Configuration
    app.config['SECRET_KEY'] = os.environ.get('SECRET_KEY', 'dev-secret-key')
    
    # Database Configuration (MySQL or SQLite)
    db_type = os.environ.get('DB_TYPE', 'sqlite').lower()
    
    if db_type == 'mysql':
        db_host = os.environ.get('DB_HOST', 'localhost')
        db_user = os.environ.get('DB_USER', 'root')
        db_password = os.environ.get('DB_PASSWORD', '')
        db_name = os.environ.get('DB_NAME', 'mode_avenue_db')
        app.config['SQLALCHEMY_DATABASE_URI'] = f'mysql+pymysql://{db_user}:{db_password}@{db_host}/{db_name}'
    else:
        db_path = os.path.join(app.root_path, 'mode_avenue.db')
        app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{db_path}'
        
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    app.config['UPLOAD_FOLDER'] = os.path.join(app.root_path, 'static', 'uploads')

    # Initialize extensions with app
    db.init_app(app)
    bcrypt.init_app(app)

    # Create upload folder if it doesn't exist
    os.makedirs(app.config['UPLOAD_FOLDER'], exist_ok=True)

    # Register blueprints
    from auth import auth as auth_blueprint
    from main import main as main_blueprint
    from products import products as products_blueprint
    from cart import cart as cart_blueprint
    from admin import admin as admin_blueprint

    app.register_blueprint(auth_blueprint)
    app.register_blueprint(main_blueprint)
    app.register_blueprint(products_blueprint, url_prefix='/products')
    app.register_blueprint(cart_blueprint, url_prefix='/cart')
    app.register_blueprint(admin_blueprint, url_prefix='/admin')

    # Add Python functions to Jinja2 globals
    app.jinja_env.globals.update(min=min, max=max, len=len, range=range)

    return app

# Custom authentication functions
def login_user(user):
    session['user_id'] = user.id
    session['username'] = user.username
    session['is_admin'] = user.is_admin

def logout_user():
    session.pop('user_id', None)
    session.pop('username', None)
    session.pop('is_admin', None)

def current_user():
    if 'user_id' in session:
        from models import User
        return User.query.get(session['user_id'])
    return None

def login_required(f):
    from functools import wraps
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if 'user_id' not in session:
            flash('Please log in to access this page.', 'warning')
            return redirect(url_for('auth.login', next=request.url))
        return f(*args, **kwargs)
    return decorated_function

def admin_required(f):
    from functools import wraps
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if 'user_id' not in session:
            flash('Please log in to access this page.', 'warning')
            return redirect(url_for('admin.admin_login', next=request.url))
        if not session.get('is_admin', False):
            flash('Admin access required.', 'danger')
            return redirect(url_for('admin.admin_login'))
        return f(*args, **kwargs)
    return decorated_function

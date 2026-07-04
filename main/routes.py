from flask import Blueprint, render_template
from models import Category, Product

main = Blueprint('main', __name__)

@main.route('/')
@main.route('/home')
def home():
    categories = Category.query.all()
    featured_products = Product.query.limit(8).all()
    return render_template('home.html', title='Home', categories=categories, featured_products=featured_products)

@main.route('/about')
def about():
    return render_template('about.html', title='About Us')

@main.route('/contact')
def contact():
    return render_template('contact.html', title='Contact Us')

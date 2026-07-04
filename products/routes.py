from flask import Blueprint, render_template, request, redirect, url_for, flash
from models import db
from models import Product, Category
from forms import ProductForm
from app import current_user

products = Blueprint('products', __name__)

@products.route('/')
def index():
    page = request.args.get('page', 1, type=int)
    category_id = request.args.get('category', type=int)
    gender = request.args.get('gender')

    query = Product.query

    if category_id:
        query = query.filter_by(category_id=category_id)
    elif gender:
        query = query.join(Category).filter(Category.gender == gender)

    products_list = query.paginate(page=page, per_page=12)
    categories = Category.query.all()

    return render_template('products/index.html', title='Products',
                         products=products_list, categories=categories, current_user=current_user)

@products.route('/<int:product_id>')
def detail(product_id):
    product = Product.query.get_or_404(product_id)
    user = current_user()
    
    in_wishlist = False
    if user:
        from models import Wishlist
        existing = Wishlist.query.filter_by(user_id=user.id, product_id=product_id).first()
        in_wishlist = True if existing else False
        
    # Get related products from the same category (excluding current product)
    related_products = Product.query.filter(
        Product.category_id == product.category_id,
        Product.id != product.id
    ).limit(4).all()
    return render_template('products/detail.html', title=product.name, product=product, 
                         current_user=user, related_products=related_products,
                         in_wishlist=in_wishlist)

@products.route('/category/<int:category_id>')
def category(category_id):
    category = Category.query.get_or_404(category_id)
    page = request.args.get('page', 1, type=int)
    products_list = Product.query.filter_by(category_id=category_id).paginate(page=page, per_page=12)

    return render_template('products/category.html', title=category.name,
                         category=category, products=products_list, Category=Category, current_user=current_user)

@products.route('/gender/<gender>')
def gender(gender):
    if gender not in ['men', 'women', 'kids']:
        flash('Invalid gender category', 'danger')
        return redirect(url_for('products.index'))

    page = request.args.get('page', 1, type=int)
    products_list = Product.query.join(Category).filter(Category.gender == gender).paginate(page=page, per_page=12)
    categories = Category.query.filter_by(gender=gender).all()

    return render_template('products/gender.html', title=f'{gender.title()} Fashion',
                         gender=gender, products=products_list, categories=categories, current_user=current_user)

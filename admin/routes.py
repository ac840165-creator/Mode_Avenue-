from flask import Blueprint, render_template, request, redirect, url_for, flash, session
from urllib.parse import urlparse
from models import db
from models import Product, Category, Order, User
from forms import LoginForm, ProductForm, CategoryForm
from app import admin_required, login_required, current_user, logout_user, bcrypt, login_user

admin = Blueprint('admin', __name__)

@admin.route('/admin_login', methods=['GET', 'POST'])
def admin_login():
    """Admin login page - handles admin authentication directly"""
    if 'user_id' in session:
        user = current_user()
        if user and user.is_admin:
            return redirect(url_for('admin.dashboard'))

    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if user and bcrypt.check_password_hash(user.password, form.password.data):
            if user.is_admin:
                login_user(user)
                flash('Admin login successful!', 'success')
                next_page = request.args.get('next')
                if not next_page or urlparse(next_page).netloc != '':
                    next_page = url_for('admin.dashboard')
                return redirect(next_page)
            else:
                flash('Access denied. Admin privileges required.', 'danger')
        else:
            flash('Login unsuccessful. Please check email and password', 'danger')
    return render_template('admin/login.html', title='Admin Login', form=form)

@admin.route('/admin_logout')
@login_required
def admin_logout():
    """Admin logout - clears session and redirects to admin login"""
    logout_user()
    flash('You have been logged out successfully.', 'info')
    return redirect(url_for('admin.admin_login'))

@admin.route('/')
@admin_required
def dashboard():
    products_count = Product.query.count()
    categories_count = Category.query.count()
    orders_count = Order.query.count()
    recent_orders = Order.query.order_by(Order.order_date.desc()).limit(5).all()

    return render_template('admin/dashboard.html', title='Admin Dashboard',
                         products_count=products_count, categories_count=categories_count,
                         orders_count=orders_count, recent_orders=recent_orders)

@admin.route('/products')
@admin_required
def products():
    page = request.args.get('page', 1, type=int)
    products_list = Product.query.paginate(page=page, per_page=20)
    return render_template('admin/products.html', title='Manage Products', products=products_list)

@admin.route('/products/add', methods=['GET', 'POST'])
@admin_required
def add_product():
    form = ProductForm()
    form.category_id.choices = [(c.id, c.name) for c in Category.query.all()]

    if form.validate_on_submit():
        product = Product(name=form.name.data, description=form.description.data,
                         price=form.price.data, stock=form.stock.data,
                         image_file=form.image_file.data,
                         category_id=form.category_id.data)
        db.session.add(product)
        db.session.commit()
        flash('Product added successfully', 'success')
        return redirect(url_for('admin.products'))

    return render_template('admin/add_product.html', title='Add Product', form=form)

@admin.route('/products/edit/<int:product_id>', methods=['GET', 'POST'])
@admin_required
def edit_product(product_id):
    product = Product.query.get_or_404(product_id)
    form = ProductForm()
    form.category_id.choices = [(c.id, c.name) for c in Category.query.all()]

    if form.validate_on_submit():
        product.name = form.name.data
        product.description = form.description.data
        product.price = form.price.data
        product.stock = form.stock.data
        product.image_file = form.image_file.data
        product.category_id = form.category_id.data
        db.session.commit()
        flash('Product updated successfully', 'success')
        return redirect(url_for('admin.products'))
    elif request.method == 'GET':
        form.name.data = product.name
        form.description.data = product.description
        form.price.data = product.price
        form.stock.data = product.stock
        form.image_file.data = product.image_file
        form.category_id.data = product.category_id

    return render_template('admin/edit_product.html', title='Edit Product', form=form, product=product)

@admin.route('/products/delete/<int:product_id>', methods=['POST'])
@admin_required
def delete_product(product_id):
    product = Product.query.get_or_404(product_id)
    db.session.delete(product)
    db.session.commit()
    flash('Product deleted successfully', 'success')
    return redirect(url_for('admin.products'))

@admin.route('/categories')
@admin_required
def categories():
    categories_list = Category.query.all()
    return render_template('admin/categories.html', title='Manage Categories', categories=categories_list)

@admin.route('/categories/add', methods=['GET', 'POST'])
@admin_required
def add_category():
    form = CategoryForm()
    if form.validate_on_submit():
        category = Category(name=form.name.data, description=form.description.data, gender=form.gender.data)
        db.session.add(category)
        db.session.commit()
        flash('Category added successfully', 'success')
        return redirect(url_for('admin.categories'))

    return render_template('admin/add_category.html', title='Add Category', form=form)

@admin.route('/categories/edit/<int:category_id>', methods=['GET', 'POST'])
@admin_required
def edit_category(category_id):
    category = Category.query.get_or_404(category_id)
    form = CategoryForm()
    if form.validate_on_submit():
        category.name = form.name.data
        category.description = form.description.data
        category.gender = form.gender.data
        db.session.commit()
        flash('Category updated successfully', 'success')
        return redirect(url_for('admin.categories'))
    elif request.method == 'GET':
        form.name.data = category.name
        form.description.data = category.description
        form.gender.data = category.gender
    return render_template('admin/add_category.html', title='Edit Category', form=form, category=category)

@admin.route('/categories/delete/<int:category_id>', methods=['POST'])
@admin_required
def delete_category(category_id):
    category = Category.query.get_or_404(category_id)
    if category.products:
        flash('Cannot delete category with associated products.', 'danger')
    else:
        db.session.delete(category)
        db.session.commit()
        flash('Category deleted successfully', 'success')
    return redirect(url_for('admin.categories'))

@admin.route('/orders')
@admin_required
def orders():
    page = request.args.get('page', 1, type=int)
    orders_list = Order.query.order_by(Order.order_date.desc()).paginate(page=page, per_page=20)
    return render_template('admin/orders.html', title='Manage Orders', orders=orders_list)

@admin.route('/orders/<int:order_id>')
@admin_required
def view_order(order_id):
    order = Order.query.get_or_404(order_id)
    return render_template('admin/view_order.html', title=f'Order #{order.id}', order=order)

@admin.route('/orders/update_status/<int:order_id>', methods=['POST'])
@admin_required
def update_order_status(order_id):
    order = Order.query.get_or_404(order_id)
    new_status = request.form.get('status')
    valid_statuses = ['pending', 'confirmed', 'shipped', 'delivered', 'cancelled']
    
    if new_status in valid_statuses:
        order.status = new_status
        db.session.commit()
        flash(f'Order #{order.id} status updated to {new_status.title()}', 'success')
    else:
        flash('Invalid order status selected.', 'danger')
        
    return redirect(request.referrer or url_for('admin.orders'))

@admin.route('/settings')
@admin_required
def settings():
    return render_template('admin/settings.html', title='Admin Settings')

@admin.route('/users')
@admin_required
def users():
    page = request.args.get('page', 1, type=int)
    users_list = User.query.order_by(User.id.desc()).paginate(page=page, per_page=20)
    return render_template('admin/users.html', title='Manage Users', users=users_list)

@admin.route('/users/toggle_admin/<int:user_id>', methods=['POST'])
@admin_required
def toggle_admin(user_id):
    user = User.query.get_or_404(user_id)
    if user.id == current_user().id:
        flash('You cannot change your own admin status!', 'danger')
    else:
        user.is_admin = not user.is_admin
        db.session.commit()
        status = "granted" if user.is_admin else "revoked"
        flash(f'Admin privileges {status} for {user.username}', 'success')
    return redirect(url_for('admin.users'))

@admin.route('/users/delete/<int:user_id>', methods=['POST'])
@admin_required
def delete_user(user_id):
    user = User.query.get_or_404(user_id)
    if user.id == current_user().id:
        flash('You cannot delete yourself!', 'danger')
    elif user.is_admin:
        flash('Cannot delete another administrator!', 'danger')
    else:
        db.session.delete(user)
        db.session.commit()
        flash(f'User {user.username} deleted successfully.', 'success')
    return redirect(url_for('admin.users'))

from flask import Blueprint, render_template, url_for, flash, redirect, request, jsonify
from urllib.parse import urlparse
from models import db, bcrypt
from models import User
from forms import LoginForm, RegistrationForm
from app import login_user, logout_user, current_user, login_required

auth = Blueprint('auth', __name__)

@auth.route('/login', methods=['GET', 'POST'])
def login():
    if current_user():
        return redirect(url_for('main.home'))

    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if user and bcrypt.check_password_hash(user.password, form.password.data):
            login_user(user)
            flash('Login successful!', 'success')
            next_page = request.args.get('next')
            if not next_page or urlparse(next_page).netloc != '':
                next_page = url_for('main.home')
            return redirect(next_page)
        else:
            flash('Login unsuccessful. Please check email and password', 'danger')
    return render_template('login.html', title='Login', form=form)

@auth.route('/register', methods=['GET', 'POST'])
def register():
    if current_user():
        return redirect(url_for('main.home'))

    form = RegistrationForm()
    if form.validate_on_submit():
        hashed_password = bcrypt.generate_password_hash(form.password.data).decode('utf-8')
        user = User(username=form.username.data, email=form.email.data, password=hashed_password)
        db.session.add(user)
        db.session.commit()
        flash('Your account has been created! You are now able to log in', 'success')
        return redirect(url_for('auth.login'))
    return render_template('register.html', title='Register', form=form)

@auth.route('/logout')
def logout():
    logout_user()
    flash('You have been logged out.', 'info')
    return redirect(url_for('main.home'))

@login_required
@auth.route('/profile')
def profile():
    user = current_user()
    return render_template('profile_settings.html', title='Profile Settings', current_user=user)

@login_required
@auth.route('/wishlist')
def wishlist():
    user = current_user()
    from models import Wishlist, Product
    wishlist_items = []
    if user:
        # Get user's wishlist items with product details
        items = Wishlist.query.filter_by(user_id=user.id).all()
        for item in items:
            wishlist_items.append(item.product)
    return render_template('wishlist.html', title='My Wishlist', current_user=user, wishlist_items=wishlist_items)

@login_required
@auth.route('/orders')
def order_history():
    user = current_user()
    from models import Order
    orders = Order.query.filter_by(user_id=user.id).order_by(Order.order_date.desc()).all() if user else []
    return render_template('order_history.html', title='Order History', orders=orders, current_user=user)

@login_required
@auth.route('/wishlist/add/<int:product_id>', methods=['POST'])
def add_to_wishlist(product_id):
    user = current_user()
    from models import Wishlist
    if user:
        # Check if already in wishlist
        existing = Wishlist.query.filter_by(user_id=user.id, product_id=product_id).first()
        if not existing:
            new_item = Wishlist(user_id=user.id, product_id=product_id)
            db.session.add(new_item)
            db.session.commit()
            return jsonify({'success': True, 'message': 'Added to wishlist'})
        return jsonify({'success': True, 'message': 'Already in wishlist'})
    return jsonify({'success': False, 'message': 'User not found'})

@login_required
@auth.route('/addresses')
def addresses():
    user = current_user()
    from models import Address
    addresses = Address.query.filter_by(user_id=user.id).all() if user else []
    return render_template('addresses.html', title='Addresses', addresses=addresses, current_user=user)

@login_required
@auth.route('/wishlist/remove/<int:product_id>', methods=['POST'])
def remove_from_wishlist(product_id):
    user = current_user()
    from models import Wishlist
    if user:
        # Remove item from wishlist
        Wishlist.query.filter_by(user_id=user.id, product_id=product_id).delete()
        db.session.commit()
        return jsonify({'success': True})
    return jsonify({'success': False})

@login_required
@auth.route('/wishlist/clear', methods=['POST'])
def clear_wishlist():
    user = current_user()
    from models import Wishlist
    if user:
        # Clear all wishlist items for user
        Wishlist.query.filter_by(user_id=user.id).delete()
        db.session.commit()
        return jsonify({'success': True})
    return jsonify({'success': False})

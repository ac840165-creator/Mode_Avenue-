from flask import Blueprint, render_template, request, redirect, url_for, flash, make_response
from models import db
from models import Cart, CartItem, Product
from app import login_required, current_user
from utils import generate_invoice_pdf

cart = Blueprint('cart', __name__)

@cart.route('/')
@login_required
def view_cart():
    user = current_user()
    if user is None:
        flash('Please log in to access your cart.', 'warning')
        return redirect(url_for('auth.login', next=request.url))
    
    user_cart = Cart.query.filter_by(user_id=user.id).first()
    if not user_cart:
        user_cart = Cart(user_id=user.id)
        db.session.add(user_cart)
        db.session.commit()

    cart_items = CartItem.query.filter_by(cart_id=user_cart.id).all()
    total = sum(item.product.price * item.quantity for item in cart_items)

    return render_template('cart/view.html', title='Shopping Cart',
                         cart_items=cart_items, total=total)

@cart.route('/checkout')
@login_required
def checkout():
    user = current_user()
    if user is None:
        flash('Please log in to continue.', 'warning')
        return redirect(url_for('auth.login', next=request.url))
    
    user_cart = Cart.query.filter_by(user_id=user.id).first()
    if not user_cart:
        flash('Your cart is empty', 'warning')
        return redirect(url_for('products.index'))

    cart_items = CartItem.query.filter_by(cart_id=user_cart.id).all()
    if not cart_items:
        flash('Your cart is empty', 'warning')
        return redirect(url_for('products.index'))

    subtotal = sum(item.product.price * item.quantity for item in cart_items)
    tax = subtotal * 0.08
    total = subtotal + tax

    return render_template('cart/checkout.html', title='Checkout',
                         cart_items=cart_items, subtotal=subtotal, tax=tax, total=total)

@cart.route('/process-payment', methods=['POST'])
@login_required
def process_payment():
    user = current_user()
    if user is None:
        flash('Please log in to continue.', 'danger')
        return redirect(url_for('auth.login', next=request.url))
    
    user_cart = Cart.query.filter_by(user_id=user.id).first()
    
    if not user_cart:
        flash('Your cart is empty', 'danger')
        return redirect(url_for('cart.view_cart'))

    cart_items = CartItem.query.filter_by(cart_id=user_cart.id).all()
    if not cart_items:
        flash('Your cart is empty', 'danger')
        return redirect(url_for('cart.view_cart'))

    # Get payment form data
    payment_method = request.form.get('payment_method')
    card_number = request.form.get('card_number', '')[-4:]  # Only last 4 digits
    cardholder_name = request.form.get('cardholder_name')

    # Simulate payment processing
    if payment_method and cardholder_name:
        # Clear the cart after successful payment
        for item in cart_items:
            db.session.delete(item)
        db.session.commit()

        flash(f'Payment successful! Order placed using {payment_method} ending in {card_number}', 'success')
        return redirect(url_for('cart.order_confirmation'))
    else:
        flash('Payment failed. Please check your information and try again.', 'danger')
        return redirect(url_for('cart.checkout'))

@cart.route('/order-confirmation')
@login_required
def order_confirmation():
    return render_template('cart/confirmation.html', title='Order Confirmation')

@cart.route('/invoice/<order_id>')
@login_required
def generate_invoice(order_id):
    # In a real application, you would fetch order details from database
    # For now, we'll create a sample invoice
    user = current_user()
    
    invoice_data = {
        'order_id': order_id,
        'customer_name': user.username,
        'customer_email': user.email,
        'order_date': 'March 10, 2024',
        'order_items': [
            {
                'name': 'Sample Product 1',
                'quantity': 2,
                'price': 29.99,
                'total': 59.98
            },
            {
                'name': 'Sample Product 2',
                'quantity': 1,
                'price': 49.99,
                'total': 49.99
            }
        ],
        'subtotal': 109.97,
        'tax': 8.80,
        'total': 118.77,
        'payment_method': 'Credit Card ending in 1234',
        'shipping_address': '123 Main St, New York, NY 10001'
    }
    
    return render_template('cart/invoice.html', title='Invoice', invoice=invoice_data)

@cart.route('/invoice/<order_id>/pdf')
@login_required
def download_invoice_pdf(order_id):
    # Generate the same invoice data
    user = current_user()
    
    invoice_data = {
        'order_id': order_id,
        'customer_name': user.username,
        'customer_email': user.email,
        'order_date': 'March 10, 2024',
        'order_items': [
            {
                'name': 'Sample Product 1',
                'quantity': 2,
                'price': 29.99,
                'total': 59.98
            },
            {
                'name': 'Sample Product 2',
                'quantity': 1,
                'price': 49.99,
                'total': 49.99
            }
        ],
        'subtotal': 109.97,
        'tax': 8.80,
        'total': 118.77,
        'payment_method': 'Credit Card ending in 1234',
        'shipping_address': '123 Main St, New York, NY 10001'
    }
    
    # Generate PDF
    pdf_data = generate_invoice_pdf(invoice_data)
    
    # Create response
    response = make_response(pdf_data)
    response.headers['Content-Type'] = 'application/pdf'
    response.headers['Content-Disposition'] = f'attachment; filename=invoice_{order_id}.pdf'
    
    return response

@cart.route('/add/<int:product_id>', methods=['POST'])
@login_required
def add_to_cart(product_id):
    user = current_user()
    if user is None:
        flash('Please log in to add items to cart.', 'warning')
        return redirect(url_for('auth.login', next=request.url))
    
    product = Product.query.get_or_404(product_id)
    quantity = int(request.form.get('quantity', 1))
    size = request.form.get('size', 'M')

    if quantity > product.stock:
        flash('Not enough stock available', 'danger')
        return redirect(url_for('products.detail', product_id=product_id))

    # Get or create user's cart
    user_cart = Cart.query.filter_by(user_id=user.id).first()
    if not user_cart:
        user_cart = Cart(user_id=user.id)
        db.session.add(user_cart)
        db.session.commit()

    # Check if product and size already in cart
    cart_item = CartItem.query.filter_by(cart_id=user_cart.id, product_id=product_id, size=size).first()

    if cart_item:
        cart_item.quantity += quantity
    else:
        cart_item = CartItem(cart_id=user_cart.id, product_id=product_id, quantity=quantity, size=size)
        db.session.add(cart_item)

    db.session.commit()
    flash(f'Added {product.name} (Size: {size}) to cart', 'success')
    return redirect(url_for('cart.view_cart'))

@cart.route('/update/<int:item_id>', methods=['POST'])
@login_required
def update_quantity(item_id):
    user = current_user()
    if user is None:
        flash('Please log in to continue.', 'warning')
        return redirect(url_for('auth.login', next=request.url))
    
    cart_item = CartItem.query.get_or_404(item_id)

    # Ensure item belongs to current user
    user_cart = Cart.query.filter_by(user_id=user.id).first()
    if not user_cart or cart_item.cart_id != user_cart.id:
        flash('Unauthorized access', 'danger')
        return redirect(url_for('cart.view_cart'))

    new_quantity = int(request.form.get('quantity', 1))

    if new_quantity <= 0:
        db.session.delete(cart_item)
        flash('Item removed from cart', 'info')
    elif new_quantity > cart_item.product.stock:
        flash('Not enough stock available', 'danger')
    else:
        cart_item.quantity = new_quantity

    db.session.commit()
    return redirect(url_for('cart.view_cart'))

@cart.route('/remove/<int:item_id>')
@login_required
def remove_from_cart(item_id):
    user = current_user()
    if user is None:
        flash('Please log in to continue.', 'warning')
        return redirect(url_for('auth.login', next=request.url))
    
    cart_item = CartItem.query.get_or_404(item_id)

    # Ensure item belongs to current user
    user_cart = Cart.query.filter_by(user_id=user.id).first()
    if not user_cart or cart_item.cart_id != user_cart.id:
        flash('Unauthorized access', 'danger')
        return redirect(url_for('cart.view_cart'))

    db.session.delete(cart_item)
    db.session.commit()
    flash('Item removed from cart', 'info')
    return redirect(url_for('cart.view_cart'))

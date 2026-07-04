from app import create_app, db
from models import User, Category, Product, Cart, CartItem, Order, OrderItem, Payment, Address, Review, Wishlist
from werkzeug.security import generate_password_hash
from sqlalchemy import text

def test_database_connection():
    """Test database connection and populate with sample data"""
    app = create_app()
    
    with app.app_context():
        try:
            # Test database connection
            print("[INFO] Testing database connection...")
            db.session.execute(text("SELECT 1"))
            print("[SUCCESS] Database connection successful!")
            
            # Check if tables exist
            inspector = db.inspect(db.engine)
            tables = inspector.get_table_names()
            print(f"[INFO] Found {len(tables)} tables: {sorted(tables)}")
            
            # Check if we have any data
            user_count = User.query.count()
            category_count = Category.query.count()
            product_count = Product.query.count()
            
            print(f"\n[INFO] Current data counts:")
            print(f"   Users: {user_count}")
            print(f"   Categories: {category_count}")
            print(f"   Products: {product_count}")
            
            # Add sample data if tables are empty
            if user_count == 0:
                print("\n[INFO] Adding sample data...")
                add_sample_data()
                print("[SUCCESS] Sample data added successfully!")
            
            # Test queries
            print("\n[INFO] Testing database queries...")
            test_queries()
            
            print("\n[SUCCESS] Database is fully connected and ready!")
            
        except Exception as e:
            print(f"[ERROR] Database connection failed: {e}")

def add_sample_data():
    """Add sample data to the database"""
    
    # Create sample user
    sample_user = User(
        username='testuser',
        email='test@example.com',
        password=generate_password_hash('password123'),
        is_admin=False
    )
    db.session.add(sample_user)
    
    # Create categories
    categories = [
        Category(name='T-Shirts', gender='men', description='Men\'s T-Shirts'),
        Category(name='Shirts', gender='men', description='Men\'s Shirts'),
        Category(name='Dresses', gender='women', description='Women\'s Dresses'),
        Category(name='Tops', gender='women', description='Women\'s Tops'),
        Category(name='Toys', gender='kids', description='Kids Toys'),
        Category(name='Clothing', gender='kids', description='Kids Clothing')
    ]
    
    for category in categories:
        db.session.add(category)
    
    db.session.commit()  # Commit to get category IDs
    
    # Create sample products
    products = [
        Product(
            name='Men\'s Blue T-Shirt',
            description='Comfortable blue cotton t-shirt for men',
            price=29.99,
            stock=50,
            category_id=categories[0].id,
            image_file='mens_blue_tshirt.jpg'
        ),
        Product(
            name='Women\'s Red Dress',
            description='Elegant red dress for women',
            price=89.99,
            stock=25,
            category_id=categories[2].id,
            image_file='womens_red_dress.jpg'
        ),
        Product(
            name='Kids Toy Car',
            description='Fun toy car for kids',
            price=19.99,
            stock=100,
            category_id=categories[4].id,
            image_file='kids_toy_car.jpg'
        )
    ]
    
    for product in products:
        db.session.add(product)
    
    db.session.commit()

def test_queries():
    """Test various database queries"""
    
    # Test user query
    users = User.query.all()
    print(f"   Found {len(users)} users")
    
    # Test category query
    men_categories = Category.query.filter_by(gender='men').all()
    women_categories = Category.query.filter_by(gender='women').all()
    kids_categories = Category.query.filter_by(gender='kids').all()
    
    print(f"   Men categories: {len(men_categories)}")
    print(f"   Women categories: {len(women_categories)}")
    print(f"   Kids categories: {len(kids_categories)}")
    
    # Test product query
    products = Product.query.all()
    print(f"   Total products: {len(products)}")
    
    # Test product with category relationship
    for product in products[:3]:  # Show first 3 products
        print(f"   - {product.name} (${product.price}) - {product.category.name}")

if __name__ == "__main__":
    test_database_connection()

from app import create_app, db
from models import User, Category, Product, Cart, CartItem, Order, OrderItem, Payment, Address, Review, Wishlist

def clean_create_tables():
    """Drop all tables and recreate exactly 11 tables"""
    app = create_app()
    
    with app.app_context():
        print("Dropping all existing tables...")
        db.drop_all()
        
        print("Creating exactly 11 database tables...")
        db.create_all()
        
        print("All tables created successfully!")
        
        # List all tables
        inspector = db.inspect(db.engine)
        tables = inspector.get_table_names()
        
        print(f"\nTotal tables created: {len(tables)}")
        print("Tables:")
        for i, table in enumerate(sorted(tables), 1):
            print(f"{i}. {table}")
        
        print(f"\nExpected 11 tables, got {len(tables)} tables.")
        
        # Verify we have exactly the expected tables
        expected_tables = {
            'address', 'cart', 'cart_item', 'category', 
            'order', 'order_item', 'payment', 'product', 
            'review', 'user', 'wishlist'
        }
        
        actual_tables = set(tables)
        
        if expected_tables == actual_tables:
            print("✅ Perfect! Exactly 11 tables created as expected.")
        else:
            print("❌ Table mismatch:")
            print(f"Expected: {expected_tables}")
            print(f"Actual: {actual_tables}")
            missing = expected_tables - actual_tables
            extra = actual_tables - expected_tables
            if missing:
                print(f"Missing: {missing}")
            if extra:
                print(f"Extra: {extra}")

if __name__ == "__main__":
    clean_create_tables()

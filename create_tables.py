from app import create_app, db
from models import User, Category, Product, Cart, CartItem, Order, OrderItem, Payment, Address, Review, Wishlist

def create_all_tables():
    """Create all database tables"""
    app = create_app()
    
    with app.app_context():
        print("Creating all database tables...")
        
        # Drop all tables first (optional - uncomment if you want to start fresh)
        # db.drop_all()
        
        # Create all tables
        db.create_all()
        
        print("All tables created successfully!")
        
        # List all tables
        inspector = db.inspect(db.engine)
        tables = inspector.get_table_names()
        
        print(f"\nTotal tables created: {len(tables)}")
        print("Tables:")
        for i, table in enumerate(tables, 1):
            print(f"{i}. {table}")
        
        print(f"\nExpected 11 tables, got {len(tables)} tables.")

if __name__ == "__main__":
    create_all_tables()

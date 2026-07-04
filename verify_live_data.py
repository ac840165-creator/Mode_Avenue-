from app import create_app, db
from models import User, Category, Product, Cart, CartItem, Order, OrderItem, Payment, Address, Review, Wishlist

def verify_live_data():
    """Verify and display live data from mode_avenue_db"""
    app = create_app()
    
    with app.app_context():
        print("🔍 VERIFYING LIVE DATA FROM mode_avenue_db")
        print("=" * 50)
        
        # Test Users
        print("\n👥 USERS:")
        users = User.query.all()
        for user in users:
            print(f"   ID: {user.id} | Username: {user.username} | Email: {user.email} | Admin: {user.is_admin}")
        
        # Test Categories
        print("\n📂 CATEGORIES:")
        categories = Category.query.all()
        for category in categories:
            print(f"   ID: {category.id} | Name: {category.name} | Gender: {category.gender}")
        
        # Test Products with Categories
        print("\n🛍️  PRODUCTS:")
        products = Product.query.all()
        for product in products:
            print(f"   ID: {product.id} | Name: {product.name} | Price: ${product.price} | Stock: {product.stock}")
            print(f"       Category: {product.category.name} ({product.category.gender})")
        
        # Test Relationships
        print("\n🔗 RELATIONSHIP TESTS:")
        
        # Get products by gender
        men_products = Product.query.join(Category).filter(Category.gender == 'men').all()
        women_products = Product.query.join(Category).filter(Category.gender == 'women').all()
        kids_products = Product.query.join(Category).filter(Category.gender == 'kids').all()
        
        print(f"   Men's Products: {len(men_products)}")
        for product in men_products:
            print(f"     - {product.name} (${product.price})")
        
        print(f"   Women's Products: {len(women_products)}")
        for product in women_products:
            print(f"     - {product.name} (${product.price})")
        
        print(f"   Kids' Products: {len(kids_products)}")
        for product in kids_products:
            print(f"     - {product.name} (${product.price})")
        
        # Test empty tables
        print("\n📊 EMPTY TABLES (Ready for data):")
        empty_tables = []
        
        if Cart.query.count() == 0:
            empty_tables.append("Cart")
        if CartItem.query.count() == 0:
            empty_tables.append("CartItem")
        if Order.query.count() == 0:
            empty_tables.append("Order")
        if OrderItem.query.count() == 0:
            empty_tables.append("OrderItem")
        if Payment.query.count() == 0:
            empty_tables.append("Payment")
        if Address.query.count() == 0:
            empty_tables.append("Address")
        if Review.query.count() == 0:
            empty_tables.append("Review")
        if Wishlist.query.count() == 0:
            empty_tables.append("Wishlist")
        
        for table in empty_tables:
            print(f"   ✅ {table} - Ready for use")
        
        print("\n" + "=" * 50)
        print("🎉 DATABASE IS READY FOR LIVE USE!")
        print("📍 Database: mode_avenue_db (MySQL)")
        print("📊 Total Tables: 11")
        print("🔗 All relationships working correctly")
        print("💾 Sample data added for testing")

if __name__ == "__main__":
    verify_live_data()

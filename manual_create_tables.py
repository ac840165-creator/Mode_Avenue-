from app import create_app, db
from sqlalchemy import text

def manual_create_tables():
    """Manually create exactly 11 tables in MySQL database"""
    app = create_app()
    
    with app.app_context():
        # Drop all tables first
        print("Dropping all existing tables...")
        db.drop_all()
        
        # Execute raw SQL to create tables manually
        print("Creating tables manually...")
        
        # Create tables in specific order to respect foreign keys
        tables_sql = [
            # User table
            """
            CREATE TABLE user (
                id INT AUTO_INCREMENT PRIMARY KEY,
                username VARCHAR(20) UNIQUE NOT NULL,
                email VARCHAR(120) UNIQUE NOT NULL,
                password VARCHAR(60) NOT NULL,
                is_admin BOOLEAN DEFAULT FALSE
            )
            """,
            
            # Category table
            """
            CREATE TABLE category (
                id INT AUTO_INCREMENT PRIMARY KEY,
                name VARCHAR(50) NOT NULL,
                description TEXT,
                gender VARCHAR(10) NOT NULL
            )
            """,
            
            # Product table
            """
            CREATE TABLE product (
                id INT AUTO_INCREMENT PRIMARY KEY,
                name VARCHAR(100) NOT NULL,
                description TEXT NOT NULL,
                price FLOAT NOT NULL,
                image_file VARCHAR(20) DEFAULT 'default.jpg',
                stock INT DEFAULT 0,
                category_id INT NOT NULL,
                FOREIGN KEY (category_id) REFERENCES category(id)
            )
            """,
            
            # Cart table
            """
            CREATE TABLE cart (
                id INT AUTO_INCREMENT PRIMARY KEY,
                user_id INT NOT NULL,
                FOREIGN KEY (user_id) REFERENCES user(id)
            )
            """,
            
            # CartItem table
            """
            CREATE TABLE cart_item (
                id INT AUTO_INCREMENT PRIMARY KEY,
                cart_id INT NOT NULL,
                product_id INT NOT NULL,
                quantity INT DEFAULT 1,
                FOREIGN KEY (cart_id) REFERENCES cart(id),
                FOREIGN KEY (product_id) REFERENCES product(id)
            )
            """,
            
            # Order table
            """
            CREATE TABLE `order` (
                id INT AUTO_INCREMENT PRIMARY KEY,
                user_id INT NOT NULL,
                order_date DATETIME DEFAULT CURRENT_TIMESTAMP,
                total_amount FLOAT NOT NULL,
                status VARCHAR(20) DEFAULT 'pending',
                FOREIGN KEY (user_id) REFERENCES user(id)
            )
            """,
            
            # OrderItem table
            """
            CREATE TABLE order_item (
                id INT AUTO_INCREMENT PRIMARY KEY,
                order_id INT NOT NULL,
                product_id INT NOT NULL,
                quantity INT NOT NULL,
                price FLOAT NOT NULL,
                FOREIGN KEY (order_id) REFERENCES `order`(id),
                FOREIGN KEY (product_id) REFERENCES product(id)
            )
            """,
            
            # Payment table
            """
            CREATE TABLE payment (
                id INT AUTO_INCREMENT PRIMARY KEY,
                order_id INT NOT NULL,
                payment_method VARCHAR(50) NOT NULL,
                amount FLOAT NOT NULL,
                status VARCHAR(20) DEFAULT 'pending',
                transaction_id VARCHAR(100),
                payment_date DATETIME DEFAULT CURRENT_TIMESTAMP,
                FOREIGN KEY (order_id) REFERENCES `order`(id)
            )
            """,
            
            # Address table
            """
            CREATE TABLE address (
                id INT AUTO_INCREMENT PRIMARY KEY,
                user_id INT NOT NULL,
                street_address VARCHAR(200) NOT NULL,
                city VARCHAR(100) NOT NULL,
                state VARCHAR(100) NOT NULL,
                zip_code VARCHAR(20) NOT NULL,
                country VARCHAR(100) DEFAULT 'USA',
                is_default BOOLEAN DEFAULT FALSE,
                address_type VARCHAR(20) NOT NULL,
                FOREIGN KEY (user_id) REFERENCES user(id)
            )
            """,
            
            # Review table
            """
            CREATE TABLE review (
                id INT AUTO_INCREMENT PRIMARY KEY,
                product_id INT NOT NULL,
                user_id INT NOT NULL,
                rating INT NOT NULL,
                comment TEXT,
                review_date DATETIME DEFAULT CURRENT_TIMESTAMP,
                FOREIGN KEY (product_id) REFERENCES product(id),
                FOREIGN KEY (user_id) REFERENCES user(id)
            )
            """,
            
            # Wishlist table
            """
            CREATE TABLE wishlist (
                id INT AUTO_INCREMENT PRIMARY KEY,
                user_id INT NOT NULL,
                product_id INT NOT NULL,
                created_date DATETIME DEFAULT CURRENT_TIMESTAMP,
                FOREIGN KEY (user_id) REFERENCES user(id),
                FOREIGN KEY (product_id) REFERENCES product(id)
            )
            """
        ]
        
        # Execute each table creation
        for i, table_sql in enumerate(tables_sql, 1):
            try:
                db.session.execute(text(table_sql))
                print(f"✅ Created table {i}/11")
            except Exception as e:
                print(f"❌ Error creating table {i}: {e}")
        
        # Commit all changes
        db.session.commit()
        
        # Verify tables
        inspector = db.inspect(db.engine)
        tables = inspector.get_table_names()
        
        print(f"\n✅ Successfully created {len(tables)} tables:")
        for i, table in enumerate(sorted(tables), 1):
            print(f"{i}. {table}")
        
        print(f"\n🎯 Target: 11 tables | Created: {len(tables)} tables")
        
        if len(tables) == 11:
            print("🎉 Perfect! Exactly 11 tables created in mode_avenue_db database!")
        else:
            print(f"⚠️  Expected 11 tables but got {len(tables)}")

if __name__ == "__main__":
    manual_create_tables()

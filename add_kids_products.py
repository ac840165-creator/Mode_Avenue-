#!/usr/bin/env python3

"""
Script to add 10+ products to Kids collection categories: T-Shirts, Pants, Dresses, Shoes
"""

import os
from app import create_app
from models import db, Product, Category

def add_kids_products():
    app = create_app()
    with app.app_context():
        
        # Get kids categories
        kids_tshirts = Category.query.filter_by(name='T-Shirts', gender='kids').first()
        kids_pants = Category.query.filter_by(name='Pants', gender='kids').first()
        kids_dresses = Category.query.filter_by(name='Dresses', gender='kids').first()
        kids_shoes = Category.query.filter_by(name='Shoes', gender='kids').first()
        
        if not all([kids_tshirts, kids_pants, kids_dresses, kids_shoes]):
            print("❌ One or more kids categories not found!")
            print(f"T-Shirts: {kids_tshirts}")
            print(f"Pants: {kids_pants}")
            print(f"Dresses: {kids_dresses}")
            print(f"Shoes: {kids_shoes}")
            return
        
        print("✅ Found all kids categories")
        
        # Kids T-Shirts
        kids_tshirt_products = [
            {
                'name': 'Superhero Graphic T-Shirt',
                'description': 'Fun superhero graphic tee for kids. Made from soft cotton with vibrant colors.',
                'price': 14.99,
                'stock': 30,
                'image_file': 'superhero_graphic_tshirt.jpg'
            },
            {
                'name': 'Cartoon Character T-Shirt',
                'description': 'Kids favorite cartoon character printed on comfortable cotton tee.',
                'price': 12.99,
                'stock': 35,
                'image_file': 'cartoon_character_tshirt.jpg'
            },
            {
                'name': 'Sports Jersey T-Shirt',
                'description': 'Athletic-style jersey tee perfect for active kids. Breathable fabric.',
                'price': 16.99,
                'stock': 25,
                'image_file': 'sports_jersey_tshirt.jpg'
            },
            {
                'name': 'Animal Print T-Shirt',
                'description': 'Cute animal print design that kids will love. Soft and comfortable.',
                'price': 13.99,
                'stock': 28,
                'image_file': 'animal_print_tshirt.jpg'
            },
            {
                'name': 'Rainbow Striped T-Shirt',
                'description': 'Colorful rainbow striped tee that brightens up any day.',
                'price': 11.99,
                'stock': 32,
                'image_file': 'rainbow_striped_tshirt.jpg'
            },
            {
                'name': 'Dinosaur T-Shirt',
                'description': 'Cool dinosaur graphic tee for little explorers. Educational and fun.',
                'price': 14.99,
                'stock': 26,
                'image_file': 'dinosaur_tshirt.jpg'
            },
            {
                'name': 'Space Theme T-Shirt',
                'description': 'Outer space themed tee with planets and rockets. Inspires imagination.',
                'price': 15.99,
                'stock': 24,
                'image_file': 'space_theme_tshirt.jpg'
            },
            {
                'name': 'Polka Dot T-Shirt',
                'description': 'Classic polka dot pattern in bright colors. Timeless kids design.',
                'price': 12.99,
                'stock': 30,
                'image_file': 'polka_dot_tshirt.jpg'
            },
            {
                'name': 'School Spirit T-Shirt',
                'description': 'Show school pride with this fun spirit tee. Great for school events.',
                'price': 13.99,
                'stock': 22,
                'image_file': 'school_spirit_tshirt.jpg'
            },
            {
                'name': 'Tie-Dye T-Shirt',
                'description': 'Trendy tie-dye pattern that kids love. Each one is unique.',
                'price': 16.99,
                'stock': 20,
                'image_file': 'tie_dye_tshirt.jpg'
            },
            {
                'name': 'Construction Truck T-Shirt',
                'description': 'Construction vehicle graphics for kids who love big machines.',
                'price': 14.99,
                'stock': 25,
                'image_file': 'construction_truck_tshirt.jpg'
            },
            {
                'name': 'Unicorn T-Shirt',
                'description': 'Magical unicorn design with sparkly details. Perfect for dreamers.',
                'price': 15.99,
                'stock': 23,
                'image_file': 'unicorn_tshirt.jpg'
            }
        ]
        
        # Kids Pants
        kids_pants_products = [
            {
                'name': 'Denim Jeans',
                'description': 'Classic denim jeans for kids. Durable and comfortable for everyday wear.',
                'price': 24.99,
                'stock': 25,
                'image_file': 'denim_jeans.jpg'
            },
            {
                'name': 'Cargo Shorts',
                'description': 'Utility cargo shorts with multiple pockets. Perfect for adventures.',
                'price': 19.99,
                'stock': 30,
                'image_file': 'cargo_shorts.jpg'
            },
            {
                'name': 'Sweatpants',
                'description': 'Cozy sweatpants for lounging and play. Soft fleece lining.',
                'price': 17.99,
                'stock': 28,
                'image_file': 'sweatpants.jpg'
            },
            {
                'name': 'Khaki Pants',
                'description': 'Classic khaki pants for school and special occasions.',
                'price': 22.99,
                'stock': 20,
                'image_file': 'khaki_pants.jpg'
            },
            {
                'name': 'Leggings',
                'description': 'Stretchy leggings perfect for active kids. Comes in various colors.',
                'price': 14.99,
                'stock': 35,
                'image_file': 'leggings.jpg'
            },
            {
                'name': 'Athletic Shorts',
                'description': 'Lightweight athletic shorts for sports and outdoor activities.',
                'price': 16.99,
                'stock': 32,
                'image_file': 'athletic_shorts.jpg'
            },
            {
                'name': 'Jogger Pants',
                'description': 'Trendy jogger style pants with elastic cuffs. Comfortable and stylish.',
                'price': 21.99,
                'stock': 24,
                'image_file': 'jogger_pants.jpg'
            },
            {
                'name': 'Plaid Pants',
                'description': 'Classic plaid pattern pants for a preppy look.',
                'price': 23.99,
                'stock': 18,
                'image_file': 'plaid_pants.jpg'
            },
            {
                'name': 'Overalls',
                'description': 'Classic denim overalls that kids love. Adjustable straps.',
                'price': 26.99,
                'stock': 15,
                'image_file': 'overalls.jpg'
            },
            {
                'name': 'Track Pants',
                'description': 'Athletic track pants with side stripes. Sporty and comfortable.',
                'price': 19.99,
                'stock': 27,
                'image_file': 'track_pants.jpg'
            },
            {
                'name': 'Corduroy Pants',
                'description': 'Soft corduroy pants for cooler weather. Warm and durable.',
                'price': 25.99,
                'stock': 20,
                'image_file': 'corduroy_pants.jpg'
            },
            {
                'name': 'Yoga Pants',
                'description': 'Stretchy yoga pants for active kids. Comfortable for all activities.',
                'price': 18.99,
                'stock': 22,
                'image_file': 'yoga_pants.jpg'
            }
        ]
        
        # Kids Dresses
        kids_dress_products = [
            {
                'name': 'Princess Dress',
                'description': 'Beautiful princess dress with sparkle details. Perfect for special occasions.',
                'price': 29.99,
                'stock': 20,
                'image_file': 'princess_dress.jpg'
            },
            {
                'name': 'Floral Sundress',
                'description': 'Light floral sundress for sunny days. Comfortable and pretty.',
                'price': 24.99,
                'stock': 25,
                'image_file': 'floral_sundress.jpg'
            },
            {
                'name': 'Party Dress',
                'description': 'Elegant party dress for celebrations. Twirl-worthy design.',
                'price': 34.99,
                'stock': 15,
                'image_file': 'party_dress.jpg'
            },
            {
                'name': 'School Dress',
                'description': 'Simple and comfortable dress perfect for school days.',
                'price': 22.99,
                'stock': 22,
                'image_file': 'school_dress.jpg'
            },
            {
                'name': 'Holiday Dress',
                'description': 'Festive holiday dress with seasonal details. Picture-perfect.',
                'price': 32.99,
                'stock': 12,
                'image_file': 'holiday_dress.jpg'
            },
            {
                'name': 'Play Dress',
                'description': 'Durable play dress for everyday adventures. Stain-resistant fabric.',
                'price': 19.99,
                'stock': 30,
                'image_file': 'play_dress.jpg'
            },
            {
                'name': 'Tutu Dress',
                'description': 'Fun tutu dress for little dancers. Fluffy and fun.',
                'price': 26.99,
                'stock': 18,
                'image_file': 'tutu_dress.jpg'
            },
            {
                'name': 'Summer Dress',
                'description': 'Lightweight summer dress with bright colors. Breathable fabric.',
                'price': 21.99,
                'stock': 28,
                'image_file': 'summer_dress.jpg'
            },
            {
                'name': 'Birthday Dress',
                'description': 'Special birthday dress for their big day. Makes them feel special.',
                'price': 36.99,
                'stock': 10,
                'image_file': 'birthday_dress.jpg'
            },
            {
                'name': 'Cotton Dress',
                'description': 'Soft cotton dress for sensitive skin. All-day comfort.',
                'price': 23.99,
                'stock': 24,
                'image_file': 'cotton_dress.jpg'
            },
            {
                'name': 'Ruffled Dress',
                'description': 'Cute ruffled dress with playful details. Twirl-worthy fun.',
                'price': 27.99,
                'stock': 16,
                'image_file': 'ruffled_dress.jpg'
            },
            {
                'name': 'Denim Dress',
                'description': 'Stylish denim dress for a casual look. Durable and fashionable.',
                'price': 28.99,
                'stock': 19,
                'image_file': 'denim_dress.jpg'
            }
        ]
        
        # Kids Shoes
        kids_shoe_products = [
            {
                'name': 'Sneakers',
                'description': 'Comfortable sneakers for everyday wear. Non-slip soles.',
                'price': 29.99,
                'stock': 25,
                'image_file': 'sneakers.jpg'
            },
            {
                'name': 'Sandals',
                'description': 'Breathable sandals for summer fun. Adjustable straps.',
                'price': 19.99,
                'stock': 30,
                'image_file': 'sandals.jpg'
            },
            {
                'name': 'Rain Boots',
                'description': 'Waterproof rain boots for puddle jumping. Fun colors.',
                'price': 24.99,
                'stock': 20,
                'image_file': 'rain_boots.jpg'
            },
            {
                'name': 'Dress Shoes',
                'description': 'Elegant dress shoes for special occasions. Comfortable fit.',
                'price': 34.99,
                'stock': 15,
                'image_file': 'dress_shoes.jpg'
            },
            {
                'name': 'Athletic Shoes',
                'description': 'Performance athletic shoes for sports and active play.',
                'price': 39.99,
                'stock': 18,
                'image_file': 'athletic_shoes.jpg'
            },
            {
                'name': 'Light-Up Shoes',
                'description': 'Fun light-up shoes that flash with every step. Kids love them!',
                'price': 32.99,
                'stock': 22,
                'image_file': 'light_up_shoes.jpg'
            },
            {
                'name': 'Slip-On Shoes',
                'description': 'Easy slip-on shoes for independent dressing. No laces needed.',
                'price': 26.99,
                'stock': 28,
                'image_file': 'slip_on_shoes.jpg'
            },
            {
                'name': 'Winter Boots',
                'description': 'Warm winter boots with insulation. Keeps feet cozy in cold weather.',
                'price': 44.99,
                'stock': 12,
                'image_file': 'winter_boots.jpg'
            },
            {
                'name': 'Crocs Style Shoes',
                'description': 'Lightweight and easy to clean. Perfect for water activities.',
                'price': 22.99,
                'stock': 35,
                'image_file': 'crocs_style_shoes.jpg'
            },
            {
                'name': 'School Shoes',
                'description': 'Durable school shoes that withstand daily wear. Comfortable for long days.',
                'price': 31.99,
                'stock': 20,
                'image_file': 'school_shoes.jpg'
            },
            {
                'name': 'Character Shoes',
                'description': 'Fun shoes featuring favorite cartoon characters. Makes dressing fun.',
                'price': 27.99,
                'stock': 24,
                'image_file': 'character_shoes.jpg'
            },
            {
                'name': 'Running Shoes',
                'description': 'Lightweight running shoes for active kids. Good traction.',
                'price': 35.99,
                'stock': 16,
                'image_file': 'running_shoes.jpg'
            }
        ]
        
        # Function to add products to category
        def add_products_to_category(category, products, category_name):
            added_count = 0
            print(f"\n📦 Adding {category_name}...")
            
            for product_data in products:
                # Check if product already exists
                existing_product = Product.query.filter_by(name=product_data['name'], category_id=category.id).first()
                
                if existing_product:
                    print(f"⚠️  Product already exists: {product_data['name']}")
                    continue
                
                # Create new product
                new_product = Product(
                    name=product_data['name'],
                    description=product_data['description'],
                    price=product_data['price'],
                    stock=product_data['stock'],
                    image_file=product_data['image_file'],
                    category_id=category.id
                )
                
                db.session.add(new_product)
                added_count += 1
                print(f"✅ Added: {product_data['name']} - ${product_data['price']}")
            
            return added_count
        
        # Add products to each category
        tshirts_added = add_products_to_category(kids_tshirts, kids_tshirt_products, "Kids T-Shirts")
        pants_added = add_products_to_category(kids_pants, kids_pants_products, "Kids Pants")
        dresses_added = add_products_to_category(kids_dresses, kids_dress_products, "Kids Dresses")
        shoes_added = add_products_to_category(kids_shoes, kids_shoe_products, "Kids Shoes")
        
        # Commit changes to database
        total_added = tshirts_added + pants_added + dresses_added + shoes_added
        
        if total_added > 0:
            db.session.commit()
            print(f"\n🎉 Successfully added {total_added} new kids products!")
            print(f"   T-Shirts: {tshirts_added} new products")
            print(f"   Pants: {pants_added} new products")
            print(f"   Dresses: {dresses_added} new products")
            print(f"   Shoes: {shoes_added} new products")
        else:
            print("\n⚠️  No new kids products were added (they may already exist)")

if __name__ == '__main__':
    add_kids_products()

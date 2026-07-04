#!/usr/bin/env python3

"""
Comprehensive script to add men's shoes and all kids' products with proper images
"""

from app import create_app
from models import db, Product, Category

def add_products_to_category(category, products, category_name, gender):
    """Add products to a category with duplicate checking"""
    added_count = 0
    print(f"\n📦 Adding {gender.title()} {category_name}...")

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

def get_mens_shoes_products():
    """Men's shoes products data"""
    return [
        {
            'name': 'Classic Leather Loafers',
            'description': 'Premium leather loafers with comfortable fit and timeless style. Perfect for business casual and formal occasions.',
            'price': 89.99,
            'stock': 25,
            'image_file': 'mens_shoes_classic_leather_loafers_1.jpg'
        },
        {
            'name': 'Running Athletic Shoes',
            'description': 'High-performance running shoes with advanced cushioning and breathable mesh upper for maximum comfort during workouts.',
            'price': 129.99,
            'stock': 30,
            'image_file': 'mens_shoes_running_athletic_shoes_2.jpg'
        },
        {
            'name': 'Casual Canvas Sneakers',
            'description': 'Stylish canvas sneakers with rubber sole for everyday wear. Lightweight and comfortable for all-day comfort.',
            'price': 59.99,
            'stock': 40,
            'image_file': 'mens_shoes_casual_canvas_sneakers_3.jpg'
        },
        {
            'name': 'Formal Oxford Shoes',
            'description': 'Elegant oxford shoes crafted from genuine leather. The perfect choice for weddings, business meetings, and formal events.',
            'price': 119.99,
            'stock': 20,
            'image_file': 'mens_shoes_formal_oxford_shoes_4.jpg'
        },
        {
            'name': 'Hiking Boots',
            'description': 'Durable hiking boots with waterproof membrane and rugged sole. Designed for outdoor adventures and rough terrain.',
            'price': 149.99,
            'stock': 15,
            'image_file': 'mens_shoes_hiking_boots_5.jpg'
        },
        {
            'name': 'Slip-On Casual Shoes',
            'description': 'Easy-to-wear slip-on shoes with elastic panels. Comfortable and stylish for casual outings and office wear.',
            'price': 79.99,
            'stock': 35,
            'image_file': 'mens_shoes_slip_on_casual_shoes_6.jpg'
        },
        {
            'name': 'Basketball High-Tops',
            'description': 'Professional basketball shoes with ankle support and traction pattern. Built for performance on the court.',
            'price': 139.99,
            'stock': 18,
            'image_file': 'mens_shoes_basketball_high_tops_7.jpg'
        },
        {
            'name': 'Boat Shoes',
            'description': 'Classic boat shoes with non-slip rubber sole. Perfect for boating, sailing, and casual summer activities.',
            'price': 99.99,
            'stock': 28,
            'image_file': 'mens_shoes_boat_shoes_8.jpg'
        },
        {
            'name': 'Chelsea Boots',
            'description': 'Timeless Chelsea boots with elastic side panels. Versatile footwear that pairs well with jeans or trousers.',
            'price': 134.99,
            'stock': 22,
            'image_file': 'mens_shoes_chelsea_boots_9.jpg'
        },
        {
            'name': 'Sandals',
            'description': 'Comfortable leather sandals with adjustable straps. Ideal for warm weather and casual summer styling.',
            'price': 69.99,
            'stock': 45,
            'image_file': 'mens_shoes_sandals_10.jpg'
        }
    ]

def get_kids_tshirts_products():
    """Kids' T-shirts products data"""
    return [
        {
            'name': 'Superhero Graphic T-Shirt',
            'description': 'Fun graphic t-shirt featuring popular superhero designs. Made from soft cotton for all-day comfort and play.',
            'price': 14.99,
            'stock': 50,
            'image_file': 'kids_tshirts_superhero_graphic_t_shirt_1.jpg'
        },
        {
            'name': 'Cartoon Character T-Shirt',
            'description': 'Colorful t-shirt with beloved cartoon character prints. Perfect for school, playdates, and everyday wear.',
            'price': 13.99,
            'stock': 45,
            'image_file': 'kids_tshirts_cartoon_character_t_shirt_2.jpg'
        },
        {
            'name': 'Sports Jersey T-Shirt',
            'description': 'Athletic-inspired jersey t-shirt with team colors and numbers. Great for sports fans and active kids.',
            'price': 16.99,
            'stock': 40,
            'image_file': 'kids_tshirts_sports_jersey_t_shirt_3.jpg'
        },
        {
            'name': 'Animal Print T-Shirt',
            'description': 'Adorable animal-themed t-shirt with cute prints. Soft fabric perfect for sensitive skin.',
            'price': 12.99,
            'stock': 55,
            'image_file': 'kids_tshirts_animal_print_t_shirt_4.jpg'
        },
        {
            'name': 'Rainbow Striped T-Shirt',
            'description': 'Colorful striped t-shirt with rainbow patterns. Bright and cheerful design for happy kids.',
            'price': 15.99,
            'stock': 42,
            'image_file': 'kids_tshirts_rainbow_striped_t_shirt_5.jpg'
        },
        {
            'name': 'Dinosaur T-Shirt',
            'description': 'Cool dinosaur-themed t-shirt with prehistoric designs. Perfect for little explorers and dinosaur fans.',
            'price': 14.99,
            'stock': 38,
            'image_file': 'kids_tshirts_dinosaur_t_shirt_6.jpg'
        },
        {
            'name': 'Space Theme T-Shirt',
            'description': 'Out-of-this-world space-themed t-shirt with planets and stars. Ideal for young astronauts.',
            'price': 16.99,
            'stock': 35,
            'image_file': 'kids_tshirts_space_theme_t_shirt_7.jpg'
        },
        {
            'name': 'Polka Dot T-Shirt',
            'description': 'Classic polka dot t-shirt in fun colors. Versatile style that matches with any outfit.',
            'price': 13.99,
            'stock': 48,
            'image_file': 'kids_tshirts_polka_dot_t_shirt_8.jpg'
        },
        {
            'name': 'School Spirit T-Shirt',
            'description': 'School-themed t-shirt with fun slogans and designs. Great for school events and spirit days.',
            'price': 15.99,
            'stock': 52,
            'image_file': 'kids_tshirts_school_spirit_t_shirt_9.jpg'
        },
        {
            'name': 'Tie-Dye T-Shirt',
            'description': 'Vibrant tie-dye t-shirt with swirling colors. Express your child\'s creative and colorful personality.',
            'price': 17.99,
            'stock': 30,
            'image_file': 'kids_tshirts_tie_dye_t_shirt_10.jpg'
        }
    ]

def get_kids_pants_products():
    """Kids' pants products data"""
    return [
        {
            'name': 'Denim Jeans',
            'description': 'Classic denim jeans with comfortable fit and durable construction. Perfect for school and casual wear.',
            'price': 29.99,
            'stock': 35,
            'image_file': 'kids_pants_denim_jeans_1.jpg'
        },
        {
            'name': 'Cargo Shorts',
            'description': 'Fun cargo shorts with multiple pockets. Ideal for outdoor play and summer adventures.',
            'price': 24.99,
            'stock': 42,
            'image_file': 'kids_pants_cargo_shorts_2.jpg'
        },
        {
            'name': 'Sweatpants',
            'description': 'Cozy sweatpants made from soft fleece material. Perfect for lounging and cool weather activities.',
            'price': 22.99,
            'stock': 48,
            'image_file': 'kids_pants_sweatpants_3.jpg'
        },
        {
            'name': 'Khaki Pants',
            'description': 'Classic khaki pants for school and dressy occasions. Easy to care for and comfortable to wear.',
            'price': 26.99,
            'stock': 38,
            'image_file': 'kids_pants_khaki_pants_4.jpg'
        },
        {
            'name': 'Leggings',
            'description': 'Stretchy leggings in fun colors and patterns. Great for active kids and comfortable all-day wear.',
            'price': 19.99,
            'stock': 55,
            'image_file': 'kids_pants_leggings_5.jpg'
        },
        {
            'name': 'Athletic Shorts',
            'description': 'Breathable athletic shorts for sports and play. Moisture-wicking fabric keeps kids comfortable.',
            'price': 21.99,
            'stock': 44,
            'image_file': 'kids_pants_athletic_shorts_6.jpg'
        },
        {
            'name': 'Jogger Pants',
            'description': 'Comfortable jogger pants with elastic cuffs. Stylish and functional for everyday wear.',
            'price': 27.99,
            'stock': 36,
            'image_file': 'kids_pants_jogger_pants_7.jpg'
        },
        {
            'name': 'Plaid Pants',
            'description': 'Fun plaid pants in seasonal colors. Perfect for fall and winter wardrobes.',
            'price': 28.99,
            'stock': 32,
            'image_file': 'kids_pants_plaid_pants_8.jpg'
        },
        {
            'name': 'Overalls',
            'description': 'Adorable overalls with adjustable straps. Durable and practical for active children.',
            'price': 31.99,
            'stock': 28,
            'image_file': 'kids_pants_overalls_9.jpg'
        },
        {
            'name': 'Track Pants',
            'description': 'Sporty track pants with side stripes. Great for gym class and casual athletic wear.',
            'price': 25.99,
            'stock': 40,
            'image_file': 'kids_pants_track_pants_10.jpg'
        }
    ]

def get_kids_dresses_products():
    """Kids' dresses products data"""
    return [
        {
            'name': 'Princess Dress',
            'description': 'Magical princess dress with sparkly details. Perfect for dress-up, parties, and special occasions.',
            'price': 34.99,
            'stock': 25,
            'image_file': 'kids_dresses_princess_dress_1.jpg'
        },
        {
            'name': 'Floral Sundress',
            'description': 'Beautiful floral sundress for warm weather. Light and airy fabric perfect for spring and summer.',
            'price': 29.99,
            'stock': 35,
            'image_file': 'kids_dresses_floral_sundress_2.jpg'
        },
        {
            'name': 'School Dress',
            'description': 'Modest school dress in classic colors. Comfortable and appropriate for classroom settings.',
            'price': 27.99,
            'stock': 42,
            'image_file': 'kids_dresses_school_dress_3.jpg'
        },
        {
            'name': 'Holiday Dress',
            'description': 'Festive holiday dress with seasonal patterns. Perfect for Christmas, birthdays, and family celebrations.',
            'price': 36.99,
            'stock': 28,
            'image_file': 'kids_dresses_holiday_dress_4.jpg'
        },
        {
            'name': 'Play Dress',
            'description': 'Durable play dress designed for active girls. Stain-resistant fabric that holds up to rough play.',
            'price': 24.99,
            'stock': 48,
            'image_file': 'kids_dresses_play_dress_5.jpg'
        },
        {
            'name': 'Tutu Dress',
            'description': 'Fun tutu dress with tulle skirt. Perfect for dance recitals, parties, and ballet performances.',
            'price': 32.99,
            'stock': 30,
            'image_file': 'kids_dresses_tutu_dress_6.jpg'
        },
        {
            'name': 'Summer Dress',
            'description': 'Light summer dress in bright colors. Breezy and comfortable for hot summer days.',
            'price': 26.99,
            'stock': 40,
            'image_file': 'kids_dresses_summer_dress_7.jpg'
        },
        {
            'name': 'Birthday Dress',
            'description': 'Special birthday dress with celebration motifs. Makes any birthday extra memorable.',
            'price': 38.99,
            'stock': 22,
            'image_file': 'kids_dresses_birthday_dress_8.jpg'
        },
        {
            'name': 'Cotton Dress',
            'description': 'Soft cotton dress perfect for everyday wear. Gentle on skin and comfortable for all-day wear.',
            'price': 23.99,
            'stock': 50,
            'image_file': 'kids_dresses_cotton_dress_9.jpg'
        },
        {
            'name': 'Ruffled Dress',
            'description': 'Cute ruffled dress with feminine details. Perfect for photos, parties, and special events.',
            'price': 35.99,
            'stock': 32,
            'image_file': 'kids_dresses_ruffled_dress_10.jpg'
        }
    ]

def get_kids_shoes_products():
    """Kids' shoes products data"""
    return [
        {
            'name': 'Sandals',
            'description': 'Comfortable sandals with adjustable straps. Perfect for beach days and warm weather activities.',
            'price': 19.99,
            'stock': 60,
            'image_file': 'kids_shoes_sandals_1.jpg'
        },
        {
            'name': 'Rain Boots',
            'description': 'Fun rain boots with waterproof design. Keeps little feet dry during puddle jumping adventures.',
            'price': 29.99,
            'stock': 35,
            'image_file': 'kids_shoes_rain_boots_2.jpg'
        },
        {
            'name': 'Dress Shoes',
            'description': 'Polished dress shoes for special occasions. Comfortable and stylish for weddings and parties.',
            'price': 39.99,
            'stock': 25,
            'image_file': 'kids_shoes_dress_shoes_3.jpg'
        },
        {
            'name': 'Athletic Shoes',
            'description': 'High-performance athletic shoes for sports and play. Lightweight and supportive for active kids.',
            'price': 49.99,
            'stock': 40,
            'image_file': 'kids_shoes_athletic_shoes_4.jpg'
        },
        {
            'name': 'Light-Up Shoes',
            'description': 'Fun shoes with LED lights that light up with every step. Perfect for night walks and playtime.',
            'price': 34.99,
            'stock': 30,
            'image_file': 'kids_shoes_light_up_shoes_5.jpg'
        },
        {
            'name': 'Slip-On Shoes',
            'description': 'Easy-to-wear slip-on shoes with elastic panels. No-tie convenience for busy mornings.',
            'price': 24.99,
            'stock': 55,
            'image_file': 'kids_shoes_slip_on_shoes_6.jpg'
        },
        {
            'name': 'Winter Boots',
            'description': 'Warm winter boots with insulated lining. Keeps feet toasty during cold winter days.',
            'price': 44.99,
            'stock': 28,
            'image_file': 'kids_shoes_winter_boots_7.jpg'
        },
        {
            'name': 'Crocs Style Shoes',
            'description': 'Comfortable molded shoes inspired by Crocs. Lightweight and easy to clean for everyday wear.',
            'price': 31.99,
            'stock': 45,
            'image_file': 'kids_shoes_crocs_style_shoes_8.jpg'
        },
        {
            'name': 'School Shoes',
            'description': 'Durable school shoes designed for classroom wear. Comfortable and appropriate for school policies.',
            'price': 36.99,
            'stock': 38,
            'image_file': 'kids_shoes_school_shoes_9.jpg'
        },
        {
            'name': 'Character Shoes',
            'description': 'Fun shoes featuring popular character designs. Makes getting dressed an exciting adventure.',
            'price': 42.99,
            'stock': 32,
            'image_file': 'kids_shoes_character_shoes_10.jpg'
        }
    ]

def main():
    """Main function to add all products"""
    app = create_app()
    with app.app_context():
        print("🛍️ MODE AVENUE COMPREHENSIVE PRODUCT ADDITION")
        print("=" * 60)

        # Get categories
        mens_shoes_cat = Category.query.filter_by(name='Shoes', gender='men').first()
        kids_tshirts_cat = Category.query.filter_by(name='T-Shirts', gender='kids').first()
        kids_pants_cat = Category.query.filter_by(name='Pants', gender='kids').first()
        kids_dresses_cat = Category.query.filter_by(name='Dresses', gender='kids').first()
        kids_shoes_cat = Category.query.filter_by(name='Shoes', gender='kids').first()

        total_added = 0

        # Add Men's Shoes
        if mens_shoes_cat:
            mens_shoes_products = get_mens_shoes_products()
            added = add_products_to_category(mens_shoes_cat, mens_shoes_products, "Shoes", "men's")
            total_added += added

        # Add Kids' T-Shirts
        if kids_tshirts_cat:
            kids_tshirts_products = get_kids_tshirts_products()
            added = add_products_to_category(kids_tshirts_cat, kids_tshirts_products, "T-Shirts", "kids'")
            total_added += added

        # Add Kids' Pants
        if kids_pants_cat:
            kids_pants_products = get_kids_pants_products()
            added = add_products_to_category(kids_pants_cat, kids_pants_products, "Pants", "kids'")
            total_added += added

        # Add Kids' Dresses
        if kids_dresses_cat:
            kids_dresses_products = get_kids_dresses_products()
            added = add_products_to_category(kids_dresses_cat, kids_dresses_products, "Dresses", "kids'")
            total_added += added

        # Add Kids' Shoes
        if kids_shoes_cat:
            kids_shoes_products = get_kids_shoes_products()
            added = add_products_to_category(kids_shoes_cat, kids_shoes_products, "Shoes", "kids'")
            total_added += added

        # Save all changes
        if total_added > 0:
            db.session.commit()
            print(f"\n🎉 Successfully added {total_added} new products!")
            print("\n📊 Summary:")
            print(f"   Men's Shoes: 10 products")
            print(f"   Kids' T-Shirts: 10 products")
            print(f"   Kids' Pants: 10 products")
            print(f"   Kids' Dresses: 10 products")
            print(f"   Kids' Shoes: 10 products")
            print(f"   Total: {total_added} products")
        else:
            print("\n⚠️  No new products were added")

if __name__ == '__main__':
    main()

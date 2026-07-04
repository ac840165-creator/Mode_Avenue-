#!/usr/bin/env python3

"""
Script to add 10+ products to Women's Tops, Skirts, and Shoes categories
"""

import os
from app import create_app
from models import db, Product, Category

def add_womens_products():
    app = create_app()
    with app.app_context():
        
        # Get women categories
        womens_tops = Category.query.filter_by(name='Tops', gender='women').first()
        womens_skirts = Category.query.filter_by(name='Skirts', gender='women').first()
        womens_shoes = Category.query.filter_by(name='Shoes', gender='women').first()
        
        if not all([womens_tops, womens_skirts, womens_shoes]):
            print("❌ One or more women's categories not found!")
            print(f"Tops: {womens_tops}")
            print(f"Skirts: {womens_skirts}")
            print(f"Shoes: {womens_shoes}")
            return
        
        print("✅ Found all women's categories")
        
        # Women's Tops
        womens_tops_products = [
            {
                'name': 'Silk Blouse',
                'description': 'Elegant silk blouse with a modern cut. Perfect for office and evening wear.',
                'price': 59.99,
                'stock': 20,
                'image_file': 'silk_blouse.jpg'
            },
            {
                'name': 'Casual T-Shirt',
                'description': 'Comfortable cotton t-shirt for everyday wear. Soft and breathable fabric.',
                'price': 19.99,
                'stock': 35,
                'image_file': 'casual_t_shirt.jpg'
            },
            {
                'name': 'Button-Up Shirt',
                'description': 'Classic button-up shirt in crisp white. Versatile for any occasion.',
                'price': 39.99,
                'stock': 25,
                'image_file': 'button_up_shirt.jpg'
            },
            {
                'name': 'Tank Top',
                'description': 'Lightweight tank top for summer days. Perfect for layering.',
                'price': 16.99,
                'stock': 30,
                'image_file': 'tank_top.jpg'
            },
            {
                'name': 'Sweater',
                'description': 'Cozy knit sweater for cooler weather. Soft and warm.',
                'price': 49.99,
                'stock': 18,
                'image_file': 'sweater.jpg'
            },
            {
                'name': 'Crop Top',
                'description': 'Trendy crop top for a modern look. Perfect for high-waisted bottoms.',
                'price': 24.99,
                'stock': 22,
                'image_file': 'crop_top.jpg'
            },
            {
                'name': 'Blazer',
                'description': 'Professional blazer for business meetings. Structured fit.',
                'price': 79.99,
                'stock': 15,
                'image_file': 'blazer.jpg'
            },
            {
                'name': 'Cardigan',
                'description': 'Lightweight cardigan for layering. Open front design.',
                'price': 44.99,
                'stock': 20,
                'image_file': 'cardigan.jpg'
            },
            {
                'name': 'Hoodie',
                'description': 'Comfortable hoodie for casual weekends. Soft fleece lining.',
                'price': 34.99,
                'stock': 25,
                'image_file': 'hoodie.jpg'
            },
            {
                'name': 'Camisole',
                'description': 'Delicate camisole with lace details. Perfect for layering.',
                'price': 22.99,
                'stock': 28,
                'image_file': 'camisole.jpg'
            },
            {
                'name': 'Polo Shirt',
                'description': 'Classic polo shirt for a sporty look. Collared design.',
                'price': 29.99,
                'stock': 24,
                'image_file': 'polo_shirt.jpg'
            },
            {
                'name': 'Off-Shoulder Top',
                'description': 'Stylish off-shoulder top for a feminine look. Elastic neckline.',
                'price': 32.99,
                'stock': 19,
                'image_file': 'off_shoulder_top.jpg'
            }
        ]
        
        # Women's Skirts
        womens_skirts_products = [
            {
                'name': 'Pencil Skirt',
                'description': 'Classic pencil skirt for professional wear. Knee-length design.',
                'price': 44.99,
                'stock': 20,
                'image_file': 'pencil_skirt.jpg'
            },
            {
                'name': 'A-Line Skirt',
                'description': 'Flattering A-line skirt that suits all body types. Comfortable fit.',
                'price': 39.99,
                'stock': 22,
                'image_file': 'a_line_skirt.jpg'
            },
            {
                'name': 'Mini Skirt',
                'description': 'Trendy mini skirt for a bold look. Perfect for nights out.',
                'price': 34.99,
                'stock': 18,
                'image_file': 'mini_skirt.jpg'
            },
            {
                'name': 'Midi Skirt',
                'description': 'Elegant midi skirt for a sophisticated look. Versatile length.',
                'price': 42.99,
                'stock': 16,
                'image_file': 'midi_skirt.jpg'
            },
            {
                'name': 'Maxi Skirt',
                'description': 'Flowing maxi skirt for bohemian style. Long and elegant.',
                'price': 49.99,
                'stock': 15,
                'image_file': 'maxi_skirt.jpg'
            },
            {
                'name': 'Pleated Skirt',
                'description': 'Chic pleated skirt with textured details. Professional yet stylish.',
                'price': 46.99,
                'stock': 14,
                'image_file': 'pleated_skirt.jpg'
            },
            {
                'name': 'Denim Skirt',
                'description': 'Casual denim skirt for everyday wear. Durable and comfortable.',
                'price': 36.99,
                'stock': 20,
                'image_file': 'denim_skirt.jpg'
            },
            {
                'name': 'Wrap Skirt',
                'description': 'Versatile wrap skirt that adjusts to your size. Flattering fit.',
                'price': 38.99,
                'stock': 17,
                'image_file': 'wrap_skirt.jpg'
            },
            {
                'name': 'Tennis Skirt',
                'description': 'Athletic tennis skirt for active lifestyle. Built-in shorts.',
                'price': 32.99,
                'stock': 25,
                'image_file': 'tennis_skirt.jpg'
            },
            {
                'name': 'Leather Skirt',
                'description': 'Edgy leather skirt for a bold statement. Faux leather material.',
                'price': 54.99,
                'stock': 12,
                'image_file': 'leather_skirt.jpg'
            },
            {
                'name': 'Tiered Skirt',
                'description': 'Bohemian tiered skirt with multiple layers. Flowy design.',
                'price': 41.99,
                'stock': 18,
                'image_file': 'tiered_skirt.jpg'
            },
            {
                'name': 'High-Waisted Skirt',
                'description': 'Flattering high-waisted skirt for a vintage look. Comfortable fit.',
                'price': 43.99,
                'stock': 16,
                'image_file': 'high_waisted_skirt.jpg'
            }
        ]
        
        # Women's Shoes
        womens_shoes_products = [
            {
                'name': 'High Heels',
                'description': 'Elegant high heels for formal occasions. Stiletto design.',
                'price': 69.99,
                'stock': 15,
                'image_file': 'high_heels.jpg'
            },
            {
                'name': 'Flats',
                'description': 'Comfortable flats for everyday wear. Ballet-style design.',
                'price': 39.99,
                'stock': 25,
                'image_file': 'flats.jpg'
            },
            {
                'name': 'Sneakers',
                'description': 'Trendy sneakers for casual style. Comfortable cushioning.',
                'price': 59.99,
                'stock': 20,
                'image_file': 'sneakers.jpg'
            },
            {
                'name': 'Boots',
                'description': 'Stylish boots for fall and winter. Knee-high design.',
                'price': 89.99,
                'stock': 12,
                'image_file': 'boots.jpg'
            },
            {
                'name': 'Sandals',
                'description': 'Comfortable sandals for summer. Strappy design.',
                'price': 34.99,
                'stock': 30,
                'image_file': 'sandals.jpg'
            },
            {
                'name': 'Loafers',
                'description': 'Classic loafers for professional look. Slip-on style.',
                'price': 54.99,
                'stock': 18,
                'image_file': 'loafers.jpg'
            },
            {
                'name': 'Wedges',
                'description': 'Comfortable wedges for height without heels. Summer style.',
                'price': 49.99,
                'stock': 16,
                'image_file': 'wedges.jpg'
            },
            {
                'name': 'Pumps',
                'description': 'Classic pumps for office wear. Low heel design.',
                'price': 64.99,
                'stock': 14,
                'image_file': 'pumps.jpg'
            },
            {
                'name': 'Athletic Shoes',
                'description': 'Performance athletic shoes for workouts. Supportive design.',
                'price': 79.99,
                'stock': 20,
                'image_file': 'athletic_shoes.jpg'
            },
            {
                'name': 'Ankle Boots',
                'description': 'Chic ankle boots for versatile styling. Comfortable fit.',
                'price': 74.99,
                'stock': 15,
                'image_file': 'ankle_boots.jpg'
            },
            {
                'name': 'Espadrilles',
                'description': 'Casual espadrilles for summer comfort. Rope sole design.',
                'price': 44.99,
                'stock': 22,
                'image_file': 'espadrilles.jpg'
            },
            {
                'name': 'Platform Shoes',
                'description': 'Trendy platform shoes for added height. Comfortable sole.',
                'price': 56.99,
                'stock': 17,
                'image_file': 'platform_shoes.jpg'
            }
        ]
        
        # Function to add products to category
        def add_products_to_category(category, products, category_name):
            added_count = 0
            print(f"\n📦 Adding Women's {category_name}...")
            
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
        tops_added = add_products_to_category(womens_tops, womens_tops_products, "Tops")
        skirts_added = add_products_to_category(womens_skirts, womens_skirts_products, "Skirts")
        shoes_added = add_products_to_category(womens_shoes, womens_shoes_products, "Shoes")
        
        # Commit changes to database
        total_added = tops_added + skirts_added + shoes_added
        
        if total_added > 0:
            db.session.commit()
            print(f"\n🎉 Successfully added {total_added} new women's products!")
            print(f"   Tops: {tops_added} new products")
            print(f"   Skirts: {skirts_added} new products")
            print(f"   Shoes: {shoes_added} new products")
        else:
            print("\n⚠️  No new women's products were added (they may already exist)")

if __name__ == '__main__':
    add_womens_products()

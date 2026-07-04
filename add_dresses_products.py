#!/usr/bin/env python3

"""
Script to add 10+ products to Women's Dresses category
"""

import os
from app import create_app
from models import db, Product, Category

def add_dresses_products():
    app = create_app()
    with app.app_context():
        # Get the Dresses category for women
        dresses_category = Category.query.filter_by(name='Dresses', gender='women').first()
        
        if not dresses_category:
            print("❌ Dresses category for women not found!")
            return
        
        print(f"✅ Found Dresses category: {dresses_category.name}")
        
        # Define new dress products
        new_dresses = [
            {
                'name': 'Floral Summer Dress',
                'description': 'Light and breezy floral print dress perfect for summer days. Features a flattering A-line silhouette with adjustable straps.',
                'price': 49.99,
                'stock': 25,
                'image_file': 'floral_summer_dress.jpg'
            },
            {
                'name': 'Little Black Dress',
                'description': 'Classic little black dress that never goes out of style. Perfect for cocktail parties and special occasions.',
                'price': 89.99,
                'stock': 20,
                'image_file': 'little_black_dress.jpg'
            },
            {
                'name': 'Maxi Beach Dress',
                'description': 'Flowing maxi dress ideal for beach vacations and resort wear. Made from lightweight, breathable fabric.',
                'price': 64.99,
                'stock': 18,
                'image_file': 'maxi_beach_dress.jpg'
            },
            {
                'name': 'Cocktail Party Dress',
                'description': 'Elegant cocktail dress with sequin details and a form-fitting silhouette. Perfect for evening events.',
                'price': 119.99,
                'stock': 15,
                'image_file': 'cocktail_party_dress.jpg'
            },
            {
                'name': 'Business Casual Dress',
                'description': 'Professional yet stylish dress suitable for office wear. Features a modest cut and comfortable fit.',
                'price': 74.99,
                'stock': 22,
                'image_file': 'business_casual_dress.jpg'
            },
            {
                'name': 'Bohemian Sundress',
                'description': 'Free-spirited bohemian style sundress with intricate embroidery and fringe details. Perfect for festivals.',
                'price': 54.99,
                'stock': 20,
                'image_file': 'bohemian_sundress.jpg'
            },
            {
                'name': 'Wedding Guest Dress',
                'description': 'Elegant dress suitable for wedding guests. Features delicate lace details and a sophisticated design.',
                'price': 139.99,
                'stock': 12,
                'image_file': 'wedding_guest_dress.jpg'
            },
            {
                'name': 'Casual Day Dress',
                'description': 'Comfortable and versatile casual dress for everyday wear. Easy to dress up or down with accessories.',
                'price': 39.99,
                'stock': 30,
                'image_file': 'casual_day_dress.jpg'
            },
            {
                'name': 'Evening Gown',
                'description': 'Stunning evening gown for formal events and galas. Features luxurious fabric and elegant draping.',
                'price': 199.99,
                'stock': 8,
                'image_file': 'evening_gown.jpg'
            },
            {
                'name': 'Wrap Dress',
                'description': 'Classic wrap dress that flatters every body type. Versatile design suitable for various occasions.',
                'price': 69.99,
                'stock': 25,
                'image_file': 'wrap_dress.jpg'
            },
            {
                'name': 'Midi Dress',
                'description': 'Chic midi dress with a modern silhouette. Perfect for brunch dates and casual outings.',
                'price': 59.99,
                'stock': 20,
                'image_file': 'midi_dress.jpg'
            },
            {
                'name': 'Summer Sundress',
                'description': 'Bright and cheerful summer sundress with vibrant colors. Lightweight and comfortable for hot weather.',
                'price': 44.99,
                'stock': 28,
                'image_file': 'summer_sundress.jpg'
            }
        ]
        
        added_count = 0
        
        for dress_data in new_dresses:
            # Check if product already exists
            existing_product = Product.query.filter_by(name=dress_data['name'], category_id=dresses_category.id).first()
            
            if existing_product:
                print(f"⚠️  Product already exists: {dress_data['name']}")
                continue
            
            # Create new product
            new_product = Product(
                name=dress_data['name'],
                description=dress_data['description'],
                price=dress_data['price'],
                stock=dress_data['stock'],
                image_file=dress_data['image_file'],
                category_id=dresses_category.id
            )
            
            db.session.add(new_product)
            added_count += 1
            print(f"✅ Added: {dress_data['name']} - ${dress_data['price']}")
        
        # Commit changes to database
        if added_count > 0:
            db.session.commit()
            print(f"\n🎉 Successfully added {added_count} new dresses to the collection!")
        else:
            print("\n⚠️  No new dresses were added (they may already exist)")

if __name__ == '__main__':
    add_dresses_products()

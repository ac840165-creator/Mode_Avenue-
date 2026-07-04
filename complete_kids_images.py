#!/usr/bin/env python3

"""
Complete kids image update for remaining products
"""

import os
import requests
from app import create_app
from models import db, Product, Category

def download_image(url, filename):
    """Download image from URL and save to static/images/"""
    try:
        response = requests.get(url, stream=True)
        response.raise_for_status()
        
        # Create static/images directory if it doesn't exist
        os.makedirs('static/images', exist_ok=True)
        
        filepath = os.path.join('static/images', filename)
        with open(filepath, 'wb') as f:
            for chunk in response.iter_content(chunk_size=8192):
                f.write(chunk)
        
        print(f"✅ Downloaded: {filename}")
        return True
    except Exception as e:
        print(f"❌ Failed to download {filename}: {e}")
        return False

def complete_kids_images():
    app = create_app()
    with app.app_context():
        
        # Get kids categories
        kids_categories = {
            'T-Shirts': Category.query.filter_by(name='T-Shirts', gender='kids').first(),
            'Pants': Category.query.filter_by(name='Pants', gender='kids').first(),
            'Dresses': Category.query.filter_by(name='Dresses', gender='kids').first(),
            'Shoes': Category.query.filter_by(name='Shoes', gender='kids').first()
        }
        
        # Working kids-friendly image URLs
        working_urls = [
            "https://images.unsplash.com/photo-1519452575417-564c1401ecc0?w=400&h=400&fit=crop&crop=center",
            "https://images.unsplash.com/photo-1606107557195-0e29a4b5b4aa?w=400&h=400&fit=crop&crop=center",
            "https://images.unsplash.com/photo-1549298916-b41d501d3772?w=400&h=400&fit=crop&crop=center",
            "https://images.unsplash.com/photo-1515372039744-b8f02a3ae446?w=400&h=400&fit=crop&crop=center",
            "https://images.unsplash.com/photo-1539008835657-9e8e9680c956?w=400&h=400&fit=crop&crop=center",
        ]
        
        total_updated = 0
        
        for category_name, category in kids_categories.items():
            if not category:
                print(f"❌ {category_name} category not found!")
                continue
                
            print(f"\n📦 Completing {category_name} images...")
            
            # Get products that still have default image names
            products_to_update = Product.query.filter_by(category_id=category.id).filter(
                Product.image_file.in_([
                    'superhero_graphic_tshirt.jpg', 'cartoon_character_tshirt.jpg', 'sports_jersey_tshirt.jpg',
                    'animal_print_tshirt.jpg', 'rainbow_striped_tshirt.jpg', 'dinosaur_tshirt.jpg',
                    'space_theme_tshirt.jpg', 'polka_dot_tshirt.jpg', 'school_spirit_tshirt.jpg',
                    'tie_dye_tshirt.jpg', 'construction_truck_tshirt.jpg', 'unicorn_tshirt.jpg',
                    'denim_jeans.jpg', 'cargo_shorts.jpg', 'sweatpants.jpg', 'khaki_pants.jpg',
                    'leggings.jpg', 'athletic_shorts.jpg', 'jogger_pants.jpg', 'plaid_pants.jpg',
                    'overalls.jpg', 'track_pants.jpg', 'corduroy_pants.jpg', 'yoga_pants.jpg',
                    'princess_dress.jpg', 'floral_sundress.jpg', 'party_dress.jpg', 'school_dress.jpg',
                    'holiday_dress.jpg', 'play_dress.jpg', 'tutu_dress.jpg', 'summer_dress.jpg',
                    'birthday_dress.jpg', 'cotton_dress.jpg', 'ruffled_dress.jpg', 'denim_dress.jpg',
                    'sneakers.jpg', 'sandals.jpg', 'rain_boots.jpg', 'dress_shoes.jpg',
                    'athletic_shoes.jpg', 'light_up_shoes.jpg', 'slip_on_shoes.jpg', 'winter_boots.jpg',
                    'crocs_style_shoes.jpg', 'school_shoes.jpg', 'character_shoes.jpg', 'running_shoes.jpg'
                ])
            ).all()
            
            if not products_to_update:
                print(f"✅ All {category_name} products already have custom images!")
                continue
            
            category_updated = 0
            
            for i, product in enumerate(products_to_update):
                # Use working image URLs
                image_url = working_urls[i % len(working_urls)]
                
                # Generate unique filename based on product name
                product_name_clean = product.name.lower().replace(' ', '_').replace('-', '_').replace('/', '_').replace('\\', '_')
                filename = f"kids_{product_name_clean}_{product.id}_final.jpg"
                
                # Download the image
                if download_image(image_url, filename):
                    # Update product in database
                    product.image_file = filename
                    category_updated += 1
                    total_updated += 1
                    print(f"📝 Updated: {product.name}")
        
        # Save changes to database
        if total_updated > 0:
            db.session.commit()
            print(f"\n🎉 Successfully updated {total_updated} remaining kids products!")
        else:
            print("\n✅ All kids products already have custom images!")

if __name__ == '__main__':
    complete_kids_images()

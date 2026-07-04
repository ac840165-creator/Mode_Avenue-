#!/usr/bin/env python3

"""
Complete dress image update for remaining products
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

def complete_dresses_images():
    app = create_app()
    with app.app_context():
        # Get the Dresses category
        dresses_category = Category.query.filter_by(name='Dresses', gender='women').first()
        
        if not dresses_category:
            print("❌ Dresses category not found!")
            return
        
        # Get dress products that still need images (default images)
        dress_products = Product.query.filter_by(category_id=dresses_category.id).filter(
            Product.image_file.in_(['floral_summer_dress.jpg', 'little_black_dress.jpg', 'maxi_beach_dress.jpg', 
                                  'cocktail_party_dress.jpg', 'business_casual_dress.jpg', 'bohemian_sundress.jpg',
                                  'wedding_guest_dress.jpg', 'casual_day_dress.jpg', 'evening_gown.jpg', 'wrap_dress.jpg',
                                  'midi_dress.jpg', 'summer_sundress.jpg'])
        ).all()
        
        if not dress_products:
            print("✅ All dress products have been updated with custom images!")
            return
        
        print(f"Found {len(dress_products)} dress products still needing image updates...")
        
        # Working fashion image URLs
        working_urls = [
            "https://images.unsplash.com/photo-1539008835657-9e8e9680c956?w=400&h=400&fit=crop&crop=center",
            "https://images.unsplash.com/photo-1515372039744-b8f02a3ae446?w=400&h=400&fit=crop&crop=center",
            "https://images.unsplash.com/photo-1496717675326-50322d0b2467?w=400&h=400&fit=crop&crop=center",
            "https://images.unsplash.com/photo-1483985988355-763728e1935b?w=400&h=400&fit=crop&crop=center",
            "https://images.unsplash.com/photo-1519452575417-564c1401ecc0?w=400&h=400&fit=crop&crop=center",
        ]
        
        updated_count = 0
        
        for i, product in enumerate(dress_products):
            # Use working image URLs
            image_url = working_urls[i % len(working_urls)]
            
            # Generate unique filename based on product name
            product_name_clean = product.name.lower().replace(' ', '_').replace('-', '_').replace('/', '_').replace('\\', '_')
            filename = f"{product_name_clean}_{product.id}_final.jpg"
            
            # Download the image
            if download_image(image_url, filename):
                # Update product in database
                product.image_file = filename
                updated_count += 1
                print(f"📝 Updated product: {product.name}")
        
        # Save changes to database
        if updated_count > 0:
            db.session.commit()
            print(f"\n🎉 Successfully updated {updated_count} remaining dress products!")
        else:
            print("\n⚠️  No dress products were updated")

if __name__ == '__main__':
    complete_dresses_images()

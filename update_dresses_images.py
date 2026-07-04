#!/usr/bin/env python3

"""
Script to download and update dress product images with professional fashion images
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

def update_dresses_images():
    app = create_app()
    with app.app_context():
        # Get the Dresses category
        dresses_category = Category.query.filter_by(name='Dresses', gender='women').first()
        
        if not dresses_category:
            print("❌ Dresses category not found!")
            return
        
        # Get all dress products
        dress_products = Product.query.filter_by(category_id=dresses_category.id).all()
        
        if not dress_products:
            print("❌ No dress products found!")
            return
        
        print(f"Found {len(dress_products)} dress products to update images for...")
        
        # Professional dress image URLs
        dress_image_urls = [
            "https://images.unsplash.com/photo-1539008835657-9e8e9680c956?w=400&h=400&fit=crop&crop=center",  # Floral dress
            "https://images.unsplash.com/photo-1515372039744-b8f02a3ae446?w=400&h=400&fit=crop&crop=center",  # Black dress
            "https://images.unsplash.com/photo-1496717675326-50322d0b2467?w=400&h=400&fit=crop&crop=center",  # Maxi dress
            "https://images.unsplash.com/photo-1483985988355-763728e1935b?w=400&h=400&fit=crop&crop=center",  # Cocktail dress
            "https://images.unsplash.com/photo-1519452575417-564c1401ecc0?w=400&h=400&fit=crop&crop=center",  # Business dress
            "https://images.unsplash.com/photo-1539008835657-9e8e9680c956?w=400&h=400&fit=crop&crop=center",  # Bohemian dress
            "https://images.unsplash.com/photo-1515372039744-b8f02a3ae446?w=400&h=400&fit=crop&crop=center",  # Wedding dress
            "https://images.unsplash.com/photo-1496717675326-50322d0b2467?w=400&h=400&fit=crop&crop=center",  # Casual dress
            "https://images.unsplash.com/photo-1483985988355-763728e1935b?w=400&h=400&fit=crop&crop=center",  # Evening gown
            "https://images.unsplash.com/photo-1519452575417-564c1401ecc0?w=400&h=400&fit=crop&crop=center",  # Wrap dress
            "https://images.unsplash.com/photo-1539008835657-9e8e9680c956?w=400&h=400&fit=crop&crop=center",  # Midi dress
            "https://images.unsplash.com/photo-1496717675326-50322d0b2467?w=400&h=400&fit=crop&crop=center",  # Summer dress
        ]
        
        updated_count = 0
        
        for i, product in enumerate(dress_products):
            # Use corresponding image URL (cycle if needed)
            image_url = dress_image_urls[i % len(dress_image_urls)]
            
            # Generate unique filename based on product name
            product_name_clean = product.name.lower().replace(' ', '_').replace('-', '_').replace('/', '_').replace('\\', '_')
            filename = f"{product_name_clean}_{product.id}.jpg"
            
            # Download the image
            if download_image(image_url, filename):
                # Update product in database
                product.image_file = filename
                updated_count += 1
                print(f"📝 Updated product: {product.name}")
        
        # Save changes to database
        if updated_count > 0:
            db.session.commit()
            print(f"\n🎉 Successfully updated {updated_count} dress products with new images!")
        else:
            print("\n⚠️  No dress products were updated")

if __name__ == '__main__':
    update_dresses_images()

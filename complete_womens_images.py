#!/usr/bin/env python3

"""
Complete women's image update for remaining failed products
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

def complete_womens_images():
    app = create_app()
    with app.app_context():
        
        # Get women categories
        womens_tops = Category.query.filter_by(name='Tops', gender='women').first()
        womens_skirts = Category.query.filter_by(name='Skirts', gender='women').first()
        womens_shoes = Category.query.filter_by(name='Shoes', gender='women').first()
        
        # Working women's fashion image URLs
        working_urls = [
            "https://images.unsplash.com/photo-1539008835657-9e8e9680c956?w=400&h=400&fit=crop&crop=center",
            "https://images.unsplash.com/photo-1515372039744-b8f02a3ae446?w=400&h=400&fit=crop&crop=center",
            "https://images.unsplash.com/photo-1483985988355-763728e1935b?w=400&h=400&fit=crop&crop=center",
            "https://images.unsplash.com/photo-1519452575417-564c1401ecc0?w=400&h=400&fit=crop&crop=center",
            "https://images.unsplash.com/photo-1460353581641-37baddab0fa2?w=400&h=400&fit=crop&crop=center",
        ]
        
        total_updated = 0
        
        # Update remaining Women's Tops
        if womens_tops:
            print(f"\n📦 Completing Women's Tops images...")
            
            tops_to_update = Product.query.filter_by(category_id=womens_tops.id).filter(
                Product.image_file.in_(['tank_top.jpg'])
            ).all()
            
            for i, product in enumerate(tops_to_update):
                image_url = working_urls[i % len(working_urls)]
                product_name_clean = product.name.lower().replace(' ', '_').replace('-', '_').replace('/', '_').replace('\\', '_')
                filename = f"womens_tops_{product_name_clean}_{product.id}_final.jpg"
                
                if download_image(image_url, filename):
                    product.image_file = filename
                    total_updated += 1
                    print(f"📝 Updated: {product.name}")
        
        # Update remaining Women's Skirts
        if womens_skirts:
            print(f"\n📦 Completing Women's Skirts images...")
            
            skirts_to_update = Product.query.filter_by(category_id=womens_skirts.id).filter(
                Product.image_file.in_(['mini_skirt.jpg'])
            ).all()
            
            for i, product in enumerate(skirts_to_update):
                image_url = working_urls[i % len(working_urls)]
                product_name_clean = product.name.lower().replace(' ', '_').replace('-', '_').replace('/', '_').replace('\\', '_')
                filename = f"womens_skirts_{product_name_clean}_{product.id}_final.jpg"
                
                if download_image(image_url, filename):
                    product.image_file = filename
                    total_updated += 1
                    print(f"📝 Updated: {product.name}")
        
        # Update remaining Women's Shoes
        if womens_shoes:
            print(f"\n📦 Completing Women's Shoes images...")
            
            shoes_to_update = Product.query.filter_by(category_id=womens_shoes.id).filter(
                Product.image_file.in_(['sneakers.jpg'])
            ).all()
            
            for i, product in enumerate(shoes_to_update):
                image_url = working_urls[i % len(working_urls)]
                product_name_clean = product.name.lower().replace(' ', '_').replace('-', '_').replace('/', '_').replace('\\', '_')
                filename = f"womens_shoes_{product_name_clean}_{product.id}_final.jpg"
                
                if download_image(image_url, filename):
                    product.image_file = filename
                    total_updated += 1
                    print(f"📝 Updated: {product.name}")
        
        # Save changes to database
        if total_updated > 0:
            db.session.commit()
            print(f"\n🎉 Successfully updated {total_updated} remaining women's products!")
        else:
            print("\n✅ All women's products already have custom images!")

if __name__ == '__main__':
    complete_womens_images()

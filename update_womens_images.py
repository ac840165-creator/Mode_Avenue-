#!/usr/bin/env python3

"""
Script to download and update women's product images with professional fashion images
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

def update_womens_images():
    app = create_app()
    with app.app_context():
        
        # Get women categories
        womens_tops = Category.query.filter_by(name='Tops', gender='women').first()
        womens_skirts = Category.query.filter_by(name='Skirts', gender='women').first()
        womens_shoes = Category.query.filter_by(name='Shoes', gender='women').first()
        
        # Women's fashion image URLs
        womens_image_urls = [
            "https://images.unsplash.com/photo-1539008835657-9e8e9680c956?w=400&h=400&fit=crop&crop=center",  # Women's elegant
            "https://images.unsplash.com/photo-1515372039744-b8f02a3ae446?w=400&h=400&fit=crop&crop=center",  # Women's dress
            "https://images.unsplash.com/photo-1496717675326-50322d0b2467?w=400&h=400&fit=crop&crop=center",  # Women's casual
            "https://images.unsplash.com/photo-1483985988355-763728e1935b?w=400&h=400&fit=crop&crop=center",  # Women's formal
            "https://images.unsplash.com/photo-1519452575417-564c1401ecc0?w=400&h=400&fit=crop&crop=center",  # Women's business
            "https://images.unsplash.com/photo-1460353581641-37baddab0fa2?w=400&h=400&fit=crop&crop=center",  # Women's shoes
            "https://images.unsplash.com/photo-1578632292335-df3abbb0d586?w=400&h=400&fit=crop&crop=center",  # Fashion model
            "https://images.unsplash.com/photo-1515886657613-9f3515b0c78f?w=400&h=400&fit=crop&crop=center",  # Style
            "https://images.unsplash.com/photo-1434389677669-e08b4cac3105?w=400&h=400&fit=crop&crop=center",  # Fashion
            "https://images.unsplash.com/photo-1507003211169-0a1dd7228f2d?w=400&h=400&fit=crop&crop=center",  # Portrait
            "https://images.unsplash.com/photo-1529626455594-4ff0802cfb7e?w=400&h=400&fit=crop&crop=center",  # Style
            "https://images.unsplash.com/photo-1490481651871-ab68de25d43d?w=400&h=400&fit=crop&crop=center",  # Fashion
            "https://images.unsplash.com/photo-1487412720507-e7ab37603c6f?w=400&h=400&fit=crop&crop=center",  # Professional
            "https://images.unsplash.com/photo-1501196354995-cbb51b654e0f?w=400&h=400&fit=crop&crop=center",  # Business
            "https://images.unsplash.com/photo-1571019613454-1cb2f99b2d8b?w=400&h=400&fit=crop&crop=center",  # Style
        ]
        
        total_updated = 0
        
        # Update Women's Tops
        if womens_tops:
            print(f"\n📦 Updating Women's Tops images...")
            
            # Get products that still have default image names
            tops_to_update = Product.query.filter_by(category_id=womens_tops.id).filter(
                Product.image_file.in_([
                    'silk_blouse.jpg', 'casual_t_shirt.jpg', 'button_up_shirt.jpg', 'tank_top.jpg',
                    'sweater.jpg', 'crop_top.jpg', 'blazer.jpg', 'cardigan.jpg', 'hoodie.jpg',
                    'camisole.jpg', 'polo_shirt.jpg', 'off_shoulder_top.jpg'
                ])
            ).all()
            
            for i, product in enumerate(tops_to_update):
                image_url = womens_image_urls[i % len(womens_image_urls)]
                product_name_clean = product.name.lower().replace(' ', '_').replace('-', '_').replace('/', '_').replace('\\', '_')
                filename = f"womens_tops_{product_name_clean}_{product.id}.jpg"
                
                if download_image(image_url, filename):
                    product.image_file = filename
                    total_updated += 1
                    print(f"📝 Updated: {product.name}")
        
        # Update Women's Skirts
        if womens_skirts:
            print(f"\n📦 Updating Women's Skirts images...")
            
            skirts_to_update = Product.query.filter_by(category_id=womens_skirts.id).filter(
                Product.image_file.in_([
                    'pencil_skirt.jpg', 'a_line_skirt.jpg', 'mini_skirt.jpg', 'midi_skirt.jpg',
                    'maxi_skirt.jpg', 'pleated_skirt.jpg', 'denim_skirt.jpg', 'wrap_skirt.jpg',
                    'tennis_skirt.jpg', 'leather_skirt.jpg', 'tiered_skirt.jpg', 'high_waisted_skirt.jpg'
                ])
            ).all()
            
            for i, product in enumerate(skirts_to_update):
                image_url = womens_image_urls[i % len(womens_image_urls)]
                product_name_clean = product.name.lower().replace(' ', '_').replace('-', '_').replace('/', '_').replace('\\', '_')
                filename = f"womens_skirts_{product_name_clean}_{product.id}.jpg"
                
                if download_image(image_url, filename):
                    product.image_file = filename
                    total_updated += 1
                    print(f"📝 Updated: {product.name}")
        
        # Update Women's Shoes
        if womens_shoes:
            print(f"\n📦 Updating Women's Shoes images...")
            
            shoes_to_update = Product.query.filter_by(category_id=womens_shoes.id).filter(
                Product.image_file.in_([
                    'high_heels.jpg', 'flats.jpg', 'sneakers.jpg', 'boots.jpg', 'sandals.jpg',
                    'loafers.jpg', 'wedges.jpg', 'pumps.jpg', 'athletic_shoes.jpg', 'ankle_boots.jpg',
                    'espadrilles.jpg', 'platform_shoes.jpg'
                ])
            ).all()
            
            for i, product in enumerate(shoes_to_update):
                image_url = womens_image_urls[i % len(womens_image_urls)]
                product_name_clean = product.name.lower().replace(' ', '_').replace('-', '_').replace('/', '_').replace('\\', '_')
                filename = f"womens_shoes_{product_name_clean}_{product.id}.jpg"
                
                if download_image(image_url, filename):
                    product.image_file = filename
                    total_updated += 1
                    print(f"📝 Updated: {product.name}")
        
        # Save changes to database
        if total_updated > 0:
            db.session.commit()
            print(f"\n🎉 Successfully updated {total_updated} women's products with new images!")
        else:
            print("\n⚠️  No women's products were updated")

if __name__ == '__main__':
    update_womens_images()

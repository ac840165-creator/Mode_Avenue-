#!/usr/bin/env python3

"""
Complete image repolishing and regeneration for ALL products in the database
"""

import os
import requests
from app import create_app
from models import db, Product

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

def repolish_all_images():
    app = create_app()
    with app.app_context():
        # Get ALL products in the database
        all_products = Product.query.all()
        
        if not all_products:
            print("❌ No products found in database!")
            return
        
        print(f"🎨 Found {len(all_products)} products to repolish images...")
        
        # Comprehensive collection of high-quality fashion image URLs
        fashion_image_urls = [
            # Men's Fashion
            "https://images.unsplash.com/photo-1620012253295-c15cc3e65df4?w=400&h=400&fit=crop&crop=center",  # Men's shirt
            "https://images.unsplash.com/photo-1596755094514-f87e34085b2c?w=400&h=400&fit=crop&crop=center",  # Men's casual
            "https://images.unsplash.com/photo-1602810318383-e386cc2a3ccf?w=400&h=400&fit=crop&crop=center",  # Men's style
            "https://images.unsplash.com/photo-1542272604-787c3835535d?w=400&h=400&fit=crop&crop=center",  # Men's pants
            "https://images.unsplash.com/photo-1594634311265-b0dc7dd2a1c4?w=400&h=400&fit=crop&crop=center",  # Men's fashion
            "https://images.unsplash.com/photo-1551488831-00ddcb6c6bd3?w=400&h=400&fit=crop&crop=center",  # Men's jacket
            "https://images.unsplash.com/photo-1551698618-1dfe5d97d256?w=400&h=400&fit=crop&crop=center",  # Men's coat
            "https://images.unsplash.com/photo-1591047139829-d91ecb626e6b?w=400&h=400&fit=crop&crop=center",  # Men's shoes
            "https://images.unsplash.com/photo-1576871335924-2e5d9f5b0d2f?w=400&h=400&fit=crop&crop=center",  # Men's formal
            "https://images.unsplash.com/photo-1608231387042-66d17730faf0?w=400&h=400&fit=crop&crop=center",  # Men's premium
            
            # Women's Fashion
            "https://images.unsplash.com/photo-1539008835657-9e8e9680c956?w=400&h=400&fit=crop&crop=center",  # Women's dress
            "https://images.unsplash.com/photo-1515372039744-b8f02a3ae446?w=400&h=400&fit=crop&crop=center",  # Women's elegant
            "https://images.unsplash.com/photo-1496717675326-50322d0b2467?w=400&h=400&fit=crop&crop=center",  # Women's casual
            "https://images.unsplash.com/photo-1483985988355-763728e1935b?w=400&h=400&fit=crop&crop=center",  # Women's formal
            "https://images.unsplash.com/photo-1519452575417-564c1401ecc0?w=400&h=400&fit=crop&crop=center",  # Women's business
            "https://images.unsplash.com/photo-1460353581641-37baddab0fa2?w=400&h=400&fit=crop&crop=center",  # Women's shoes
            
            # Kids Fashion
            "https://images.unsplash.com/photo-1519452575417-564c1401ecc0?w=400&h=400&fit=crop&crop=center",  # Kids clothing
            "https://images.unsplash.com/photo-1606107557195-0e29a4b5b4aa?w=400&h=400&fit=crop&crop=center",  # Kids shoes
            "https://images.unsplash.com/photo-1549298916-b41d501d3772?w=400&h=400&fit=crop&crop=center",  # Kids fashion
            
            # Additional Professional Fashion Images
            "https://images.unsplash.com/photo-1578632292335-df3abbb0d586?w=400&h=400&fit=crop&crop=center",  # Fashion model
            "https://images.unsplash.com/photo-1515886657613-9f3515b0c78f?w=400&h=400&fit=crop&crop=center",  # Style
            "https://images.unsplash.com/photo-1434389677669-e08b4cac3105?w=400&h=400&fit=crop&crop=center",  # Fashion
            "https://images.unsplash.com/photo-1507003211169-0a1dd7228f2d?w=400&h=400&fit=crop&crop=center",  # Portrait
            "https://images.unsplash.com/photo-1529626455594-4ff0802cfb7e?w=400&h=400&fit=crop&crop=center",  # Style
            "https://images.unsplash.com/photo-1490481651871-ab68de25d43d?w=400&h=400&fit=crop&crop=center",  # Fashion
            "https://images.unsplash.com/photo-1487412720507-e7ab37603c6f?w=400&h=400&fit=crop&crop=center",  # Professional
            "https://images.unsplash.com/photo-1501196354995-cbb51b654e0f?w=400&h=400&fit=crop&crop=center",  # Business
            "https://images.unsplash.com/photo-1571019613454-1cb2f99b2d8b?w=400&h=400&fit=crop&crop=center",  # Style
            "https://images.unsplash.com/photo-1507003211169-0a1dd7228f2d?w=400&h=400&fit=crop&crop=center",  # Fashion
        ]
        
        updated_count = 0
        failed_count = 0
        
        for i, product in enumerate(all_products):
            # Cycle through image URLs
            image_url = fashion_image_urls[i % len(fashion_image_urls)]
            
            # Generate unique filename based on product name and ID
            product_name_clean = product.name.lower().replace(' ', '_').replace('-', '_').replace('/', '_').replace('\\', '_').replace(',', '').replace('.', '').replace('!', '').replace('?', '')
            filename = f"repolished_{product_name_clean}_{product.id}.jpg"
            
            # Download the image
            if download_image(image_url, filename):
                # Update product in database
                product.image_file = filename
                updated_count += 1
                print(f"📝 Updated: {product.name}")
            else:
                failed_count += 1
                print(f"⚠️  Failed: {product.name}")
        
        # Save changes to database
        if updated_count > 0:
            db.session.commit()
            print(f"\n🎉 Successfully repolished {updated_count} products!")
            if failed_count > 0:
                print(f"⚠️  {failed_count} products failed to update")
        else:
            print("\n❌ No products were updated")

if __name__ == '__main__':
    repolish_all_images()

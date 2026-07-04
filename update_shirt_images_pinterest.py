#!/usr/bin/env python3

"""
Update specific shirt products with custom Pinterest images
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

def update_shirt_images():
    app = create_app()
    with app.app_context():
        
        # Define shirt products with their Pinterest URLs
        shirt_updates = [
            {
                'name': 'Classic White Shirt',
                'url': 'https://i.pinimg.com/control1/1200x/7d/8e/09/7d8e09b5c1dd0a2ffb7688a94a69deba.jpg',
                'filename': 'classic_white_shirt_pinterest.jpg'
            },
            {
                'name': 'Striped Oxford Shirt',
                'url': 'https://i.pinimg.com/1200x/78/b1/54/78b154e3fc62b72e1a86552c62173d71.jpg',
                'filename': 'striped_oxford_shirt_pinterest.jpg'
            },
            {
                'name': 'Denim Button-Down',
                'url': 'https://i.pinimg.com/736x/57/8c/7e/578c7e6b63071835e1ae9ae5cb9e1bff.jpg',
                'filename': 'denim_button_down_pinterest.jpg'
            },
            {
                'name': 'Linen Summer Shirt',
                'url': 'https://i.pinimg.com/1200x/c7/93/38/c7933891ea3d94886a94a902b64bc590.jpg',
                'filename': 'linen_summer_shirt_pinterest.jpg'
            },
            {
                'name': 'Black Dress Shirt',
                'url': 'https://i.pinimg.com/1200x/18/bd/93/18bd93694e1d729504b1cfea5ef5889b.jpg',
                'filename': 'black_dress_shirt_pinterest.jpg'
            },
            {
                'name': 'Plaid Flannel Shirt',
                'url': 'https://i.pinimg.com/1200x/85/e9/2e/85e92e682784286546d6b60996cc17ed.jpg',
                'filename': 'plaid_flannel_shirt_pinterest.jpg'
            },
            {
                'name': 'Slim Fit Polo',
                'url': 'https://i.pinimg.com/1200x/97/d8/4c/97d84c74dbcd46d961c55e66d0b9179e.jpg',
                'filename': 'slim_fit_polo_pinterest.jpg'
            },
            {
                'name': 'Hawaiian Print Shirt',
                'url': 'https://i.pinimg.com/1200x/d1/a1/32/d1a132264b3a3b6262c3e97702eed0b6.jpg',
                'filename': 'hawaiian_print_shirt_pinterest.jpg'
            },
            {
                'name': 'Chambray Shirt',
                'url': 'https://i.pinimg.com/1200x/8a/4b/ff/8a4bffe9bd59cf571984b4b9da315397.jpg',
                'filename': 'chambray_shirt_pinterest.jpg'
            },
            {
                'name': 'Henley Shirt',
                'url': 'https://i.pinimg.com/1200x/62/66/a7/6266a7469c0f0ef82eed819e31415acd.jpg',
                'filename': 'henley_shirt_pinterest.jpg'
            }
        ]
        
        updated_count = 0
        
        for shirt_data in shirt_updates:
            # Find the product by name
            product = Product.query.filter_by(name=shirt_data['name']).first()
            
            if not product:
                print(f"⚠️  Product not found: {shirt_data['name']}")
                continue
            
            # Download the image
            if download_image(shirt_data['url'], shirt_data['filename']):
                # Update product in database
                product.image_file = shirt_data['filename']
                updated_count += 1
                print(f"📝 Updated product: {shirt_data['name']}")
            else:
                print(f"❌ Failed to update: {shirt_data['name']}")
        
        # Save changes to database
        if updated_count > 0:
            db.session.commit()
            print(f"\n🎉 Successfully updated {updated_count} shirt products with Pinterest images!")
        else:
            print("\n⚠️  No shirt products were updated")

if __name__ == '__main__':
    update_shirt_images()

#!/usr/bin/env python3

"""
Create local placeholder images for all products to ensure they load properly
"""

import os
from PIL import Image, ImageDraw, ImageFont
from app import create_app
from models import db, Product

def create_placeholder_image(filename, text, color=(100, 150, 200)):
    """Create a simple placeholder image with text"""
    try:
        # Create image
        img = Image.new('RGB', (400, 400), color)
        draw = ImageDraw.Draw(img)
        
        # Add text
        try:
            # Try to use a larger font
            font = ImageFont.truetype("arial.ttf", 24)
        except:
            # Fallback to default font
            font = ImageFont.load_default()
        
        # Calculate text position (center)
        text_bbox = draw.textbbox((0, 0), text, font=font)
        text_width = text_bbox[2] - text_bbox[0]
        text_height = text_bbox[3] - text_bbox[1]
        
        x = (400 - text_width) // 2
        y = (400 - text_height) // 2
        
        # Draw text
        draw.text((x, y), text, fill=(255, 255, 255), font=font)
        
        # Save image
        os.makedirs('static/images', exist_ok=True)
        filepath = os.path.join('static/images', filename)
        img.save(filepath, 'JPEG', quality=85)
        
        print(f"✅ Created: {filename}")
        return True
        
    except Exception as e:
        print(f"❌ Failed to create {filename}: {e}")
        return False

def create_all_placeholder_images():
    """Create placeholder images for all products"""
    app = create_app()
    with app.app_context():
        
        # Get all products
        all_products = Product.query.all()
        
        if not all_products:
            print("❌ No products found in database!")
            return
        
        print(f"🎨 Creating placeholder images for {len(all_products)} products...")
        
        # Color schemes for different categories
        colors = {
            'men': [(70, 130, 180), (60, 120, 170), (50, 110, 160)],  # Blues
            'women': [(255, 105, 180), (255, 95, 170), (245, 85, 160)],  # Pinks
            'kids': [(50, 205, 50), (40, 195, 40), (30, 185, 40)]      # Greens
        }
        
        updated_count = 0
        
        for i, product in enumerate(all_products):
            # Generate filename
            product_name_clean = product.name.lower().replace(' ', '_').replace('-', '_').replace('/', '_').replace('\\', '_').replace(',', '').replace('.', '').replace('!', '').replace('?', '')
            filename = f"placeholder_{product_name_clean}_{product.id}.jpg"
            
            # Choose color based on category gender
            if hasattr(product.category, 'gender'):
                gender_colors = colors.get(product.category.gender, colors['men'])
                color = gender_colors[i % len(gender_colors)]
            else:
                color = colors['men'][0]
            
            # Create text (shortened if too long)
            text = product.name
            if len(text) > 20:
                text = text[:17] + "..."
            
            # Create placeholder image
            if create_placeholder_image(filename, text, color):
                # Update product in database
                product.image_file = filename
                updated_count += 1
                print(f"📝 Updated: {product.name}")
        
        # Save changes to database
        if updated_count > 0:
            db.session.commit()
            print(f"\n🎉 Successfully created {updated_count} placeholder images!")
        else:
            print("\n❌ No placeholder images were created")

def verify_images():
    """Verify that all images exist and are accessible"""
    app = create_app()
    with app.app_context():
        
        # Check all products
        all_products = Product.query.all()
        
        print("🔍 Verifying all product images...")
        
        missing_count = 0
        existing_count = 0
        
        for product in all_products:
            image_path = os.path.join('static/images', product.image_file)
            
            if os.path.exists(image_path):
                file_size = os.path.getsize(image_path)
                print(f"✅ {product.name}: {product.image_file} ({file_size} bytes)")
                existing_count += 1
            else:
                print(f"❌ {product.name}: {product.image_file} - MISSING")
                missing_count += 1
        
        print(f"\n📊 Summary:")
        print(f"   ✅ Existing images: {existing_count}")
        print(f"   ❌ Missing images: {missing_count}")
        print(f"   📈 Success rate: {(existing_count/len(all_products)*100):.1f}%")

if __name__ == '__main__':
    print("🎨 MODE AVENUE PLACEHOLDER IMAGE CREATOR")
    print("=" * 50)
    
    # Create placeholder images
    create_all_placeholder_images()
    
    print("\n" + "=" * 50)
    
    # Verify all images
    verify_images()

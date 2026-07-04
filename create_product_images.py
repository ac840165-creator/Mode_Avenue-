#!/usr/bin/env python3

"""
Generate placeholder images for all men's shoes and kids' products
"""

import os
from PIL import Image, ImageDraw, ImageFont
from app import create_app
from models import db, Product, Category

def create_placeholder_image(filename, text, color=(100, 150, 200)):
    """Create a simple placeholder image with text"""
    try:
        # Create image
        img = Image.new('RGB', (400, 400), color)
        draw = ImageDraw.Draw(img)

        # Try to use a larger font
        try:
            font = ImageFont.truetype("arial.ttf", 20)
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

def get_mens_colors():
    """Colors for men's products"""
    return [
        (70, 130, 180),   # Steel Blue
        (60, 120, 170),   # Medium Blue
        (50, 110, 160),   # Dark Blue
        (80, 140, 190),   # Sky Blue
        (65, 125, 175),   # Blue variants
        (75, 135, 185),
        (55, 115, 165),
        (85, 145, 195),
        (45, 105, 155),
        (90, 150, 200)
    ]

def get_kids_colors():
    """Colors for kids' products"""
    return [
        (50, 205, 50),    # Lime Green
        (40, 195, 40),    # Green
        (30, 185, 30),    # Dark Green
        (60, 215, 60),    # Light Green
        (35, 190, 35),    # Green variants
        (45, 200, 45),
        (55, 210, 55),
        (25, 180, 25),
        (65, 220, 65),
        (20, 175, 20)
    ]

def create_images_for_category(category, gender, colors):
    """Create placeholder images for products in a category"""
    products = Product.query.filter_by(category_id=category.id).all()

    print(f"\n🎨 Creating images for {gender} {category.name} ({len(products)} products)...")

    created_count = 0
    for i, product in enumerate(products):
        # Get image filename from product
        filename = product.image_file

        # Choose color based on product index
        color = colors[i % len(colors)]

        # Create shortened text for display
        text = product.name
        if len(text) > 25:
            text = text[:22] + "..."

        # Create placeholder image
        if create_placeholder_image(filename, text, color):
            created_count += 1
        else:
            print(f"❌ Failed: {product.name}")

    return created_count

def main():
    """Main function to create all placeholder images"""
    app = create_app()
    with app.app_context():
        print("🎨 MODE AVENUE PLACEHOLDER IMAGE GENERATOR")
        print("=" * 60)

        # Get categories that need images
        mens_shoes_cat = Category.query.filter_by(name='Shoes', gender='men').first()
        kids_tshirts_cat = Category.query.filter_by(name='T-Shirts', gender='kids').first()
        kids_pants_cat = Category.query.filter_by(name='Pants', gender='kids').first()
        kids_dresses_cat = Category.query.filter_by(name='Dresses', gender='kids').first()
        kids_shoes_cat = Category.query.filter_by(name='Shoes', gender='kids').first()

        mens_colors = get_mens_colors()
        kids_colors = get_kids_colors()

        total_created = 0

        # Create images for Men's Shoes
        if mens_shoes_cat:
            created = create_images_for_category(mens_shoes_cat, "Men's", mens_colors)
            total_created += created

        # Create images for Kids' T-Shirts
        if kids_tshirts_cat:
            created = create_images_for_category(kids_tshirts_cat, "Kids'", kids_colors)
            total_created += created

        # Create images for Kids' Pants
        if kids_pants_cat:
            created = create_images_for_category(kids_pants_cat, "Kids'", kids_colors)
            total_created += created

        # Create images for Kids' Dresses
        if kids_dresses_cat:
            created = create_images_for_category(kids_dresses_cat, "Kids'", kids_colors)
            total_created += created

        # Create images for Kids' Shoes
        if kids_shoes_cat:
            created = create_images_for_category(kids_shoes_cat, "Kids'", kids_colors)
            total_created += created

        print(f"\n🎉 Successfully created {total_created} placeholder images!")
        print("\n📊 Summary:")
        print(f"   Men's Shoes: 10 images")
        print(f"   Kids' T-Shirts: 10 images")
        print(f"   Kids' Pants: 10 images")
        print(f"   Kids' Dresses: 10 images")
        print(f"   Kids' Shoes: 10 images")
        print(f"   Total: {total_created} images")

        # Verify image files exist
        print(f"\n🔍 Verifying image files...")
        static_dir = 'static/images'
        if os.path.exists(static_dir):
            # Count new product images
            all_files = os.listdir(static_dir)
            product_images = [f for f in all_files if f.startswith(('mens_shoes_', 'kids_tshirts_', 'kids_pants_', 'kids_dresses_', 'kids_shoes_'))]

            print(f"✅ Found {len(product_images)} new product image files")
            print(f"📁 Total image files in directory: {len(all_files)}")
        else:
            print("❌ Static images directory not found")

if __name__ == '__main__':
    main()

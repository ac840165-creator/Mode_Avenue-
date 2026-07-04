from PIL import Image, ImageDraw, ImageFont
import os

# Create a simple placeholder image
def create_default_image():
    # Create a gray background image
    width, height = 400, 300
    image = Image.new('RGB', (width, height), color='#E0E0E0')
    draw = ImageDraw.Draw(image)
    
    # Add a border
    border_color = '#999999'
    border_width = 2
    draw.rectangle([border_width, border_width, width-border_width, height-border_width], outline=border_color, width=border_width)
    
    # Add text
    text = "No Image"
    try:
        font = ImageFont.truetype("arial.ttf", 36)
    except:
        font = ImageFont.load_default()
    
    # Get text size and position it in center
    bbox = draw.textbbox((0, 0), text, font=font)
    text_width = bbox[2] - bbox[0]
    text_height = bbox[3] - bbox[1]
    x = (width - text_width) // 2
    y = (height - text_height) // 2
    
    # Draw text
    draw.text((x, y), text, fill='#666666', font=font)
    
    # Save image
    image_dir = 'c:/Users/ajay.chaudhari/Desktop/Mode_Avenue/static/images'
    os.makedirs(image_dir, exist_ok=True)
    image_path = os.path.join(image_dir, 'default-product.jpg')
    image.save(image_path, 'JPEG')
    print(f"✅ Created default product image at: {image_path}")

if __name__ == "__main__":
    create_default_image()

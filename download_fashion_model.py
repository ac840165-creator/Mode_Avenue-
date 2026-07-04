#!/usr/bin/env python3

"""
Download and add fashion model image to homepage
"""

import os
import requests
from app import create_app

def download_image(url, filename):
    """Download image from URL with proper headers"""
    try:
        # Add proper headers to mimic browser request
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36',
            'Accept': 'image/webp,image/apng,image/*,*/*;q=0.8',
            'Accept-Language': 'en-US,en;q=0.9',
            'Accept-Encoding': 'gzip, deflate, br',
            'Connection': 'keep-alive',
            'Referer': 'https://www.istockphoto.com/',
        }
        
        response = requests.get(url, stream=True, headers=headers, timeout=30)
        response.raise_for_status()
        
        # Validate content type
        content_type = response.headers.get('content-type', '')
        if not content_type.startswith('image/'):
            print(f"⚠️  Warning: Content type is {content_type}, not an image")
        
        # Create static/images directory if it doesn't exist
        os.makedirs('static/images', exist_ok=True)
        
        filepath = os.path.join('static/images', filename)
        
        # Download and save the image
        with open(filepath, 'wb') as f:
            for chunk in response.iter_content(chunk_size=8192):
                if chunk:  # Filter out keep-alive chunks
                    f.write(chunk)
        
        # Verify file was created and has content
        if os.path.exists(filepath) and os.path.getsize(filepath) > 0:
            file_size = os.path.getsize(filepath)
            print(f"✅ Downloaded: {filename} ({file_size} bytes)")
            return True
        else:
            print(f"❌ File creation failed: {filename}")
            return False
            
    except requests.exceptions.RequestException as e:
        print(f"❌ Network error downloading {filename}: {e}")
        return False
    except Exception as e:
        print(f"❌ Failed to download {filename}: {e}")
        return False

def download_fashion_model_image():
    """Download the fashion model image for homepage"""
    
    # Fashion model image URL
    fashion_model_url = "https://media.istockphoto.com/id/1018293976/photo/attractive-fashionable-woman-posing-in-white-trendy-sweater-beige-pants-and-autumn-heels-on.jpg?s=612x612&w=0&k=20&c=_CLawpZw6l9z0uV4Uon-7lqaS013E853ub883pkIK3c="
    
    # Target filename
    filename = "fashion_model_homepage.jpg"
    
    print("👗 Downloading Fashion Model Image for Homepage...")
    print("=" * 60)
    
    # Download the image
    if download_image(fashion_model_url, filename):
        print(f"\n🎉 Fashion model image successfully downloaded!")
        print(f"📁 Saved as: static/images/{filename}")
        print(f"🌐 You can now use this image in your homepage")
        print(f"📸 Reference URL: {filename}")
        
        # Provide HTML code for homepage
        print(f"\n📝 HTML Code for Homepage:")
        print(f'<div class="fashion-model-section">')
        print(f'    <img src="{{{{ url_for("static", filename="images/{filename}") }}}}" alt="Fashion Model" class="img-fluid">')
        print(f'</div>')
        
        return True
    else:
        print(f"\n❌ Failed to download fashion model image")
        return False

if __name__ == '__main__':
    download_fashion_model_image()

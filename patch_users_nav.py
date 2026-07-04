import os
import glob

nav_link = """            <a href="{{ url_for('admin.users') }}" class="nav-item {% if request.endpoint == 'admin.users' %}active{% endif %}"><div class="nav-icon"><i class="fas fa-users"></i></div><span>Users</span></a>"""
nav_link_alt = """            <a href="{{ url_for('admin.users') }}" class="nav-item">
                <div class="nav-icon">
                    <i class="fas fa-users"></i>
                </div>
                <span>Users</span>
            </a>"""

target_dir = r"C:\Users\AE\Desktop\Mode_Avenue today\Mode_Avenue\templates\admin"
html_files = glob.glob(os.path.join(target_dir, "*.html"))

for file_path in html_files:
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    if "admin.users" in content:
        continue

    # Try replacement
    if "<span>Settings</span></a>" in content:
        content = content.replace("<span>Settings</span></a>\n", "<span>Settings</span></a>\n" + nav_link + "\n")
    elif "<span>Settings</span>\n            </a>" in content:
        content = content.replace("<span>Settings</span>\n            </a>\n", "<span>Settings</span>\n            </a>\n" + nav_link_alt + "\n")
        
    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(content)

print("Patch applied to all admin templates")

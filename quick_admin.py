from app import create_app, db
from models import User

def quick_make_all_admin():
    """Quickly make all users admin"""
    app = create_app()
    
    with app.app_context():
        users = User.query.all()
        
        print(f"Making {len(users)} user(s) admin...")
        
        for user in users:
            user.is_admin = True
            print(f"[SUCCESS] {user.username} is now admin")
        
        db.session.commit()
        print("\nAll users are now admins!")
        print("\nYou can now access: http://127.0.0.1:5000/admin/")

if __name__ == "__main__":
    quick_make_all_admin()

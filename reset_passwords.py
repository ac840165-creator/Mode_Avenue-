from app import create_app, db
from models import User, bcrypt

def reset_all_passwords():
    app = create_app()
    with app.app_context():
        users = User.query.all()
        # Generate standard bcrypt hash for 'admin123'
        hashed_password = bcrypt.generate_password_hash('admin123').decode('utf-8')
        
        print("Resetting all user passwords to 'admin123'...")
        for user in users:
            user.password = hashed_password
            user.is_admin = True # Force admin status
            print(f"[SUCCESS] Updated user: {user.username} (Email: {user.email})")
        
        db.session.commit()
        print("\nAll passwords successfully reset to: admin123")

if __name__ == '__main__':
    reset_all_passwords()

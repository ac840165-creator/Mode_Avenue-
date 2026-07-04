from app import create_app, db
from models import User

def make_user_admin():
    """Make a user an admin"""
    app = create_app()
    
    with app.app_context():
        print("🔍 Looking for users in database...")
        
        # List all users
        users = User.query.all()
        
        if not users:
            print("❌ No users found in database!")
            print("\n📝 Please register a user first:")
            print("   1. Go to: http://127.0.0.1:5000/register")
            print("   2. Create an account")
            print("   3. Run this script again")
            return
        
        print(f"\n👥 Found {len(users)} user(s):")
        for user in users:
            admin_status = "✅ ADMIN" if user.is_admin else "❌ Not Admin"
            print(f"   ID: {user.id} | Username: {user.username} | Email: {user.email} | {admin_status}")
        
        # Ask which user to make admin
        print("\n🎯 Options:")
        print("   1. Make the first user an admin")
        print("   2. Enter a specific username to make admin")
        print("   3. Make ALL users admins")
        
        choice = input("\nEnter your choice (1/2/3): ").strip()
        
        if choice == "1":
            user = users[0]
            user.is_admin = True
            db.session.commit()
            print(f"\n✅ Made '{user.username}' an admin!")
            
        elif choice == "2":
            username = input("Enter username: ").strip()
            user = User.query.filter_by(username=username).first()
            if user:
                user.is_admin = True
                db.session.commit()
                print(f"\n✅ Made '{user.username}' an admin!")
            else:
                print(f"\n❌ User '{username}' not found!")
                
        elif choice == "3":
            for user in users:
                user.is_admin = True
            db.session.commit()
            print(f"\n✅ Made ALL {len(users)} user(s) admin!")
        else:
            print("\n❌ Invalid choice!")
            return
        
        print("\n🎉 Admin access granted!")
        print("\n📍 Access the admin dashboard at:")
        print("   http://127.0.0.1:5000/admin/")
        print("\n⚠️  Make sure you're logged in as the admin user!")

if __name__ == "__main__":
    make_user_admin()

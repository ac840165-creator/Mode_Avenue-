from app import create_app, db
from sqlalchemy import text

def fix_database_tables():
    """Keep only the 11 required tables, drop the extra ones"""
    app = create_app()
    
    with app.app_context():
        # Tables we want to keep
        keep_tables = {
            'address', 'cart', 'cart_item', 'category', 
            'order', 'order_item', 'payment', 'product', 
            'review', 'user', 'wishlist'
        }
        
        # Get current tables
        inspector = db.inspect(db.engine)
        current_tables = set(inspector.get_table_names())
        
        # Tables to drop (extra plural versions)
        drop_tables = current_tables - keep_tables
        
        print(f"Current tables: {len(current_tables)}")
        print(f"Tables to keep: {len(keep_tables)}")
        print(f"Tables to drop: {len(drop_tables)}")
        
        if drop_tables:
            print(f"\nDropping extra tables: {drop_tables}")
            for table in drop_tables:
                try:
                    db.session.execute(text(f"DROP TABLE IF EXISTS {table}"))
                    print(f"✅ Dropped table: {table}")
                except Exception as e:
                    print(f"❌ Error dropping {table}: {e}")
            
            db.session.commit()
        
        # Verify final result
        inspector = db.inspect(db.engine)
        final_tables = inspector.get_table_names()
        
        print(f"\n🎉 Final database has {len(final_tables)} tables:")
        for i, table in enumerate(sorted(final_tables), 1):
            print(f"{i}. {table}")
        
        print(f"\n🎯 Target: 11 tables | Final: {len(final_tables)} tables")
        
        if len(final_tables) == 11:
            print("✅ Perfect! Database now has exactly 11 tables in mode_avenue_db!")
        else:
            print(f"⚠️  Still have {len(final_tables)} tables instead of 11")

if __name__ == "__main__":
    fix_database_tables()

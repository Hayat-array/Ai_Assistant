#!/usr/bin/env python3
"""
Database setup script for AI Assistant
Run this script to initialize your MongoDB database with proper indexes and collections.
"""

import os
import sys
from pymongo import MongoClient
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

def setup_database():
    """Setup MongoDB database with required collections and indexes"""
    
    try:
        # Connect to MongoDB
        mongo_uri = os.getenv("MONGO_URI", "mongodb://localhost:27017/")
        print(f"Connecting to MongoDB: {mongo_uri}")
        
        client = MongoClient(mongo_uri)
        
        # Test connection
        client.admin.command('ismaster')
        print("✅ MongoDB connection successful!")
        
        # Get database
        db = client.get_database("ai_assistant")
        
        # Create collections
        collections_to_create = ["users", "chats"]
        
        for collection_name in collections_to_create:
            if collection_name not in db.list_collection_names():
                db.create_collection(collection_name)
                print(f"✅ Created collection: {collection_name}")
            else:
                print(f"📋 Collection already exists: {collection_name}")
        
        # Get collections
        users_collection = db.get_collection("users")
        chats_collection = db.get_collection("chats")
        
        # Create indexes for better performance
        print("\n🔧 Creating database indexes...")
        
        try:
            # Users collection indexes
            users_collection.create_index("email", unique=True)
            print("✅ Created unique index on users.email")
            
            # Chats collection indexes
            chats_collection.create_index([("user_id", 1), ("timestamp", -1)])
            print("✅ Created compound index on chats.user_id and timestamp")
            
        except Exception as e:
            if "already exists" in str(e).lower():
                print("📋 Indexes already exist")
            else:
                print(f"⚠️  Warning creating indexes: {e}")
        
        # Display database info
        print(f"\n📊 Database: {db.name}")
        print(f"📊 Collections: {db.list_collection_names()}")
        print(f"👥 Users count: {users_collection.count_documents({})}")
        print(f"💬 Chats count: {chats_collection.count_documents({})}")
        
        print("\n🎉 Database setup completed successfully!")
        return True
        
    except Exception as e:
        print(f"❌ Database setup failed: {e}")
        return False
    
    finally:
        try:
            client.close()
        except:
            pass

def test_database_connection():
    """Test database connection and basic operations"""
    
    try:
        mongo_uri = os.getenv("MONGO_URI", "mongodb://localhost:27017/")
        client = MongoClient(mongo_uri)
        
        # Test connection
        client.admin.command('ismaster')
        
        # Test basic operations
        db = client.get_database("ai_assistant")
        users_collection = db.get_collection("users")
        
        # Try a simple query
        count = users_collection.count_documents({})
        print(f"✅ Database connection test passed. Users: {count}")
        
        client.close()
        return True
        
    except Exception as e:
        print(f"❌ Database connection test failed: {e}")
        return False

if __name__ == "__main__":
    print("🚀 AI Assistant Database Setup")
    print("=" * 40)
    
    # Check if .env file exists
    if not os.path.exists('.env'):
        print("⚠️  Warning: .env file not found!")
        print("Please create a .env file with your MongoDB connection string.")
        print("Example: MONGO_URI=mongodb://localhost:27017/ai_assistant")
        sys.exit(1)
    
    # Test connection first
    print("🔍 Testing database connection...")
    if not test_database_connection():
        print("❌ Please check your MONGO_URI in .env file")
        sys.exit(1)
    
    # Setup database
    print("\n🛠️  Setting up database...")
    if setup_database():
        print("\n✅ Setup completed! You can now run your Flask application.")
    else:
        print("\n❌ Setup failed. Please check the error messages above.")
        sys.exit(1)
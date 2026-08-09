"""
Automated Supabase setup script
"""
import os
from supabase import create_client
from dotenv import load_dotenv

load_dotenv('.env.local')

url = os.getenv('SUPABASE_URL')
key = os.getenv('SUPABASE_SERVICE_ROLE_KEY')

print("🚀 Setting up Supabase...")
print(f"URL: {url}")

try:
    client = create_client(url, key)
    
    # Create storage buckets
    print("\n📦 Creating storage buckets...")
    
    try:
        # Create raw-docs bucket (private)
        client.storage.create_bucket('raw-docs', {'public': False})
        print("✅ Created bucket: raw-docs (private)")
    except Exception as e:
        if 'already exists' in str(e).lower():
            print("ℹ️  Bucket raw-docs already exists")
        else:
            print(f"❌ Error creating raw-docs: {e}")
    
    try:
        # Create assets bucket (public)
        client.storage.create_bucket('assets', {'public': True})
        print("✅ Created bucket: assets (public)")
    except Exception as e:
        if 'already exists' in str(e).lower():
            print("ℹ️  Bucket assets already exists")
        else:
            print(f"❌ Error creating assets: {e}")
    
    print("\n" + "="*60)
    print("✅ Storage buckets setup complete!")
    print("="*60)
    
    print("\n📋 NEXT STEP: Apply Database Schema")
    print("\nYou need to run the SQL manually:")
    print("1. Go to: https://supabase.com/dashboard/project/easyazauclbtxgkxyfbe/sql/new")
    print("2. Copy SQL from: supabase/migrations/20260211_initial_schema.sql")
    print("3. Paste and click 'Run'")
    print("\nOr run this command:")
    print("  open 'https://supabase.com/dashboard/project/easyazauclbtxgkxyfbe/sql/new'")
    
except Exception as e:
    print(f"❌ Error: {e}")
    exit(1)

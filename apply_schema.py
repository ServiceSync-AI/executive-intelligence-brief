"""
Apply database schema to Supabase
"""
import os
from supabase import create_client
from dotenv import load_dotenv

load_dotenv('.env.local')

url = os.getenv('SUPABASE_URL')
key = os.getenv('SUPABASE_SERVICE_ROLE_KEY')

if not url or not key:
    print("❌ Error: SUPABASE_URL and SUPABASE_SERVICE_ROLE_KEY required in .env.local")
    exit(1)

print(f"🔗 Connecting to Supabase: {url}")

try:
    client = create_client(url, key)
    
    # Read schema file
    with open('supabase/migrations/20260211_initial_schema.sql', 'r') as f:
        schema_sql = f.read()
    
    print("📝 Applying database schema...")
    
    # Execute SQL via Supabase REST API
    # Note: This requires using the SQL editor or direct PostgreSQL connection
    print("\n⚠️  Schema must be applied via Supabase Dashboard:")
    print("1. Go to: https://supabase.com/dashboard/project/easyazauclbtxgkxyfbe/sql/new")
    print("2. Copy the SQL from: supabase/migrations/20260211_initial_schema.sql")
    print("3. Paste and click 'Run'")
    print("\nOr use Supabase CLI:")
    print("  supabase link --project-ref easyazauclbtxgkxyfbe")
    print("  supabase db push")
    
except Exception as e:
    print(f"❌ Error: {e}")
    exit(1)

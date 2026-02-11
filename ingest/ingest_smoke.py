"""
Ingestion smoke test - validates configuration and connectivity
"""
import os
from dotenv import load_dotenv

def test_environment():
    """Check environment variables are set"""
    load_dotenv('.env.local')
    
    required_vars = [
        'SUPABASE_URL',
        'SUPABASE_SERVICE_ROLE_KEY',
        'OPENAI_API_KEY'
    ]
    
    missing = []
    for var in required_vars:
        if not os.getenv(var):
            missing.append(var)
    
    if missing:
        print(f"❌ Missing environment variables: {', '.join(missing)}")
        print("   Create .env.local from .env.example and fill in values")
        return False
    
    print("✓ Environment variables configured")
    return True

def test_supabase_connection():
    """Test Supabase connectivity"""
    try:
        from supabase import create_client
        
        url = os.getenv('SUPABASE_URL')
        key = os.getenv('SUPABASE_SERVICE_ROLE_KEY')
        
        client = create_client(url, key)
        
        # Try a simple query
        result = client.table('raw_files').select('id').limit(1).execute()
        
        print("✓ Supabase connection successful")
        return True
        
    except Exception as e:
        print(f"❌ Supabase connection failed: {e}")
        return False

def test_openai_connection():
    """Test OpenAI API connectivity"""
    try:
        from openai import OpenAI
        
        client = OpenAI(api_key=os.getenv('OPENAI_API_KEY'))
        
        # Test with minimal request
        response = client.embeddings.create(
            model="text-embedding-3-small",
            input="test"
        )
        
        print("✓ OpenAI API connection successful")
        return True
        
    except Exception as e:
        print(f"❌ OpenAI API connection failed: {e}")
        return False

if __name__ == '__main__':
    print("Running smoke tests...\n")
    
    tests = [
        test_environment(),
        test_supabase_connection(),
        test_openai_connection()
    ]
    
    if all(tests):
        print("\n✅ All tests passed! Ready to start development.")
    else:
        print("\n❌ Some tests failed. Fix issues above before continuing.")

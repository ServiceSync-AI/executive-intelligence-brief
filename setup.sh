#!/bin/bash

# Setup script for Executive Intelligence Brief
# Run this after creating Supabase project

set -e

echo "🚀 Executive Intelligence Brief - Setup Script"
echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
echo ""

# Check if we're in the right directory
if [ ! -f "README.md" ]; then
    echo "❌ Error: Run this script from the project root directory"
    exit 1
fi

echo "📋 Step 1: Collecting Supabase Credentials"
echo ""

read -p "Supabase Project URL (https://xxx.supabase.co): " SUPABASE_URL
read -p "Supabase Anon Key: " SUPABASE_ANON_KEY
read -sp "Supabase Service Role Key: " SUPABASE_SERVICE_ROLE_KEY
echo ""
read -p "OpenAI API Key (sk-...): " OPENAI_API_KEY
echo ""

# Validate inputs
if [ -z "$SUPABASE_URL" ] || [ -z "$SUPABASE_ANON_KEY" ] || [ -z "$SUPABASE_SERVICE_ROLE_KEY" ] || [ -z "$OPENAI_API_KEY" ]; then
    echo "❌ Error: All credentials are required"
    exit 1
fi

echo ""
echo "✅ Credentials collected"
echo ""

# Create .env.local
echo "📝 Step 2: Creating .env.local"
cat > .env.local << EOF
# Supabase
SUPABASE_URL=$SUPABASE_URL
SUPABASE_SERVICE_ROLE_KEY=$SUPABASE_SERVICE_ROLE_KEY
SUPABASE_ANON_KEY=$SUPABASE_ANON_KEY

# OpenAI
OPENAI_API_KEY=$OPENAI_API_KEY

# Configuration
EMBEDDING_MODEL=text-embedding-3-small
VECTOR_DIM=1536

# Next.js (for microsite)
NEXT_PUBLIC_SUPABASE_URL=$SUPABASE_URL
NEXT_PUBLIC_SUPABASE_ANON_KEY=$SUPABASE_ANON_KEY
EOF

echo "✅ .env.local created"
echo ""

# Create app/.env.local
echo "📝 Step 3: Creating app/.env.local"
cat > app/.env.local << EOF
NEXT_PUBLIC_SUPABASE_URL=$SUPABASE_URL
NEXT_PUBLIC_SUPABASE_ANON_KEY=$SUPABASE_ANON_KEY
EOF

echo "✅ app/.env.local created"
echo ""

# Install Python dependencies
echo "📦 Step 4: Installing Python dependencies"
if [ ! -d "venv" ]; then
    python3 -m venv venv
fi

source venv/bin/activate
pip install -q --upgrade pip
pip install -q -r requirements.txt

echo "✅ Python dependencies installed"
echo ""

# Install Node dependencies
echo "📦 Step 5: Installing Node dependencies"
cd app
npm install --silent
cd ..

echo "✅ Node dependencies installed"
echo ""

# Test configuration
echo "🧪 Step 6: Testing configuration"
python ingest/ingest_smoke.py

echo ""
echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
echo "✅ Setup Complete!"
echo ""
echo "Next steps:"
echo "1. Apply database schema:"
echo "   supabase login"
echo "   supabase link --project-ref [your-project-ref]"
echo "   supabase db push"
echo ""
echo "2. Create storage buckets in Supabase Studio:"
echo "   - raw-docs (private)"
echo "   - assets (public)"
echo ""
echo "3. Start development:"
echo "   source venv/bin/activate"
echo "   python ingest/ingest.py --directory data/nada-jan-2026"
echo ""
echo "4. Set up AWS Amplify hosting:"
echo "   See docs/AWS_AMPLIFY_SETUP.md"
echo ""
echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"

#!/bin/bash
# Apply database schema to Supabase

echo "📋 Applying database schema to Supabase..."
echo ""
echo "Option 1: Use Supabase CLI (recommended)"
echo "  supabase db push"
echo ""
echo "Option 2: Use SQL Editor"
echo "  1. Go to: https://supabase.com/dashboard/project/easyazauclbtxgkxyfbe/sql/new"
echo "  2. Copy contents of: supabase/migrations/20260211_initial_schema.sql"
echo "  3. Click 'Run'"
echo ""
echo "Option 3: Use psql directly"
echo "  Get connection string from Supabase dashboard → Settings → Database"
echo "  psql 'postgresql://...' < supabase/migrations/20260211_initial_schema.sql"
echo ""

read -p "Apply schema now using Supabase CLI? (y/n) " -n 1 -r
echo
if [[ $REPLY =~ ^[Yy]$ ]]
then
    supabase db push
fi

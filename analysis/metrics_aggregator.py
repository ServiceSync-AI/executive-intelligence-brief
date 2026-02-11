"""Aggregate performance metrics from CSV files."""

import os
import sys
from pathlib import Path
from supabase import create_client
import re


def load_env():
    """Load environment variables"""
    env_path = Path(__file__).parent.parent / ".env.local"
    if env_path.exists():
        with open(env_path) as f:
            for line in f:
                if '=' in line and not line.startswith('#'):
                    key, val = line.strip().split('=', 1)
                    os.environ[key] = val


def get_supabase_client():
    """Initialize Supabase client"""
    url = os.getenv("SUPABASE_URL")
    key = os.getenv("SUPABASE_SERVICE_ROLE_KEY")
    return create_client(url, key)


def get_csv_files(supabase):
    """Get all CSV file contents"""
    print("📥 Retrieving CSV files...")
    
    result = supabase.table('raw_files').select('*').eq('file_type', 'csv').execute()
    
    print(f"   ✓ Retrieved {len(result.data)} CSV files")
    return result.data


def extract_numbers(text):
    """Extract numbers from text"""
    # Find all numbers (including decimals and percentages)
    numbers = re.findall(r'\d+\.?\d*', text)
    return [float(n) for n in numbers if n]


def aggregate_metrics(csv_files):
    """Aggregate metrics from CSV files"""
    print(f"\n📊 Aggregating metrics...")
    
    metrics = []
    
    # Service Absorption
    absorption_files = [f for f in csv_files if 'absorption' in f['file_name'].lower()]
    if absorption_files:
        all_values = []
        for f in absorption_files:
            all_values.extend(extract_numbers(f['content']))
        
        if all_values:
            metrics.append({
                'name': 'Service Absorption',
                'median': sorted(all_values)[len(all_values)//2],
                'low': min(all_values),
                'high': max(all_values),
                'units': 'percentage',
                'evidence': {'sources': [f['file_name'] for f in absorption_files]}
            })
    
    # Tech Proficiency
    prof_files = [f for f in csv_files if 'profic' in f['file_name'].lower()]
    if prof_files:
        all_values = []
        for f in prof_files:
            all_values.extend(extract_numbers(f['content']))
        
        if all_values:
            metrics.append({
                'name': 'Technician Proficiency',
                'median': sorted(all_values)[len(all_values)//2],
                'low': min(all_values),
                'high': max(all_values),
                'units': 'percentage',
                'evidence': {'sources': [f['file_name'] for f in prof_files]}
            })
    
    # Parts Inventory Turn
    parts_files = [f for f in csv_files if 'parts' in f['file_name'].lower() and 'turn' in f['file_name'].lower()]
    if parts_files:
        all_values = []
        for f in parts_files:
            all_values.extend(extract_numbers(f['content']))
        
        if all_values:
            metrics.append({
                'name': 'Parts Inventory Turn',
                'median': sorted(all_values)[len(all_values)//2],
                'low': min(all_values),
                'high': max(all_values),
                'units': 'days',
                'evidence': {'sources': [f['file_name'] for f in parts_files]}
            })
    
    # Recon Days
    recon_files = [f for f in csv_files if 'recon' in f['file_name'].lower()]
    if recon_files:
        all_values = []
        for f in recon_files:
            all_values.extend(extract_numbers(f['content']))
        
        if all_values:
            metrics.append({
                'name': 'Days to Breakeven After Recon',
                'median': sorted(all_values)[len(all_values)//2],
                'low': min(all_values),
                'high': max(all_values),
                'units': 'days',
                'evidence': {'sources': [f['file_name'] for f in recon_files]}
            })
    
    print(f"   ✓ Aggregated {len(metrics)} metrics")
    return metrics


def store_metrics(supabase, metrics):
    """Store metrics in database"""
    print(f"\n💾 Storing metrics...")
    
    result = supabase.table("metrics").insert(metrics).execute()
    
    print(f"   ✓ Stored {len(result.data)} metrics")
    return result.data


def main():
    print("\n🚀 Starting Metrics Aggregation\n")
    print("=" * 60)
    
    load_env()
    supabase = get_supabase_client()
    print("✓ Connected to Supabase")
    
    # Get CSV files
    csv_files = get_csv_files(supabase)
    
    # Aggregate metrics
    metrics = aggregate_metrics(csv_files)
    
    # Store metrics
    stored = store_metrics(supabase, metrics)
    
    # Summary
    print("\n" + "=" * 60)
    print(f"\n✅ Metrics Aggregation Complete!")
    print(f"\n📊 Results:")
    print(f"   Metrics aggregated: {len(stored)}")
    
    print(f"\n📈 Metrics:")
    for m in metrics:
        print(f"\n   {m['name']}")
        print(f"      Median: {m['median']:.1f} {m['units']}")
        print(f"      Range: {m['low']:.1f} - {m['high']:.1f}")
        print(f"      Sources: {len(m['evidence']['sources'])}")


if __name__ == "__main__":
    main()

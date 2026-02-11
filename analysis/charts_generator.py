"""Generate visualizations for the intelligence brief."""

import os
import sys
from pathlib import Path
from supabase import create_client
import plotly.graph_objects as go
import plotly.express as px
from datetime import datetime


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


def create_topic_gravity_map(topics):
    """Create bubble chart of topics by evidence count"""
    print("📊 Creating topic gravity map...")
    
    # Extract data
    names = [t['topic'] for t in topics]
    evidence_counts = [t['evidence']['count'] for t in topics]
    confidence = [t['confidence'] for t in topics]
    
    # Create bubble chart
    fig = go.Figure(data=[go.Scatter(
        x=list(range(len(names))),
        y=evidence_counts,
        mode='markers+text',
        marker=dict(
            size=[c * 100 for c in confidence],
            color=confidence,
            colorscale='Viridis',
            showscale=True,
            colorbar=dict(title="Confidence")
        ),
        text=names,
        textposition="top center",
        textfont=dict(size=10),
        hovertemplate='<b>%{text}</b><br>Evidence: %{y}<br>Confidence: %{marker.color:.2f}<extra></extra>'
    )])
    
    fig.update_layout(
        title="Topic Gravity Map - Discussion Frequency",
        xaxis_title="Topics",
        yaxis_title="Evidence Count (chunks)",
        height=600,
        showlegend=False,
        xaxis=dict(showticklabels=False)
    )
    
    output_path = Path(__file__).parent.parent / "assets" / "topic_gravity_map.html"
    output_path.parent.mkdir(exist_ok=True)
    fig.write_html(str(output_path))
    
    print(f"   ✓ Saved to {output_path}")
    return str(output_path)


def create_commitment_matrix(commitments):
    """Create matrix of commitments by theme"""
    print("📊 Creating commitment matrix...")
    
    # Group by theme
    by_theme = {}
    for c in commitments:
        theme = c['theme']
        if theme not in by_theme:
            by_theme[theme] = []
        by_theme[theme].append(c['dealer_code'])
    
    # Create bar chart
    themes = list(by_theme.keys())
    counts = [len(by_theme[t]) for t in themes]
    
    fig = go.Figure(data=[go.Bar(
        x=themes,
        y=counts,
        text=counts,
        textposition='auto',
        marker_color='rgb(55, 83, 109)'
    )])
    
    fig.update_layout(
        title="Dealer Commitments by Theme",
        xaxis_title="Theme",
        yaxis_title="Number of Commitments",
        height=500
    )
    
    output_path = Path(__file__).parent.parent / "assets" / "commitment_matrix.html"
    fig.write_html(str(output_path))
    
    print(f"   ✓ Saved to {output_path}")
    return str(output_path)


def create_metrics_variance(metrics):
    """Create variance panels for metrics"""
    print("📊 Creating metrics variance panels...")
    
    # Create box plots for each metric
    fig = go.Figure()
    
    for i, m in enumerate(metrics):
        fig.add_trace(go.Box(
            y=[m['low'], m['median'], m['high']],
            name=m['name'],
            boxmean='sd'
        ))
    
    fig.update_layout(
        title="Performance Metrics - Variance Analysis",
        yaxis_title="Value",
        height=500,
        showlegend=True
    )
    
    output_path = Path(__file__).parent.parent / "assets" / "metrics_variance.html"
    fig.write_html(str(output_path))
    
    print(f"   ✓ Saved to {output_path}")
    return str(output_path)


def create_topic_heatmap(topics):
    """Create heatmap of topic confidence"""
    print("📊 Creating topic confidence heatmap...")
    
    # Sort by confidence
    sorted_topics = sorted(topics, key=lambda x: x['confidence'], reverse=True)
    
    names = [t['topic'] for t in sorted_topics]
    confidence = [t['confidence'] for t in sorted_topics]
    evidence = [t['evidence']['count'] for t in sorted_topics]
    
    fig = go.Figure(data=go.Heatmap(
        z=[confidence],
        x=names,
        y=['Confidence'],
        colorscale='RdYlGn',
        text=[[f"{c:.2f}" for c in confidence]],
        texttemplate='%{text}',
        textfont={"size": 10},
        hovertemplate='Topic: %{x}<br>Confidence: %{z:.2f}<extra></extra>'
    ))
    
    fig.update_layout(
        title="Topic Confidence Heatmap",
        height=300,
        xaxis=dict(tickangle=-45)
    )
    
    output_path = Path(__file__).parent.parent / "assets" / "topic_heatmap.html"
    fig.write_html(str(output_path))
    
    print(f"   ✓ Saved to {output_path}")
    return str(output_path)


def upload_to_supabase(supabase, file_paths):
    """Upload charts to Supabase storage"""
    print("\n📤 Uploading charts to Supabase...")
    
    uploaded = []
    for path in file_paths:
        file_path = Path(path)
        
        with open(file_path, 'rb') as f:
            content = f.read()
        
        # Upload to assets bucket
        result = supabase.storage.from_('assets').upload(
            f"charts/{file_path.name}",
            content,
            {"content-type": "text/html"}
        )
        
        # Get public URL
        url = supabase.storage.from_('assets').get_public_url(f"charts/{file_path.name}")
        uploaded.append(url)
        
        print(f"   ✓ Uploaded {file_path.name}")
    
    return uploaded


def main():
    print("\n🚀 Starting Visualization Generation\n")
    print("=" * 60)
    
    load_env()
    supabase = get_supabase_client()
    print("✓ Connected to Supabase")
    
    # Get data
    print("\n📥 Retrieving data...")
    topics = supabase.table("knowledge_topics").select("*").execute().data
    commitments = supabase.table("commitments").select("*").execute().data
    metrics = supabase.table("metrics").select("*").execute().data
    
    print(f"   ✓ Topics: {len(topics)}")
    print(f"   ✓ Commitments: {len(commitments)}")
    print(f"   ✓ Metrics: {len(metrics)}")
    
    # Generate charts
    print("\n📊 Generating visualizations...")
    charts = []
    
    if topics:
        charts.append(create_topic_gravity_map(topics))
        charts.append(create_topic_heatmap(topics))
    
    if commitments:
        charts.append(create_commitment_matrix(commitments))
    
    if metrics:
        charts.append(create_metrics_variance(metrics))
    
    # Upload to Supabase
    urls = upload_to_supabase(supabase, charts)
    
    # Summary
    print("\n" + "=" * 60)
    print(f"\n✅ Visualization Generation Complete!")
    print(f"\n📊 Results:")
    print(f"   Charts created: {len(charts)}")
    print(f"   Charts uploaded: {len(urls)}")
    
    print(f"\n🔗 Chart URLs:")
    for i, url in enumerate(urls, 1):
        print(f"   {i}. {url}")


if __name__ == "__main__":
    main()

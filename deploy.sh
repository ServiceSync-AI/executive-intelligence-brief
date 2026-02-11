#!/bin/bash
set -e

echo "🏗️  Building Next.js app..."
cd app
npm run build

echo "📤 Uploading to S3..."
aws s3 sync out/ s3://gc06-servicesync \
  --delete \
  --cache-control "public, max-age=31536000, immutable"

echo "✅ Deployment complete!"
echo "🌐 Site: https://gc06.servicesync.io"

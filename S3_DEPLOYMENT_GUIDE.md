# S3 + CloudFront Deployment (Cheapest Option)

## Cost: ~$0.50-1/month

---

## Prerequisites

- AWS CLI configured
- Cloudflare account with servicesync.io domain
- Next.js app built

---

## Step 1: Configure Next.js for Static Export

Edit `app/next.config.js`:

```javascript
/** @type {import('next').Config} */
const nextConfig = {
  output: 'export',
  images: {
    unoptimized: true,
  },
}

module.exports = nextConfig
```

---

## Step 2: Build Static Site

```bash
cd app
npm run build
```

This creates `app/out/` with static HTML files.

---

## Step 3: Create S3 Bucket

```bash
# Create bucket
aws s3 mb s3://gc06-servicesync --region us-east-1

# Enable static website hosting
aws s3 website s3://gc06-servicesync \
  --index-document index.html \
  --error-document 404.html
```

---

## Step 4: Create Bucket Policy (Public Read)

Create `bucket-policy.json`:

```json
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Sid": "PublicReadGetObject",
      "Effect": "Allow",
      "Principal": "*",
      "Action": "s3:GetObject",
      "Resource": "arn:aws:s3:::gc06-servicesync/*"
    }
  ]
}
```

Apply policy:

```bash
aws s3api put-bucket-policy \
  --bucket gc06-servicesync \
  --policy file://bucket-policy.json
```

---

## Step 5: Upload Files to S3

```bash
cd app
aws s3 sync out/ s3://gc06-servicesync \
  --delete \
  --cache-control "public, max-age=31536000, immutable"
```

---

## Step 6: Get S3 Website URL

```bash
echo "http://gc06-servicesync.s3-website-us-east-1.amazonaws.com"
```

Test this URL in your browser.

---

## Step 7: Configure Cloudflare DNS

1. Go to: https://dash.cloudflare.com
2. Select domain: `servicesync.io`
3. DNS → Add record:
   - **Type:** `CNAME`
   - **Name:** `gc06`
   - **Target:** `gc06-servicesync.s3-website-us-east-1.amazonaws.com`
   - **Proxy status:** ON (orange cloud) - This gives you free SSL!
   - **TTL:** Auto
4. Click "Save"

---

## Step 8: Configure Cloudflare SSL

1. In Cloudflare → SSL/TLS
2. Set mode to: **Flexible** (Cloudflare ↔ Browser: HTTPS, Cloudflare ↔ S3: HTTP)
3. Enable "Always Use HTTPS"

---

## Step 9: Test Your Site

Wait 2-3 minutes for DNS propagation, then visit:

**https://gc06.servicesync.io**

---

## Deployment Script (For Updates)

Create `deploy.sh` in project root:

```bash
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
```

Make executable:

```bash
chmod +x deploy.sh
```

To deploy updates:

```bash
./deploy.sh
```

---

## Optional: Add CloudFront CDN (Faster, Still Cheap)

If you want even faster global performance:

### Create CloudFront Distribution

```bash
aws cloudfront create-distribution \
  --origin-domain-name gc06-servicesync.s3-website-us-east-1.amazonaws.com \
  --default-root-object index.html \
  --enabled
```

Note the CloudFront domain (e.g., `d111111abcdef8.cloudfront.net`)

### Update Cloudflare DNS

Change CNAME target to CloudFront domain instead of S3.

**Cost:** Adds ~$0.50-1/month, but much faster globally.

---

## Cost Breakdown

**Without CloudFront:**
- S3 storage: $0.023/GB/month (~$0.05 for your site)
- S3 requests: $0.0004/1000 requests (~$0.10 for 250k requests)
- Data transfer: FREE (Cloudflare proxy handles this)
- **Total: ~$0.15-0.50/month**

**With CloudFront:**
- Above + CloudFront: $0.085/GB served
- **Total: ~$0.50-1.50/month**

---

## Troubleshooting

**Site not loading:**
- Check S3 bucket policy is public
- Verify files uploaded: `aws s3 ls s3://gc06-servicesync/`
- Check Cloudflare DNS: `dig gc06.servicesync.io`

**404 errors:**
- Verify `index.html` exists in S3 root
- Check Next.js export completed: `ls app/out/`

**No SSL:**
- Verify Cloudflare proxy is ON (orange cloud)
- Check SSL mode is "Flexible"
- Wait 5 minutes for SSL to activate

**Styles not loading:**
- Check `next.config.js` has `output: 'export'`
- Verify `images.unoptimized: true`
- Rebuild: `npm run build`

---

## Updating the Site

Whenever you make changes:

```bash
# 1. Make changes to code
# 2. Run deployment script
./deploy.sh

# That's it! Changes live in ~30 seconds
```

---

## Comparison

| Method | Cost/Month | Setup Time | Updates |
|--------|-----------|------------|---------|
| **S3 + Cloudflare** | $0.15-0.50 | 10 min | Manual (30 sec) |
| S3 + CloudFront | $0.50-1.50 | 15 min | Manual (30 sec) |
| AWS Amplify | $1-3 | 5 min | Auto (GitHub) |
| EC2 t4g.nano | $3-5 | 30 min | Manual (complex) |

**Recommendation:** Start with S3 + Cloudflare. Add CloudFront later if you need global speed.

---

## Next Steps

1. Create `next.config.js` with export settings
2. Run the commands above
3. Configure Cloudflare DNS
4. Test at https://gc06.servicesync.io
5. Create `deploy.sh` for easy updates

**Total time:** ~10 minutes  
**Total cost:** ~$0.50/month

---

Ready to deploy? Let me know if you want me to create the config files!

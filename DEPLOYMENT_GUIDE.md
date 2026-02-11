# AWS + Cloudflare Deployment Guide

## Goal
Deploy the Executive Intelligence Brief to AWS and make it accessible at:
**https://gc06.servicesync.io**

---

## Option 1: AWS Amplify (Recommended - Easiest)

### Step 1: Deploy to AWS Amplify

1. **Go to AWS Amplify Console:**
   https://console.aws.amazon.com/amplify/home

2. **Click "New app" → "Host web app"**

3. **Connect GitHub:**
   - Select "GitHub"
   - Authorize AWS Amplify
   - Choose repository: `ServiceSync-AI/executive-intelligence-brief`
   - Choose branch: `main`

4. **Configure build settings:**
   - App name: `executive-intelligence-brief`
   - Build settings (auto-detected):
   ```yaml
   version: 1
   frontend:
     phases:
       preBuild:
         commands:
           - cd app
           - npm ci
       build:
         commands:
           - npm run build
     artifacts:
       baseDirectory: app/.next
       files:
         - '**/*'
     cache:
       paths:
         - app/node_modules/**/*
   ```

5. **Add environment variables:**
   - Click "Advanced settings"
   - Add:
     - `NEXT_PUBLIC_SUPABASE_URL` = `https://easyazauclbtxgkxyfbe.supabase.co`
     - `NEXT_PUBLIC_SUPABASE_ANON_KEY` = `eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6ImVhc3lhemF1Y2xidHhna3h5ZmJlIiwicm9sZSI6ImFub24iLCJpYXQiOjE3NzA4MzkzMzUsImV4cCI6MjA4NjQxNTMzNX0.A9nf_XnOosibGRK-Z0FGtJyYpyOXE29Z8W3P1AkfrQA`

6. **Click "Save and deploy"**

7. **Wait for deployment** (~5 minutes)
   - You'll get a URL like: `https://main.d1234abcd.amplifyapp.com`

---

### Step 2: Configure Custom Domain in Cloudflare

1. **Get Amplify domain info:**
   - In Amplify Console → Domain management
   - Note the Amplify domain (e.g., `main.d1234abcd.amplifyapp.com`)

2. **Go to Cloudflare Dashboard:**
   https://dash.cloudflare.com

3. **Select your domain:** `servicesync.io`

4. **Add DNS record:**
   - Click "DNS" → "Records" → "Add record"
   - Type: `CNAME`
   - Name: `gc06`
   - Target: `main.d1234abcd.amplifyapp.com` (your Amplify domain)
   - Proxy status: Proxied (orange cloud)
   - TTL: Auto
   - Click "Save"

5. **Back in AWS Amplify:**
   - Go to "Domain management"
   - Click "Add domain"
   - Enter: `gc06.servicesync.io`
   - Click "Configure domain"
   - AWS will verify and issue SSL certificate (~15 minutes)

6. **Wait for SSL certificate:**
   - Status will change from "Pending verification" → "Available"
   - Site will be live at https://gc06.servicesync.io

---

## Option 2: AWS S3 + CloudFront (More Control)

### Step 1: Build the app

```bash
cd app
npm run build
npm run export  # If using static export
```

### Step 2: Create S3 bucket

```bash
aws s3 mb s3://gc06-servicesync-io --region us-east-1
```

### Step 3: Configure bucket for static hosting

```bash
aws s3 website s3://gc06-servicesync-io \
  --index-document index.html \
  --error-document 404.html
```

### Step 4: Upload files

```bash
cd app/out  # or .next if not using export
aws s3 sync . s3://gc06-servicesync-io --delete
```

### Step 5: Create CloudFront distribution

```bash
aws cloudfront create-distribution \
  --origin-domain-name gc06-servicesync-io.s3.amazonaws.com \
  --default-root-object index.html
```

Note the CloudFront domain (e.g., `d111111abcdef8.cloudfront.net`)

### Step 6: Configure Cloudflare DNS

Same as Option 1, but use CloudFront domain as target.

---

## Quick Start (Recommended Path)

### 1. AWS Amplify Setup (5 minutes)

```bash
# Install Amplify CLI
npm install -g @aws-amplify/cli

# Configure
amplify configure

# Initialize in app directory
cd app
amplify init

# Add hosting
amplify add hosting
# Choose: "Hosting with Amplify Console"

# Publish
amplify publish
```

### 2. Cloudflare DNS (2 minutes)

1. Go to Cloudflare → servicesync.io → DNS
2. Add CNAME: `gc06` → `[your-amplify-url]`
3. Enable proxy (orange cloud)

### 3. Amplify Custom Domain (15 minutes)

1. Amplify Console → Domain management
2. Add domain: `gc06.servicesync.io`
3. Wait for SSL certificate

---

## Environment Variables

Make sure these are set in Amplify:

```bash
NEXT_PUBLIC_SUPABASE_URL=https://easyazauclbtxgkxyfbe.supabase.co
NEXT_PUBLIC_SUPABASE_ANON_KEY=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6ImVhc3lhemF1Y2xidHhna3h5ZmJlIiwicm9sZSI6ImFub24iLCJpYXQiOjE3NzA4MzkzMzUsImV4cCI6MjA4NjQxNTMzNX0.A9nf_XnOosibGRK-Z0FGtJyYpyOXE29Z8W3P1AkfrQA
```

---

## Verification Steps

1. **Check Amplify deployment:**
   - Go to Amplify Console
   - Verify build succeeded
   - Test Amplify URL

2. **Check Cloudflare DNS:**
   ```bash
   dig gc06.servicesync.io
   ```
   Should show CNAME to Amplify

3. **Check SSL:**
   ```bash
   curl -I https://gc06.servicesync.io
   ```
   Should return 200 OK

4. **Test site:**
   - Open https://gc06.servicesync.io
   - Verify all data loads
   - Check charts display

---

## Troubleshooting

**Build fails:**
- Check environment variables are set
- Verify `app/package.json` has correct scripts
- Check build logs in Amplify Console

**DNS not resolving:**
- Wait 5-10 minutes for DNS propagation
- Verify CNAME record in Cloudflare
- Check proxy status (should be orange)

**SSL certificate pending:**
- Can take up to 15 minutes
- Verify domain ownership in Amplify
- Check Cloudflare proxy is enabled

**Site loads but no data:**
- Check environment variables in Amplify
- Verify Supabase URL and key are correct
- Check browser console for errors

---

## Cost Estimate

**AWS Amplify:**
- Build minutes: Free tier (1000 min/month)
- Hosting: $0.15/GB served
- Estimated: $1-5/month

**Cloudflare:**
- DNS: Free
- Proxy: Free
- SSL: Free

**Total: ~$1-5/month**

---

## Next Steps

1. Deploy to Amplify (follow Option 1)
2. Configure Cloudflare DNS
3. Wait for SSL certificate
4. Test at https://gc06.servicesync.io
5. Share with stakeholders!

---

**Questions?** Check AWS Amplify docs: https://docs.amplify.aws

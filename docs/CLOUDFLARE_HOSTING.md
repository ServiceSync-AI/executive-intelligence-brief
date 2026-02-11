# AWS Amplify + Cloudflare Setup for brief.servicesync.io

**Host the Executive Intelligence Brief on AWS with custom subdomain**

---

## 🎯 Setup Overview

1. Deploy Next.js app to AWS Amplify (automatic from GitHub)
2. Get Amplify URL
3. Add CNAME in Cloudflare pointing to Amplify
4. Configure custom domain in Amplify

**Result:** https://brief.servicesync.io

---

## Step 1: Deploy to AWS Amplify (10 minutes)

### 1.1 Go to AWS Amplify Console

```
https://console.aws.amazon.com/amplify/home?region=us-east-1
```

### 1.2 Create New App

1. Click "New app" → "Host web app"
2. Select "GitHub"
3. Click "Authorize AWS Amplify" (if needed)
4. Select repository: `ServiceSync-AI/executive-intelligence-brief`
5. Select branch: `main`

### 1.3 Configure Build Settings

Amplify should auto-detect Next.js. Verify these settings:

**App root directory:** `app`

**Build settings:**
```yaml
version: 1
frontend:
  phases:
    preBuild:
      commands:
        - npm ci
    build:
      commands:
        - npm run build
  artifacts:
    baseDirectory: .next
    files:
      - '**/*'
  cache:
    paths:
      - node_modules/**/*
```

### 1.4 Add Environment Variables

Click "Advanced settings" → Add environment variables:

```
NEXT_PUBLIC_SUPABASE_URL=https://easyazauclbtxgkxyfbe.supabase.co
NEXT_PUBLIC_SUPABASE_ANON_KEY=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6ImVhc3lhemF1Y2xidHhna3h5ZmJlIiwicm9sZSI6ImFub24iLCJpYXQiOjE3NzA4MzkzMzUsImV4cCI6MjA4NjQxNTMzNX0.A9nf_XnOosibGRK-Z0FGtJyYpyOXE29Z8W3P1AkfrQA
```

### 1.5 Deploy

1. Click "Save and deploy"
2. Wait 3-5 minutes for build
3. You'll get a URL like: `https://main.d1234abcd.amplifyapp.com`

**Test this URL first to make sure it works!**

---

## Step 2: Configure Cloudflare DNS (2 minutes)

### 2.1 Get Your Amplify Domain

From Amplify Console, copy your app URL (without https://):
```
main.d1234abcd.amplifyapp.com
```

### 2.2 Add CNAME in Cloudflare

1. Go to: https://dash.cloudflare.com
2. Select domain: `servicesync.io`
3. Go to "DNS" → "Records"
4. Click "Add record"

**Settings:**
- Type: `CNAME`
- Name: `brief`
- Target: `main.d1234abcd.amplifyapp.com` (your Amplify URL)
- Proxy status: **Proxied** (orange cloud)
- TTL: Auto

5. Click "Save"

---

## Step 3: Add Custom Domain in Amplify (3 minutes)

### 3.1 In Amplify Console

1. Go to your app in Amplify
2. Click "Domain management" in left sidebar
3. Click "Add domain"

### 3.2 Configure Domain

1. Enter: `brief.servicesync.io`
2. Click "Configure domain"
3. Amplify will show SSL certificate status
4. Wait 5-10 minutes for SSL certificate to provision

### 3.3 Verify

Once SSL is ready:
- Go to: https://brief.servicesync.io
- Should see your site with valid SSL certificate

---

## Alternative: Cloudflare Pages (Simpler)

If you prefer Cloudflare Pages instead of AWS Amplify:

### Option A: Via Cloudflare Dashboard

1. Go to: https://dash.cloudflare.com
2. Click "Workers & Pages"
3. Click "Create application" → "Pages"
4. Connect to GitHub: `ServiceSync-AI/executive-intelligence-brief`
5. Build settings:
   - Framework: Next.js
   - Build command: `cd app && npm run build`
   - Build output: `app/.next`
6. Environment variables: (same as above)
7. Deploy

**Result:** Automatic `brief.servicesync.io` subdomain (no DNS config needed!)

---

## Recommendation

**Use Cloudflare Pages** because:
- ✅ Simpler setup (no DNS configuration)
- ✅ Automatic subdomain on servicesync.io
- ✅ Free SSL
- ✅ Better integration with Cloudflare
- ✅ Faster global CDN
- ✅ Free tier is generous

**Use AWS Amplify** if:
- You want everything in AWS
- You need AWS-specific integrations
- You prefer AWS billing

---

## Quick Start: Cloudflare Pages (Recommended)

```bash
# 1. Go to Cloudflare Dashboard
https://dash.cloudflare.com

# 2. Workers & Pages → Create → Pages → Connect to Git

# 3. Select repo: ServiceSync-AI/executive-intelligence-brief

# 4. Build settings:
Root directory: app
Build command: npm run build
Build output: .next

# 5. Environment variables:
NEXT_PUBLIC_SUPABASE_URL=https://easyazauclbtxgkxyfbe.supabase.co
NEXT_PUBLIC_SUPABASE_ANON_KEY=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6ImVhc3lhemF1Y2xidHhna3h5ZmJlIiwicm9sZSI6ImFub24iLCJpYXQiOjE3NzA4MzkzMzUsImV4cCI6MjA4NjQxNTMzNX0.A9nf_XnOosibGRK-Z0FGtJyYpyOXE29Z8W3P1AkfrQA

# 6. Deploy!
```

**Result:** https://brief.servicesync.io (automatic!)

---

## Cost Comparison

**Cloudflare Pages:**
- Free: Unlimited requests, 500 builds/month
- Pro: $20/month (if needed)

**AWS Amplify:**
- Free tier: 1000 build minutes/month, 15GB served
- After: ~$0.01/min build, ~$0.15/GB served
- Estimated: $5-10/month

---

## My Recommendation

**Use Cloudflare Pages** - It's simpler, free, and you already use Cloudflare for DNS.

Want me to walk you through the Cloudflare Pages setup?

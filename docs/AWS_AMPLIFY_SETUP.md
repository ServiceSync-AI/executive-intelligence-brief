# AWS Amplify Hosting Setup

**Host the Executive Intelligence Brief microsite on AWS Amplify**

---

## Why AWS Amplify?

- ✅ Already using AWS infrastructure
- ✅ Automatic CI/CD from GitHub
- ✅ Free SSL certificates
- ✅ Global CDN
- ✅ Easy custom domain setup
- ✅ Environment variable management
- ✅ Preview deployments for PRs

---

## Setup Steps

### 1. Install Amplify CLI (if not already installed)

```bash
npm install -g @aws-amplify/cli
amplify configure
```

### 2. Connect GitHub Repository

1. Go to AWS Console → Amplify
2. Click "New app" → "Host web app"
3. Select "GitHub"
4. Authorize AWS Amplify
5. Select repository: `ServiceSync-AI/executive-intelligence-brief`
6. Select branch: `main`

### 3. Configure Build Settings

**Build settings (auto-detected for Next.js):**

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

### 4. Add Environment Variables

In Amplify Console → App Settings → Environment variables:

```
NEXT_PUBLIC_SUPABASE_URL=https://[your-project].supabase.co
NEXT_PUBLIC_SUPABASE_ANON_KEY=[your-anon-key]
```

**Note:** Don't add `SUPABASE_SERVICE_ROLE_KEY` here (only for backend/ingestion)

### 5. Deploy

- Click "Save and deploy"
- Wait 3-5 minutes for first deployment
- Get your URL: `https://main.[app-id].amplifyapp.com`

---

## Custom Domain Setup (Optional)

### If you have a domain:

1. Amplify Console → Domain management
2. Add domain
3. Follow DNS configuration steps
4. SSL certificate auto-provisioned

**Suggested subdomain:** `brief.servicesync.io`

---

## Deployment Workflow

**Automatic deployments:**
- Push to `main` → Deploys to production
- Open PR → Creates preview deployment
- Merge PR → Updates production

**Manual deployment:**
```bash
# From AWS Console
Amplify → Your App → Redeploy this version
```

---

## Environment Variables Management

**For local development:**
```bash
# In project root
cp .env.example .env.local
# Add your keys
```

**For Amplify (production):**
- Set in Amplify Console
- Automatically injected during build

---

## Monitoring

**Amplify provides:**
- Build logs
- Access logs
- Performance metrics
- Error tracking

**Access:** Amplify Console → Your App → Monitoring

---

## Cost Estimate

**Free Tier (first 12 months):**
- 1000 build minutes/month
- 15 GB served/month
- 5 GB stored/month

**After free tier:**
- ~$0.01 per build minute
- ~$0.15 per GB served
- ~$0.023 per GB stored

**Expected cost:** $0-5/month for this project

---

## Alternative: AWS S3 + CloudFront

If you prefer static hosting:

```bash
# Build static export
cd app
npm run build
npm run export

# Deploy to S3
aws s3 sync out/ s3://your-bucket-name --delete

# Invalidate CloudFront
aws cloudfront create-invalidation --distribution-id YOUR_ID --paths "/*"
```

**Setup required:**
- S3 bucket with static hosting
- CloudFront distribution
- Route53 for DNS (if custom domain)

---

## Recommendation

**Use AWS Amplify** for this project because:
- Automatic deployments from GitHub
- No manual build/upload steps
- Preview deployments for testing
- Easier for team collaboration

---

## Next Steps

1. Create Supabase project
2. Configure environment variables
3. Set up Amplify hosting
4. Test deployment
5. Configure custom domain (optional)

---

**Questions?** See AWS Amplify docs: https://docs.amplify.aws

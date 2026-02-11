# GitHub Workflows

## CI Workflow

The CI workflow (`.github/workflows/ci.yml`) runs on pull requests and pushes to main.

**Note:** Due to GitHub token scope limitations, workflow files must be added via the GitHub web interface or with a token that has `workflow` scope.

To add the workflow:
1. Go to https://github.com/ServiceSync-AI/executive-intelligence-brief
2. Navigate to `.github/workflows/`
3. Create new file `ci.yml`
4. Copy contents from this directory
5. Commit directly to main

Alternatively, update your GitHub CLI token with workflow scope:
```bash
gh auth refresh -s workflow
```

Then push the workflow file.

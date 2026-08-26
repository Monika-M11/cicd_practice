# GitHub Workflows

This project uses GitHub Actions for continuous integration and deployment.

## Workflows

### CI/CD Pipeline (`.github/workflows/deploy.yml`)

**Trigger**: Runs on every push to the `main` branch

**Purpose**: Runs tests and deploys to Render if tests pass

**Jobs**:
1. **Test Job**: Runs all pytest tests to ensure code quality
2. **Deploy Job**: Triggers Render deployment hook (only if tests pass)

**Steps in Test Job**:
1. Checks out the code
2. Sets up Python 3.10
3. Installs dependencies from `requirements.txt`
4. Runs all pytest tests
5. Optionally runs tests with coverage and uploads to Codecov

**Usage**: This workflow runs automatically on main branch pushes.

## Secrets Required

For the CI/CD workflow to work, you need to set up the following GitHub secret:

- `RENDER_DEPLOY_HOOK_URL`: The deploy hook URL from your Render service

For optional coverage reporting:

- `CODECOV_TOKEN`: Your Codecov token for coverage uploads

## Manual Testing

You can manually run tests locally with:

```bash
python -m pytest -v
```

Or run tests with coverage:

```bash
pip install pytest-cov
python -m pytest --cov=./ --cov-report=term-missing
```

**Note**: The CI/CD workflow runs the same tests automatically, so what you test locally is what will run in CI.

## Workflow Status Badges

You can add these badges to your README.md:

```markdown
[![CI/CD Status](https://github.com/your-username/your-repo/actions/workflows/deploy.yml/badge.svg)](https://github.com/your-username/your-repo/actions/workflows/deploy.yml)

[![Codecov](https://codecov.io/gh/your-username/your-repo/branch/main/graph/badge.svg)](https://codecov.io/gh/your-username/your-repo)
```

## Viewing Workflow Results

1. Go to your GitHub repository
2. Click on the "Actions" tab
3. Select the workflow you want to view
4. Click on the specific run to see details

## Troubleshooting

If a workflow fails:
1. Check the logs in the GitHub Actions interface
2. Run the tests locally to reproduce the issue
3. Make sure all dependencies are properly listed in `requirements.txt`
4. Ensure Python version matches (3.10 in this case)

## Customizing Workflows

You can customize the workflows by editing the YAML files in `.github/workflows/`.

Common customizations:
- Change Python version
- Add additional test steps
- Modify deployment conditions
- Add notifications for workflow results

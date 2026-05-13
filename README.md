# Codeberg Auto-Sync

Automatically syncs all GitHub repos to Codeberg.

## Features

- 🔄 Auto-syncs every hour
- 📦 Migrates new repos automatically
- 🏥 Health check endpoint for monitoring
- 🚀 Runs 24/7 on Render free tier

## Endpoints

| Endpoint | Method | Description |
|----------|--------|-------------|
| `/` | GET | Service status |
| `/health` | GET | Health check for uptime monitoring |
| `/sync` | GET | Manually trigger sync |

## Environment Variables

| Variable | Required | Description |
|----------|----------|-------------|
| `GITHUB_TOKEN` | Yes | GitHub PAT with `repo` scope |
| `CODEBERG_TOKEN` | Yes | Codeberg token with `write:repository` |

## Deployment

Deployed on Render: https://codeberg-auto-sync.onrender.com

## Health Check

For uptime monitoring: `https://codeberg-auto-sync.onrender.com/health`

## Tech Stack

- Flask
- Gunicorn  
- Python 3.11

## License

MIT

from flask import Flask, jsonify
import requests
import os

app = Flask(__name__)

# Tokens from environment variables (SECURE!)
GITHUB_TOKEN = os.environ.get("GITHUB_TOKEN")
CODEBERG_TOKEN = os.environ.get("CODEBERG_TOKEN")

@app.route('/')
def home():
    return jsonify({"status": "running", "service": "Codeberg Auto-Sync"})

@app.route('/sync')
def sync():
    if not GITHUB_TOKEN or not CODEBERG_TOKEN:
        return jsonify({"error": "Tokens not configured"}), 500
    
    headers = {"Authorization": f"token {GITHUB_TOKEN}"}
    repos = requests.get("https://api.github.com/users/Newton-ait/repos?per_page=100", headers=headers).json()
    
    results = []
    for repo in repos:
        repo_name = repo["name"]
        mirror_url = f"https://codeberg.org/api/v1/repos/Newton-ait/{repo_name}/mirror"
        payload = {"remote_addr": f"https://github.com/Newton-ait/{repo_name}.git", "interval": "1h"}
        response = requests.post(mirror_url, json=payload, headers={"Authorization": f"token {CODEBERG_TOKEN}"})
        results.append({"repo": repo_name, "status": "success" if response.status_code in [200,201,409] else "failed"})
    
    return jsonify({"synced": len(results), "results": results})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=int(os.environ.get("PORT", 5000)))

#!/usr/bin/env python3
"""
Post comment to GitHub Issue
"""

import os
import sys
import argparse
import requests

def post_github_comment(issue_number: int, repo: str, token: str, body: str):
    """Post comment to GitHub issue"""
    url = f"https://api.github.com/repos/{repo}/issues/{issue_number}/comments"
    
    headers = {
        "Authorization": f"token {token}",
        "Accept": "application/vnd.github.v3+json"
    }
    
    data = {
        "body": body
    }
    
    response = requests.post(url, headers=headers, json=data)
    
    if response.status_code == 201:
        print(f"✅ Comment posted to issue #{issue_number}")
        return True
    else:
        print(f"❌ Failed to post comment: {response.status_code}")
        print(response.text)
        return False

def main():
    parser = argparse.ArgumentParser(description="Post comment to GitHub Issue")
    parser.add_argument("--issue-number", type=int, required=True)
    parser.add_argument("--success", required=True)
    parser.add_argument("--changes", required=True)
    parser.add_argument("--repository", default=os.getenv("GITHUB_REPOSITORY"))
    
    args = parser.parse_args()
    
    token = os.getenv("GITHUB_TOKEN")
    if not token:
        print("❌ GITHUB_TOKEN not set")
        sys.exit(1)
    
    if not args.repository:
        print("❌ Repository not specified")
        sys.exit(1)
    
    # Post comment
    success = post_github_comment(
        issue_number=args.issue_number,
        repo=args.repository,
        token=token,
        body=args.changes
    )
    
    sys.exit(0 if success else 1)

if __name__ == "__main__":
    main()
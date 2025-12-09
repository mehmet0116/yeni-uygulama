#!/usr/bin/env python3
"""
🤖 DeepSeek AI Enterprise Architect - Main Handler
Version: 4.0
"""

import os
import sys
import json
import argparse
import requests
from typing import Dict, List, Any, Optional
from datetime import datetime
import base64
import re

# Add project root to path
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

class DeepSeekHandler:
    """DeepSeek AI API Handler for GitHub Issues"""
    
    def __init__(self, api_key: str):
        self.api_key = api_key
        self.base_url = "https://api.deepseek.com/v1"
        self.headers = {
            "Authorization": f"Bearer {api_key}",
            "Content-Type": "application/json"
        }
        self.safe_dirs = [".github", ".git"]
        self.protected_files = [
            ".gitignore",
            "README.md",
            ".github/workflows/deepseek.yml",
            "requirements.txt",
            "package.json",
            "package-lock.json",
            "Gemfile",
            "Gemfile.lock",
            "go.mod",
            "go.sum",
            "Cargo.toml",
            "Cargo.lock",
            "deepseek_handler.py"
        ]
        
    def get_issue_content(self, issue_number: int, repo: str, token: str) -> Dict[str, Any]:
        """Fetch issue content from GitHub API"""
        url = f"https://api.github.com/repos/{repo}/issues/{issue_number}"
        headers = {"Authorization": f"token {token}"}
        
        response = requests.get(url, headers=headers)
        response.raise_for_status()
        return response.json()
    
    def get_issue_comments(self, issue_number: int, repo: str, token: str) -> List[Dict]:
        """Fetch all comments for an issue"""
        url = f"https://api.github.com/repos/{repo}/issues/{issue_number}/comments"
        headers = {"Authorization": f"token {token}"}
        
        response = requests.get(url, headers=headers)
        response.raise_for_status()
        return response.json()
    
    def call_deepseek_api(self, prompt: str, context: str = "") -> str:
        """Call DeepSeek API with the given prompt"""
        messages = [
            {
                "role": "system",
                "content": """Sen DeepSeek ULTRA Enterprise Architect v4.0'sın. 
                Kullanıcıların GitHub Issue'larından gelen proje taleplerini işliyorsun.
                
                GÖREV KURALLARI:
                1. Talebi analiz et ve proje yapısını planla
                2. Sadece gerekli dosyaları oluştur
                3. Profesyonel kod yapısı kullan
                4. Test dosyaları ekle
                5. Dokümantasyon ekle
                6. Eksikleri tamamla
                
                ÇIKTI FORMATI:
                ---FILENAME: yol/dosya_adi.uzantı---
                [Kod]
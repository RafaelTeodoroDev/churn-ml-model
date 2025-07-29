#!/usr/bin/env python3
"""
API REST para Modelo de Predição de Churn - Vercel
===================================================

Este arquivo é o entry point para o Vercel em /api/
"""

from http.server import BaseHTTPRequestHandler
import json
from datetime import datetime

class handler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header('Content-type', 'application/json')
        self.send_header('Access-Control-Allow-Origin', '*')
        self.send_header('Access-Control-Allow-Methods', 'GET, POST, OPTIONS')
        self.send_header('Access-Control-Allow-Headers', 'Content-Type')
        self.end_headers()

        if self.path == '/api/':
            response = {
                "message": "Churn Prediction API",
                "version": "1.0.0",
                "timestamp": datetime.now().isoformat()
            }
        elif self.path == '/api/health':
            response = {
                "status": "healthy",
                "timestamp": datetime.now().isoformat(),
                "version": "1.0.0"
            }
        elif self.path == '/api/test':
            response = {
                "message": "API funcionando!",
                "timestamp": datetime.now().isoformat()
            }
        else:
            response = {
                "error": "Not found",
                "path": self.path
            }

        self.wfile.write(json.dumps(response).encode())

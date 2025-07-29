#!/usr/bin/env python3
"""
Servidor simples para servir os arquivos frontend
"""

import http.server
import socketserver
import os
import webbrowser
from pathlib import Path

# Configuração
PORT = 3000
DIRECTORY = Path(__file__).parent

class CustomHTTPRequestHandler(http.server.SimpleHTTPRequestHandler):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, directory=str(DIRECTORY), **kwargs)

    def end_headers(self):
        # Adicionar headers CORS para permitir requisições da API
        self.send_header('Access-Control-Allow-Origin', '*')
        self.send_header('Access-Control-Allow-Methods', 'GET, POST, OPTIONS')
        self.send_header('Access-Control-Allow-Headers', 'Content-Type')
        super().end_headers()

    def do_OPTIONS(self):
        self.send_response(200)
        self.end_headers()

def main():
    """Função principal"""
    os.chdir(DIRECTORY)

    with socketserver.TCPServer(("", PORT), CustomHTTPRequestHandler) as httpd:
        print(f"🚀 Servidor frontend iniciado em http://localhost:{PORT}")
        print(f"📁 Diretório: {DIRECTORY}")
        print(f"🌐 Abrindo navegador automaticamente...")
        print(f"⏹️  Pressione Ctrl+C para parar o servidor")

        # Abrir navegador automaticamente
        try:
            webbrowser.open(f'http://localhost:{PORT}')
        except:
            print(f"⚠️  Não foi possível abrir o navegador automaticamente")
            print(f"🌐 Acesse manualmente: http://localhost:{PORT}")

        try:
            httpd.serve_forever()
        except KeyboardInterrupt:
            print(f"\n👋 Servidor parado")

if __name__ == "__main__":
    main()

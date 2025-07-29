#!/usr/bin/env python3
"""
Script para iniciar a aplicação completa (API + Frontend)
"""

import subprocess
import time
import sys
import os
from pathlib import Path

def check_port(port):
    """Verifica se uma porta está em uso"""
    import socket
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    result = sock.connect_ex(('localhost', port))
    sock.close()
    return result == 0

def wait_for_api():
    """Aguarda a API estar pronta"""
    print("⏳ Aguardando API estar pronta...")
    max_attempts = 30
    attempts = 0

    while attempts < max_attempts:
        if check_port(8000):
            print("✅ API está pronta!")
            return True
        time.sleep(1)
        attempts += 1
        print(f"   Tentativa {attempts}/{max_attempts}")

    print("❌ API não respondeu em 30 segundos")
    return False

def main():
    """Função principal"""
    print("🚀 Iniciando aplicação completa...")
    print("=" * 50)

    # Verificar se estamos no diretório correto
    if not Path("api.py").exists():
        print("❌ Execute este script no diretório raiz do projeto")
        sys.exit(1)

    # Verificar se o frontend existe
    if not Path("frontend").exists():
        print("❌ Diretório frontend não encontrado")
        sys.exit(1)

    # Iniciar API em background
    print("🔧 Iniciando API...")
    api_process = subprocess.Popen([
        sys.executable, "api.py"
    ], stdout=subprocess.PIPE, stderr=subprocess.PIPE)

    # Aguardar API estar pronta
    if not wait_for_api():
        print("❌ Falha ao iniciar API")
        api_process.terminate()
        sys.exit(1)

    # Iniciar frontend em background
    print("🎨 Iniciando frontend...")
    frontend_process = subprocess.Popen([
        sys.executable, "frontend/server.py"
    ], stdout=subprocess.PIPE, stderr=subprocess.PIPE)

    # Aguardar frontend estar pronta
    print("⏳ Aguardando frontend estar pronta...")
    time.sleep(3)

    if check_port(3000):
        print("✅ Frontend está pronta!")
    else:
        print("⚠️  Frontend pode não estar pronta ainda")

    print("\n🎉 Aplicação iniciada com sucesso!")
    print("=" * 50)
    print("📊 API: http://localhost:8000")
    print("📚 Docs: http://localhost:8000/docs")
    print("🎨 Frontend: http://localhost:3000")
    print("=" * 50)
    print("⏹️  Pressione Ctrl+C para parar ambos os serviços")

    try:
        # Manter os processos rodando
        while True:
            time.sleep(1)

            # Verificar se os processos ainda estão rodando
            if api_process.poll() is not None:
                print("❌ API parou inesperadamente")
                break

            if frontend_process.poll() is not None:
                print("❌ Frontend parou inesperadamente")
                break

    except KeyboardInterrupt:
        print("\n🛑 Parando serviços...")

        # Parar API
        if api_process.poll() is None:
            api_process.terminate()
            print("✅ API parada")

        # Parar frontend
        if frontend_process.poll() is None:
            frontend_process.terminate()
            print("✅ Frontend parado")

        print("👋 Aplicação parada")

if __name__ == "__main__":
    main()

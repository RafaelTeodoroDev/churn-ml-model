#!/usr/bin/env python3
"""
API REST para Modelo de Predição de Churn - Vercel
===================================================

Este arquivo é o entry point para o Vercel.
"""

import sys
import pathlib

# Adicionar o diretório pai ao path
sys.path.append(str(pathlib.Path(__file__).parent.parent))

# Importar a API do arquivo vercel_api.py
from api.vercel_api import app

# Handler para o Vercel
handler = app

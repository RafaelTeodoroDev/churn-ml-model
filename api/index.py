#!/usr/bin/env python3
"""
API REST para Modelo de Predição de Churn - Vercel
===================================================

Este arquivo é o entry point para o Vercel em /api/
"""

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from datetime import datetime

# Inicializar FastAPI
app = FastAPI(
    title="Churn Prediction API",
    description="API para predição de churn de clientes",
    version="1.0.0"
)

# Configurar CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
async def root():
    """Endpoint raiz"""
    return {
        "message": "Churn Prediction API",
        "version": "1.0.0",
        "timestamp": datetime.now().isoformat()
    }

@app.get("/health")
async def health_check():
    """Health check da API"""
    return {
        "status": "healthy",
        "timestamp": datetime.now().isoformat(),
        "version": "1.0.0"
    }

@app.get("/test")
async def test():
    """Endpoint de teste"""
    return {
        "message": "API funcionando!",
        "timestamp": datetime.now().isoformat()
    }

# Handler para o Vercel
handler = app

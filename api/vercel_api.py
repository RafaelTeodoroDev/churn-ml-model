#!/usr/bin/env python3
"""
API REST para Modelo de Predição de Churn - Vercel
===================================================

Esta API permite consumir o modelo de predição de churn via HTTP requests.
Versão otimizada para Vercel com algoritmo mock.
"""

from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from typing import List, Optional, Dict, Any
import json
from datetime import datetime

# Inicializar FastAPI
app = FastAPI(
    title="Churn Prediction API",
    description="API para predição de churn de clientes",
    version="1.0.0",
    docs_url="/docs",
    redoc_url="/redoc"
)

# Configurar CORS para permitir todas as origens
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Modelos Pydantic para validação de dados
class CustomerData(BaseModel):
    """Modelo para dados do cliente"""
    age: int
    gender: str
    subscription_length_months: int
    monthly_charge: float
    total_charges: float
    contract_type: str
    payment_method: str
    paperless_billing: str
    tech_support: str
    online_security: str
    online_backup: str
    device_protection: str
    premium_tech_support: str
    streaming_tv: str
    streaming_movies: str
    streaming_music: str
    unlimited_data: str
    internet_service_type: str
    phone_service: str
    multiple_lines: str
    internet_service: str
    avg_monthly_gb_download: float
    avg_monthly_gb_download_6_months: float
    avg_monthly_gb_download_12_months: float
    monthly_usage_gb: float
    overage_fees: float
    roaming_charges: float
    international_plan: str
    voice_mail_plan: str
    number_vmail_messages: int
    number_customer_service_calls: int
    number_calls_placed: int
    number_calls_received: int
    total_minutes_used: int
    total_data_used_gb: float
    avg_call_duration_minutes: float
    avg_call_duration_6_months: float
    avg_call_duration_12_months: float
    payment_delay_days: int
    late_payment_count: int
    missed_payment_count: int
    contract_renewal_days: int
    days_since_last_upgrade: int
    days_since_last_downgrade: int
    days_since_last_complaint: int
    complaint_count: int
    positive_feedback_count: int
    negative_feedback_count: int
    social_media_mentions: int
    satisfaction_score: int

class PredictionResponse(BaseModel):
    """Modelo para resposta da predição"""
    customer_id: Optional[str] = None
    churn_probability: float
    risk_level: str
    risk_description: str
    recommendations: List[str]
    timestamp: str
    model_info: Dict[str, Any]

class BatchPredictionRequest(BaseModel):
    """Modelo para predição em lote"""
    customers: List[CustomerData]

class BatchPredictionResponse(BaseModel):
    """Modelo para resposta de predição em lote"""
    predictions: List[PredictionResponse]
    total_customers: int
    average_probability: float
    risk_distribution: Dict[str, int]

class HealthResponse(BaseModel):
    """Modelo para resposta de health check"""
    status: str
    model_loaded: bool
    timestamp: str
    version: str

def get_risk_level(probability: float) -> tuple[str, str]:
    """Determina o nível de risco baseado na probabilidade"""
    if probability < 0.4:
        return "🟢 BAIXO RISCO", "Cliente estável"
    elif probability < 0.7:
        return "🟡 RISCO MÉDIO", "Monitoramento recomendado"
    else:
        return "🔴 ALTO RISCO", "Ação imediata necessária"

def get_recommendations(probability: float, customer_data: dict) -> List[str]:
    """Gera recomendações baseadas na probabilidade de churn"""
    recommendations = []

    if probability > 0.7:
        recommendations.extend([
            "🚨 Contato imediato com o cliente",
            "💎 Proposta de desconto especial",
            "📞 Ligação direta do gerente",
            "🎁 Programa de fidelidade premium"
        ])
    elif probability > 0.4:
        recommendations.extend([
            "📧 Envio de material educativo sobre serviços",
            "🎯 Campanha de retenção personalizada",
            "📊 Monitoramento semanal do comportamento",
            "💬 Proposta de upgrade de plano"
        ])
    else:
        recommendations.extend([
            "✅ Manter estratégia atual",
            "📱 Comunicação regular sobre novos recursos",
            "🎉 Programa de recompensas",
            "📈 Análise de oportunidades de upsell"
        ])

    # Recomendações específicas baseadas nos dados do cliente
    if customer_data['contract_type'] == 'Month-to-month':
        recommendations.append("📋 Proposta de contrato anual com desconto")

    if customer_data['number_customer_service_calls'] > 5:
        recommendations.append("🔧 Melhoria no suporte técnico")

    if customer_data['satisfaction_score'] < 5:
        recommendations.append("📞 Contato para entender insatisfação")

    if customer_data['late_payment_count'] > 0:
        recommendations.append("💳 Revisão das opções de pagamento")

    return recommendations

def predict_churn_mock(customer_data: dict) -> float:
    """Prediz churn usando algoritmo mock baseado nos dados do cliente"""
    probability = 0.3  # Base probability

    # Fatores que aumentam a probabilidade de churn
    if customer_data['contract_type'] == 'Month-to-month':
        probability += 0.2

    if customer_data['satisfaction_score'] < 5:
        probability += 0.25

    if customer_data['number_customer_service_calls'] > 5:
        probability += 0.15

    if customer_data['late_payment_count'] > 0:
        probability += 0.1

    if customer_data['monthly_charge'] > 80:
        probability += 0.1

    if customer_data['age'] < 30:
        probability += 0.05

    # Fatores que diminuem a probabilidade de churn
    if customer_data['contract_type'] == 'Two year':
        probability -= 0.15

    if customer_data['satisfaction_score'] >= 8:
        probability -= 0.2

    if customer_data['tech_support'] == 'Yes':
        probability -= 0.1

    if customer_data['paperless_billing'] == 'Yes':
        probability -= 0.05

    # Garantir que a probabilidade esteja entre 0 e 1
    return max(0.1, min(0.9, probability))

@app.get("/", response_model=Dict[str, str])
async def root():
    """Endpoint raiz"""
    return {
        "message": "Churn Prediction API",
        "version": "1.0.0",
        "docs": "/docs",
        "note": "Usando modelo mock para compatibilidade com Vercel"
    }

@app.get("/health", response_model=HealthResponse)
async def health_check():
    """Health check da API"""
    return HealthResponse(
        status="healthy",
        model_loaded=False,  # Sempre False pois usamos mock
        timestamp=datetime.now().isoformat(),
        version="1.0.0"
    )

@app.post("/predict", response_model=PredictionResponse)
async def predict_churn(customer: CustomerData):
    """Prediz churn para um cliente individual"""
    try:
        # Converter para dict
        customer_data = customer.dict()

        # Fazer predição usando algoritmo mock
        probability = predict_churn_mock(customer_data)

        # Determinar nível de risco
        risk_level, risk_description = get_risk_level(probability)

        # Gerar recomendações
        recommendations = get_recommendations(probability, customer_data)

        # Informações do modelo
        model_info = {
            "model_type": "Mock Algorithm",
            "accuracy": 0.705,
            "auc": 0.7467,
            "features_used": 50,
            "note": "Algoritmo mock para demonstração"
        }

        return PredictionResponse(
            churn_probability=probability,
            risk_level=risk_level,
            risk_description=risk_description,
            recommendations=recommendations,
            timestamp=datetime.now().isoformat(),
            model_info=model_info
        )

    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Erro na predição: {str(e)}")

@app.post("/predict/batch", response_model=BatchPredictionResponse)
async def predict_churn_batch(request: BatchPredictionRequest):
    """Prediz churn para múltiplos clientes"""
    try:
        predictions = []
        total_probability = 0
        risk_distribution = {"🟢 BAIXO RISCO": 0, "🟡 RISCO MÉDIO": 0, "🔴 ALTO RISCO": 0}

        for i, customer in enumerate(request.customers):
            customer_data = customer.dict()
            probability = predict_churn_mock(customer_data)
            risk_level, risk_description = get_risk_level(probability)
            recommendations = get_recommendations(probability, customer_data)

            prediction = PredictionResponse(
                customer_id=f"customer_{i+1}",
                churn_probability=probability,
                risk_level=risk_level,
                risk_description=risk_description,
                recommendations=recommendations,
                timestamp=datetime.now().isoformat(),
                model_info={
                    "model_type": "Mock Algorithm",
                    "accuracy": 0.705,
                    "auc": 0.7467,
                    "features_used": 50,
                    "note": "Algoritmo mock para demonstração"
                }
            )

            predictions.append(prediction)
            total_probability += probability
            risk_distribution[risk_level] += 1

        average_probability = total_probability / len(request.customers)

        return BatchPredictionResponse(
            predictions=predictions,
            total_customers=len(request.customers),
            average_probability=average_probability,
            risk_distribution=risk_distribution
        )

    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Erro na predição em lote: {str(e)}")

@app.get("/model/info")
async def get_model_info():
    """Retorna informações sobre o modelo"""
    return {
        "model_type": "Mock Algorithm",
        "accuracy": 0.705,
        "auc": 0.7467,
        "features_count": 50,
        "features": ["age", "subscription_length_months", "monthly_charge", "satisfaction_score"],
        "dataset_size": 1000,
        "churn_rate": 0.645,
        "note": "Algoritmo mock para demonstração - compatível com Vercel"
    }

@app.get("/features/importance")
async def get_feature_importance():
    """Retorna a importância das features"""
    return {
        "top_features": [
            {"feature": "contract_type", "importance": 0.058787},
            {"feature": "satisfaction_score", "importance": 0.050098},
            {"feature": "monthly_charge", "importance": 0.047574},
            {"feature": "number_customer_service_calls", "importance": 0.045123},
            {"feature": "late_payment_count", "importance": 0.042891}
        ],
        "total_features": 50,
        "note": "Importância baseada em algoritmo mock"
    }

@app.post("/sample/customer")
async def get_sample_customer():
    """Retorna um cliente de exemplo"""
    sample_customer = {
        "age": 35,
        "gender": "M",
        "subscription_length_months": 12,
        "monthly_charge": 45.20,
        "total_charges": 542.40,
        "contract_type": "One year",
        "payment_method": "Bank transfer",
        "paperless_billing": "Yes",
        "tech_support": "No",
        "online_security": "No",
        "online_backup": "No",
        "device_protection": "No",
        "premium_tech_support": "No",
        "streaming_tv": "No",
        "streaming_movies": "No",
        "streaming_music": "No",
        "unlimited_data": "No",
        "internet_service_type": "DSL",
        "phone_service": "Yes",
        "multiple_lines": "No",
        "internet_service": "Yes",
        "avg_monthly_gb_download": 12.5,
        "avg_monthly_gb_download_6_months": 15.2,
        "avg_monthly_gb_download_12_months": 13.8,
        "monthly_usage_gb": 200,
        "overage_fees": 0,
        "roaming_charges": 0,
        "international_plan": "No",
        "voice_mail_plan": "No",
        "number_vmail_messages": 0,
        "number_customer_service_calls": 5,
        "number_calls_placed": 12,
        "number_calls_received": 8,
        "total_minutes_used": 300,
        "total_data_used_gb": 5.2,
        "avg_call_duration_minutes": 4.8,
        "avg_call_duration_6_months": 5.5,
        "avg_call_duration_12_months": 3,
        "payment_delay_days": 1,
        "late_payment_count": 0,
        "missed_payment_count": 0,
        "contract_renewal_days": 365,
        "days_since_last_upgrade": 90,
        "days_since_last_downgrade": 0,
        "days_since_last_complaint": 30,
        "complaint_count": 2,
        "positive_feedback_count": 1,
        "negative_feedback_count": 0,
        "social_media_mentions": 0,
        "satisfaction_score": 5
    }

    return sample_customer

# Para compatibilidade com Vercel
app.debug = True

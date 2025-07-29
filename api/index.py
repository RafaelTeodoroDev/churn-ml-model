#!/usr/bin/env python3
"""
API REST para Modelo de Predição de Churn - Vercel
===================================================

Este arquivo é o entry point para o Vercel em /api/
Versão HTTP handler básico que funciona no Vercel.
"""

from http.server import BaseHTTPRequestHandler
import json
from datetime import datetime
from urllib.parse import urlparse, parse_qs

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
                "timestamp": datetime.now().isoformat(),
                "note": "Usando modelo mock para compatibilidade com Vercel"
            }
        elif self.path == '/api/health':
            response = {
                "status": "healthy",
                "model_loaded": False,
                "timestamp": datetime.now().isoformat(),
                "version": "1.0.0"
            }
        elif self.path == '/api/model/info':
            response = {
                "model_type": "Mock Algorithm",
                "accuracy": 0.705,
                "auc": 0.7467,
                "features_count": 50,
                "features": ["age", "subscription_length_months", "monthly_charge", "satisfaction_score"],
                "dataset_size": 1000,
                "churn_rate": 0.645,
                "note": "Algoritmo mock para demonstração - compatível com Vercel"
            }
        elif self.path == '/api/features/importance':
            response = {
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
        else:
            response = {
                "error": "Not found",
                "path": self.path,
                "available_endpoints": [
                    "/api/",
                    "/api/health",
                    "/api/model/info",
                    "/api/features/importance",
                    "/api/sample/customer",
                    "/api/predict"
                ]
            }

        self.wfile.write(json.dumps(response).encode())

    def do_POST(self):
        self.send_response(200)
        self.send_header('Content-type', 'application/json')
        self.send_header('Access-Control-Allow-Origin', '*')
        self.send_header('Access-Control-Allow-Methods', 'GET, POST, OPTIONS')
        self.send_header('Access-Control-Allow-Headers', 'Content-Type')
        self.end_headers()

        if self.path == '/api/sample/customer':
            response = {
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
        elif self.path == '/api/predict':
            # Ler o corpo da requisição
            content_length = int(self.headers['Content-Length'])
            post_data = self.rfile.read(content_length)

            try:
                customer_data = json.loads(post_data.decode('utf-8'))

                # Algoritmo mock de predição
                probability = self.predict_churn_mock(customer_data)
                risk_level, risk_description = self.get_risk_level(probability)
                recommendations = self.get_recommendations(probability, customer_data)

                response = {
                    "customer_id": None,
                    "churn_probability": probability,
                    "risk_level": risk_level,
                    "risk_description": risk_description,
                    "recommendations": recommendations,
                    "timestamp": datetime.now().isoformat(),
                    "model_info": {
                        "model_type": "Mock Algorithm",
                        "accuracy": 0.705,
                        "auc": 0.7467,
                        "features_used": 50,
                        "note": "Algoritmo mock para demonstração"
                    }
                }
            except Exception as e:
                response = {
                    "error": f"Erro na predição: {str(e)}",
                    "timestamp": datetime.now().isoformat()
                }
        else:
            response = {
                "error": "Not found",
                "path": self.path,
                "available_endpoints": [
                    "/api/",
                    "/api/health",
                    "/api/model/info",
                    "/api/features/importance",
                    "/api/sample/customer",
                    "/api/predict"
                ]
            }

        self.wfile.write(json.dumps(response).encode())

    def do_OPTIONS(self):
        self.send_response(200)
        self.send_header('Access-Control-Allow-Origin', '*')
        self.send_header('Access-Control-Allow-Methods', 'GET, POST, OPTIONS')
        self.send_header('Access-Control-Allow-Headers', 'Content-Type')
        self.end_headers()

    def predict_churn_mock(self, customer_data: dict) -> float:
        """Prediz churn usando algoritmo mock baseado nos dados do cliente"""
        probability = 0.3  # Base probability

        # Fatores que aumentam a probabilidade de churn
        if customer_data.get('contract_type') == 'Month-to-month':
            probability += 0.2

        if customer_data.get('satisfaction_score', 10) < 5:
            probability += 0.25

        if customer_data.get('number_customer_service_calls', 0) > 5:
            probability += 0.15

        if customer_data.get('late_payment_count', 0) > 0:
            probability += 0.1

        if customer_data.get('monthly_charge', 0) > 80:
            probability += 0.1

        if customer_data.get('age', 0) < 30:
            probability += 0.05

        # Fatores que diminuem a probabilidade de churn
        if customer_data.get('contract_type') == 'Two year':
            probability -= 0.15

        if customer_data.get('satisfaction_score', 0) >= 8:
            probability -= 0.2

        if customer_data.get('tech_support') == 'Yes':
            probability -= 0.1

        if customer_data.get('paperless_billing') == 'Yes':
            probability -= 0.05

        # Garantir que a probabilidade esteja entre 0 e 1
        return max(0.1, min(0.9, probability))

    def get_risk_level(self, probability: float) -> tuple[str, str]:
        """Determina o nível de risco baseado na probabilidade"""
        if probability < 0.4:
            return "🟢 BAIXO RISCO", "Cliente estável"
        elif probability < 0.7:
            return "🟡 RISCO MÉDIO", "Monitoramento recomendado"
        else:
            return "🔴 ALTO RISCO", "Ação imediata necessária"

    def get_recommendations(self, probability: float, customer_data: dict) -> list[str]:
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
        if customer_data.get('contract_type') == 'Month-to-month':
            recommendations.append("📋 Proposta de contrato anual com desconto")

        if customer_data.get('number_customer_service_calls', 0) > 5:
            recommendations.append("🔧 Melhoria no suporte técnico")

        if customer_data.get('satisfaction_score', 10) < 5:
            recommendations.append("📞 Contato para entender insatisfação")

        if customer_data.get('late_payment_count', 0) > 0:
            recommendations.append("💳 Revisão das opções de pagamento")

        return recommendations

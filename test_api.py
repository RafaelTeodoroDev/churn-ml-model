#!/usr/bin/env python3
"""
Script de Teste para a API de Predição de Churn
================================================

Este script demonstra como testar a API usando curl e Python requests.
"""

import requests
import json
import time
from datetime import datetime

# Configuração da API
API_BASE_URL = "http://localhost:8000"

def test_health_check():
    """Testa o health check da API"""
    print("🏥 Testando Health Check...")

    # Com curl
    print("\n📋 Comando curl:")
    print(f"curl -X GET {API_BASE_URL}/health")

    # Com Python requests
    try:
        response = requests.get(f"{API_BASE_URL}/health")
        if response.status_code == 200:
            data = response.json()
            print(f"\n✅ Health Check - Status: {data['status']}")
            print(f"   Modelo carregado: {data['model_loaded']}")
            print(f"   Timestamp: {data['timestamp']}")
            return True
        else:
            print(f"❌ Health Check falhou: {response.status_code}")
            return False
    except requests.exceptions.ConnectionError:
        print("❌ Não foi possível conectar à API. Certifique-se de que ela está rodando.")
        return False

def test_model_info():
    """Testa as informações do modelo"""
    print("\n📊 Testando informações do modelo...")

    # Com curl
    print("\n📋 Comando curl:")
    print(f"curl -X GET {API_BASE_URL}/model/info")

    # Com Python requests
    try:
        response = requests.get(f"{API_BASE_URL}/model/info")
        if response.status_code == 200:
            data = response.json()
            print(f"\n✅ Informações do Modelo:")
            print(f"   Tipo: {data['model_type']}")
            print(f"   Acurácia: {data['accuracy']}")
            print(f"   AUC: {data['auc']}")
            print(f"   Features: {data['features_count']}")
            return True
        else:
            print(f"❌ Falha ao obter informações do modelo: {response.status_code}")
            return False
    except Exception as e:
        print(f"❌ Erro: {e}")
        return False

def test_sample_customer():
    """Testa a obtenção de um cliente de exemplo"""
    print("\n👤 Testando cliente de exemplo...")

    # Com curl
    print("\n📋 Comando curl:")
    print(f"curl -X POST {API_BASE_URL}/sample/customer")

    # Com Python requests
    try:
        response = requests.post(f"{API_BASE_URL}/sample/customer")
        if response.status_code == 200:
            data = response.json()
            print(f"\n✅ Cliente de exemplo obtido:")
            print(f"   Idade: {data['age']}")
            print(f"   Gênero: {data['gender']}")
            print(f"   Contrato: {data['contract_type']}")
            print(f"   Valor mensal: R$ {data['monthly_charge']}")
            return data
        else:
            print(f"❌ Falha ao obter cliente de exemplo: {response.status_code}")
            return None
    except Exception as e:
        print(f"❌ Erro: {e}")
        return None

def test_single_prediction(customer_data):
    """Testa predição individual"""
    print("\n🎯 Testando predição individual...")

    # Preparar dados para curl
    customer_json = json.dumps(customer_data, indent=2)

    # Com curl
    print("\n📋 Comando curl:")
    print(f"curl -X POST {API_BASE_URL}/predict \\")
    print("  -H \"Content-Type: application/json\" \\")
    print("  -d @customer_data.json")

    # Salvar dados em arquivo para curl
    with open("customer_data.json", "w") as f:
        json.dump(customer_data, f, indent=2)

    # Com Python requests
    try:
        response = requests.post(
            f"{API_BASE_URL}/predict",
            json=customer_data,
            headers={"Content-Type": "application/json"}
        )

        if response.status_code == 200:
            data = response.json()
            print(f"\n✅ Predição realizada:")
            print(f"   Probabilidade de churn: {data['churn_probability']:.2%}")
            print(f"   Nível de risco: {data['risk_level']}")
            print(f"   Descrição: {data['risk_description']}")
            print(f"   Recomendações: {len(data['recommendations'])} itens")
            return data
        else:
            print(f"❌ Falha na predição: {response.status_code}")
            print(f"   Resposta: {response.text}")
            return None
    except Exception as e:
        print(f"❌ Erro: {e}")
        return None

def test_batch_prediction():
    """Testa predição em lote"""
    print("\n📦 Testando predição em lote...")

    # Criar múltiplos clientes
    customers = [
        {
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
        },
        {
            "age": 28,
            "gender": "F",
            "subscription_length_months": 3,
            "monthly_charge": 19.99,
            "total_charges": 59.97,
            "contract_type": "Month-to-month",
            "payment_method": "Electronic check",
            "paperless_billing": "No",
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
            "phone_service": "No",
            "multiple_lines": "No",
            "internet_service": "No",
            "avg_monthly_gb_download": 5.2,
            "avg_monthly_gb_download_6_months": 6.1,
            "avg_monthly_gb_download_12_months": 5.8,
            "monthly_usage_gb": 100,
            "overage_fees": 0,
            "roaming_charges": 0,
            "international_plan": "No",
            "voice_mail_plan": "No",
            "number_vmail_messages": 0,
            "number_customer_service_calls": 12,
            "number_calls_placed": 8,
            "number_calls_received": 3,
            "total_minutes_used": 200,
            "total_data_used_gb": 4.2,
            "avg_call_duration_minutes": 3.9,
            "avg_call_duration_6_months": 4.1,
            "avg_call_duration_12_months": 15,
            "payment_delay_days": 3,
            "late_payment_count": 2,
            "missed_payment_count": 1,
            "contract_renewal_days": 90,
            "days_since_last_upgrade": 30,
            "days_since_last_downgrade": 0,
            "days_since_last_complaint": 5,
            "complaint_count": 4,
            "positive_feedback_count": 3,
            "negative_feedback_count": 2,
            "social_media_mentions": 2,
            "satisfaction_score": 2
        }
    ]

    batch_data = {"customers": customers}

    # Salvar dados em arquivo para curl
    with open("batch_data.json", "w") as f:
        json.dump(batch_data, f, indent=2)

    # Com curl
    print("\n📋 Comando curl:")
    print(f"curl -X POST {API_BASE_URL}/predict/batch \\")
    print("  -H \"Content-Type: application/json\" \\")
    print("  -d @batch_data.json")

    # Com Python requests
    try:
        response = requests.post(
            f"{API_BASE_URL}/predict/batch",
            json=batch_data,
            headers={"Content-Type": "application/json"}
        )

        if response.status_code == 200:
            data = response.json()
            print(f"\n✅ Predição em lote realizada:")
            print(f"   Total de clientes: {data['total_customers']}")
            print(f"   Probabilidade média: {data['average_probability']:.2%}")
            print(f"   Distribuição de risco: {data['risk_distribution']}")
            return data
        else:
            print(f"❌ Falha na predição em lote: {response.status_code}")
            print(f"   Resposta: {response.text}")
            return None
    except Exception as e:
        print(f"❌ Erro: {e}")
        return None

def test_feature_importance():
    """Testa a obtenção da importância das features"""
    print("\n🔍 Testando importância das features...")

    # Com curl
    print("\n📋 Comando curl:")
    print(f"curl -X GET {API_BASE_URL}/features/importance")

    # Com Python requests
    try:
        response = requests.get(f"{API_BASE_URL}/features/importance")
        if response.status_code == 200:
            data = response.json()
            print(f"\n✅ Importância das features:")
            print(f"   Total de features: {data['total_features']}")
            print(f"   Top 5 features:")
            for i, feature in enumerate(data['top_features'][:5], 1):
                print(f"   {i}. {feature['feature']}: {feature['importance']:.4f}")
            return data
        else:
            print(f"❌ Falha ao obter importância das features: {response.status_code}")
            return None
    except Exception as e:
        print(f"❌ Erro: {e}")
        return None

def main():
    """Função principal de teste"""
    print("🚀 TESTE DA API DE PREDIÇÃO DE CHURN")
    print("=" * 60)

    # Aguardar um pouco para a API inicializar
    print("⏳ Aguardando inicialização da API...")
    time.sleep(3)

    # Testar health check
    if not test_health_check():
        print("\n❌ API não está disponível. Execute primeiro:")
        print("   python3 api.py")
        return

    # Testar informações do modelo
    test_model_info()

    # Testar cliente de exemplo
    sample_customer = test_sample_customer()

    # Testar predição individual
    if sample_customer:
        test_single_prediction(sample_customer)

    # Testar predição em lote
    test_batch_prediction()

    # Testar importância das features
    test_feature_importance()

    print("\n✅ Testes concluídos!")
    print("\n📚 Documentação da API:")
    print(f"   Swagger UI: {API_BASE_URL}/docs")
    print(f"   ReDoc: {API_BASE_URL}/redoc")

if __name__ == "__main__":
    main()

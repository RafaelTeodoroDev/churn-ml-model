# 🚀 Guia da API de Predição de Churn

## 📋 Visão Geral

Esta API REST permite consumir o modelo de predição de churn via HTTP requests. A API é construída com FastAPI e oferece endpoints para predições individuais e em lote.

## 🚀 Como Iniciar a API

### 1. Instalar Dependências
```bash
pip3 install -r requirements.txt
```

### 2. Iniciar a API
```bash
python3 api.py
```

A API estará disponível em: `http://localhost:8000`

## 📚 Documentação Interativa

- **Swagger UI**: http://localhost:8000/docs
- **ReDoc**: http://localhost:8000/redoc

## 🔧 Endpoints Disponíveis

### 1. Health Check
**GET** `/health`

Verifica se a API está funcionando e se o modelo foi carregado.

```bash
curl -X GET http://localhost:8000/health
```

**Resposta:**
```json
{
  "status": "healthy",
  "model_loaded": true,
  "timestamp": "2025-01-27T10:30:00",
  "version": "1.0.0"
}
```

### 2. Informações do Modelo
**GET** `/model/info`

Retorna informações sobre o modelo treinado.

```bash
curl -X GET http://localhost:8000/model/info
```

**Resposta:**
```json
{
  "model_type": "Random Forest",
  "accuracy": 0.705,
  "auc": 0.7467,
  "features_count": 50,
  "features": ["contract_type", "satisfaction_score", "monthly_charge", ...],
  "dataset_size": 1000,
  "churn_rate": 0.645
}
```

### 3. Cliente de Exemplo
**POST** `/sample/customer`

Retorna um cliente de exemplo para teste.

```bash
curl -X POST http://localhost:8000/sample/customer
```

### 4. Predição Individual
**POST** `/predict`

Prediz a probabilidade de churn para um cliente.

```bash
curl -X POST http://localhost:8000/predict \
  -H "Content-Type: application/json" \
  -d @customer_data.json
```

**Exemplo de dados (customer_data.json):**
```json
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
}
```

**Resposta:**
```json
{
  "customer_id": null,
  "churn_probability": 0.53,
  "risk_level": "🟡 RISCO MÉDIO",
  "risk_description": "Monitoramento recomendado",
  "recommendations": [
    "📧 Envio de material educativo sobre serviços",
    "🎯 Campanha de retenção personalizada",
    "📊 Monitoramento semanal do comportamento",
    "💬 Proposta de upgrade de plano"
  ],
  "timestamp": "2025-01-27T10:30:00",
  "model_info": {
    "model_type": "Random Forest",
    "accuracy": 0.705,
    "auc": 0.7467,
    "features_used": 50
  }
}
```

### 5. Predição em Lote
**POST** `/predict/batch`

Prediz churn para múltiplos clientes.

```bash
curl -X POST http://localhost:8000/predict/batch \
  -H "Content-Type: application/json" \
  -d @batch_data.json
```

**Exemplo de dados (batch_data.json):**
```json
{
  "customers": [
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
    }
  ]
}
```

**Resposta:**
```json
{
  "predictions": [
    {
      "customer_id": "customer_1",
      "churn_probability": 0.53,
      "risk_level": "🟡 RISCO MÉDIO",
      "risk_description": "Monitoramento recomendado",
      "recommendations": [...],
      "timestamp": "2025-01-27T10:30:00",
      "model_info": {...}
    }
  ],
  "total_customers": 1,
  "average_probability": 0.53,
  "risk_distribution": {
    "🟢 BAIXO RISCO": 0,
    "🟡 RISCO MÉDIO": 1,
    "🔴 ALTO RISCO": 0
  }
}
```

### 6. Importância das Features
**GET** `/features/importance`

Retorna a importância das features para o modelo.

```bash
curl -X GET http://localhost:8000/features/importance
```

**Resposta:**
```json
{
  "top_features": [
    {
      "feature": "contract_type",
      "importance": 0.058787
    },
    {
      "feature": "satisfaction_score",
      "importance": 0.050098
    },
    {
      "feature": "monthly_charge",
      "importance": 0.047574
    }
  ],
  "total_features": 50
}
```

## 🧪 Como Testar

### 1. Teste Automático
Execute o script de teste:

```bash
python3 test_api.py
```

### 2. Teste Manual com curl

#### Health Check
```bash
curl -X GET http://localhost:8000/health
```

#### Obter cliente de exemplo
```bash
curl -X POST http://localhost:8000/sample/customer
```

#### Fazer predição
```bash
# Salvar dados do cliente
cat > customer.json << 'EOF'
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
}
EOF

# Fazer predição
curl -X POST http://localhost:8000/predict \
  -H "Content-Type: application/json" \
  -d @customer.json
```

## 📊 Níveis de Risco

- **🟢 BAIXO RISCO** (< 40%): Cliente estável
- **🟡 RISCO MÉDIO** (40-70%): Monitoramento recomendado
- **🔴 ALTO RISCO** (> 70%): Ação imediata necessária

## 🔧 Integração com Outras Ferramentas

### Python
```python
import requests

# Fazer predição
response = requests.post(
    "http://localhost:8000/predict",
    json=customer_data,
    headers={"Content-Type": "application/json"}
)

result = response.json()
print(f"Probabilidade de churn: {result['churn_probability']:.2%}")
```

### JavaScript/Node.js
```javascript
const axios = require('axios');

// Fazer predição
const response = await axios.post('http://localhost:8000/predict', customerData, {
  headers: { 'Content-Type': 'application/json' }
});

console.log(`Probabilidade de churn: ${(response.data.churn_probability * 100).toFixed(2)}%`);
```

### cURL (Bash)
```bash
#!/bin/bash

# Fazer predição
curl -X POST http://localhost:8000/predict \
  -H "Content-Type: application/json" \
  -d @customer.json | jq '.churn_probability'
```

## 🚀 Deploy em Produção

### Docker
```dockerfile
FROM python:3.9-slim

WORKDIR /app
COPY requirements.txt .
RUN pip install -r requirements.txt

COPY . .
EXPOSE 8000

CMD ["python", "api.py"]
```

### Docker Compose
```yaml
version: '3.8'
services:
  churn-api:
    build: .
    ports:
      - "8000:8000"
    volumes:
      - .:/app
```

## 📝 Logs e Monitoramento

A API inclui logs detalhados para monitoramento:

```bash
# Ver logs da API
python3 api.py 2>&1 | tee api.log
```

## 🔒 Segurança

Para produção, considere adicionar:

- Autenticação (JWT, API Keys)
- Rate limiting
- HTTPS
- CORS configuration
- Input validation

## 📞 Suporte

Para dúvidas ou problemas:

1. Verifique os logs da API
2. Teste o health check: `curl http://localhost:8000/health`
3. Consulte a documentação: `http://localhost:8000/docs`
4. Verifique se o modelo foi carregado corretamente

---

**Desenvolvido para o Hackathon** 🚀

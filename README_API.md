# 🚀 API de Predição de Churn

## ⚡ Início Rápido

### 1. Instalar dependências
```bash
pip3 install -r requirements.txt
```

### 2. Iniciar a API
```bash
python3 api.py
```

### 3. Testar com curl
```bash
# Health check
curl -X GET http://localhost:8000/health

# Informações do modelo
curl -X GET http://localhost:8000/model/info

# Cliente de exemplo
curl -X POST http://localhost:8000/sample/customer

# Fazer predição
curl -X POST http://localhost:8000/predict \
  -H "Content-Type: application/json" \
  -d @customer_data.json
```

## 📚 Documentação

- **Swagger UI**: http://localhost:8000/docs
- **ReDoc**: http://localhost:8000/redoc
- **Guia Completo**: [GUIA_API.md](GUIA_API.md)

## 🔧 Endpoints

| Método | Endpoint | Descrição |
|--------|----------|-----------|
| GET | `/health` | Health check da API |
| GET | `/model/info` | Informações do modelo |
| POST | `/sample/customer` | Cliente de exemplo |
| POST | `/predict` | Predição individual |
| POST | `/predict/batch` | Predição em lote |
| GET | `/features/importance` | Importância das features |

## 📊 Exemplo de Resposta

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

## 🧪 Teste Automático

```bash
python3 test_api.py
```

## 📁 Arquivos da API

- `api.py` - API principal
- `test_api.py` - Script de teste
- `GUIA_API.md` - Guia completo
- `customer_data.json` - Exemplo de dados (gerado automaticamente)
- `batch_data.json` - Exemplo de dados em lote (gerado automaticamente)

## 🚀 Deploy

### Docker
```bash
docker build -t churn-api .
docker run -p 8000:8000 churn-api
```

### Docker Compose
```bash
docker-compose up
```

## 📞 Suporte

1. Verifique se a API está rodando: `curl http://localhost:8000/health`
2. Consulte a documentação: http://localhost:8000/docs
3. Execute os testes: `python3 test_api.py`

---

**API Status**: ✅ Funcionando
**Modelo**: Random Forest (AUC: 74.67%)
**Performance**: 70.5% de acurácia

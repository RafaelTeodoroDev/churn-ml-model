# 🚀 Modelo de Predição de Churn

Este projeto implementa um modelo de machine learning para prever a probabilidade de um cliente cancelar sua assinatura (churn). O modelo foi desenvolvido para um hackathon e utiliza técnicas avançadas de machine learning para identificar clientes em risco.

## 📊 Dataset

O dataset `churn_dataset.csv` contém informações sintéticas de clientes com as seguintes features:

### Features Demográficas
- `age`: Idade do cliente
- `gender`: Gênero (M/F)

### Features de Assinatura
- `subscription_length_months`: Tempo de assinatura em meses
- `monthly_charge`: Valor mensal da assinatura
- `total_charges`: Total gasto pelo cliente
- `contract_type`: Tipo de contrato (Month-to-month, One year, Two year)
- `payment_method`: Método de pagamento

### Features de Serviços
- `tech_support`: Suporte técnico
- `online_security`: Segurança online
- `online_backup`: Backup online
- `device_protection`: Proteção de dispositivos
- `premium_tech_support`: Suporte técnico premium
- `streaming_tv`: Streaming de TV
- `streaming_movies`: Streaming de filmes
- `streaming_music`: Streaming de música
- `unlimited_data`: Dados ilimitados

### Features de Internet
- `internet_service_type`: Tipo de serviço de internet
- `phone_service`: Serviço de telefone
- `multiple_lines`: Múltiplas linhas
- `internet_service`: Serviço de internet
- `avg_monthly_gb_download`: Média mensal de GB baixados
- `monthly_usage_gb`: Uso mensal em GB

### Features de Uso
- `number_customer_service_calls`: Número de chamadas para o suporte
- `total_minutes_used`: Total de minutos usados
- `total_data_used_gb`: Total de dados usados
- `avg_call_duration_minutes`: Duração média das chamadas

### Features de Pagamento
- `payment_delay_days`: Dias de atraso no pagamento
- `late_payment_count`: Número de pagamentos atrasados
- `missed_payment_count`: Número de pagamentos perdidos

### Features de Satisfação
- `complaint_count`: Número de reclamações
- `positive_feedback_count`: Feedback positivo
- `negative_feedback_count`: Feedback negativo
- `satisfaction_score`: Score de satisfação

## 🤖 Modelos Implementados

O projeto treina e compara três modelos diferentes:

1. **Random Forest**: Algoritmo de ensemble baseado em árvores de decisão
2. **Gradient Boosting**: Algoritmo de boosting que combina múltiplos modelos fracos
3. **Logistic Regression**: Regressão logística para classificação binária

## 📈 Métricas de Avaliação

- **Acurácia**: Proporção de predições corretas
- **AUC (Area Under Curve)**: Medida de performance da curva ROC
- **Cross-Validation Score**: Validação cruzada para evitar overfitting

## 🚀 Como Executar

### 1. Instalar Dependências

```bash
pip install -r requirements.txt
```

### 2. Executar o Modelo

```bash
python churn_model.py
```

## 📊 Saídas do Modelo

O script gera automaticamente:

1. **feature_importance.png**: Gráfico das features mais importantes
2. **roc_curves.png**: Curvas ROC dos modelos treinados
3. **confusion_matrix.png**: Matriz de confusão do melhor modelo
4. **probability_analysis.png**: Análise das probabilidades de predição

## 🎯 Exemplo de Uso

```python
from churn_model import ChurnPredictor

# Inicializar o predictor
predictor = ChurnPredictor()

# Carregar e treinar o modelo
predictor.load_data('churn_dataset.csv')
predictor.preprocess_data()
predictor.train_models()

# Predizer churn para um novo cliente
customer_data = {
    'age': 35,
    'gender': 'M',
    'subscription_length_months': 12,
    'monthly_charge': 45.20,
    # ... outras features
}

probability = predictor.predict_churn_probability(customer_data)
print(f"Probabilidade de churn: {probability:.2%}")
```

## 🔍 Análise de Features

O modelo identifica as features mais importantes para prever churn:

1. **Tempo de assinatura**: Clientes com contratos mais longos tendem a ter menor churn
2. **Valor mensal**: Assinaturas mais caras podem aumentar o risco de churn
3. **Tipo de contrato**: Contratos month-to-month têm maior risco
4. **Chamadas para suporte**: Muitas chamadas indicam insatisfação
5. **Score de satisfação**: Clientes insatisfeitos têm maior probabilidade de churn

## ⚠️ Níveis de Risco

O modelo classifica clientes em três níveis de risco:

- **🟢 BAIXO RISCO**: Probabilidade < 40%
- **🟡 RISCO MÉDIO**: Probabilidade entre 40% e 70%
- **🔴 ALTO RISCO**: Probabilidade > 70%

## 📝 Estrutura do Projeto

```
churn-model/
├── churn_dataset.csv          # Dataset com dados dos clientes
├── churn_model.py            # Código principal do modelo
├── requirements.txt           # Dependências do projeto
└── README.md                 # Documentação
```

## 🎯 Aplicações Práticas

Este modelo pode ser usado para:

- **Identificar clientes em risco** de cancelamento
- **Desenvolver estratégias de retenção** personalizadas
- **Otimizar campanhas de marketing** para clientes específicos
- **Melhorar a experiência do cliente** baseada em insights do modelo

## 🔧 Personalização

Para usar com seus próprios dados:

1. Substitua `churn_dataset.csv` com seus dados
2. Ajuste as features no código conforme necessário
3. Modifique os parâmetros dos modelos se necessário
4. Adicione novas features relevantes para seu contexto

## 📞 Suporte

Para dúvidas ou sugestões sobre o modelo, entre em contato através do hackathon.

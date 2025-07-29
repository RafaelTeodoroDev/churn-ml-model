import pandas as pd
import numpy as np

# Criar dados sintéticos para o modelo de churn
np.random.seed(42)

# Número de registros
n_records = 1000

# Gerar dados
data = {
    'customer_id': range(1, n_records + 1),
    'age': np.random.randint(18, 80, n_records),
    'gender': np.random.choice(['M', 'F'], n_records),
    'subscription_length_months': np.random.randint(1, 60, n_records),
    'monthly_charge': np.random.uniform(20, 150, n_records).round(2),
    'total_charges': np.random.uniform(50, 5000, n_records).round(2),
    'contract_type': np.random.choice(['Month-to-month', 'One year', 'Two year'], n_records),
    'payment_method': np.random.choice(['Credit card', 'Bank transfer', 'Electronic check'], n_records),
    'paperless_billing': np.random.choice(['Yes', 'No'], n_records),
    'tech_support': np.random.choice(['Yes', 'No'], n_records),
    'online_security': np.random.choice(['Yes', 'No'], n_records),
    'online_backup': np.random.choice(['Yes', 'No'], n_records),
    'device_protection': np.random.choice(['Yes', 'No'], n_records),
    'premium_tech_support': np.random.choice(['Yes', 'No'], n_records),
    'streaming_tv': np.random.choice(['Yes', 'No'], n_records),
    'streaming_movies': np.random.choice(['Yes', 'No'], n_records),
    'streaming_music': np.random.choice(['Yes', 'No'], n_records),
    'unlimited_data': np.random.choice(['Yes', 'No'], n_records),
    'internet_service_type': np.random.choice(['Fiber optic', 'DSL'], n_records),
    'phone_service': np.random.choice(['Yes', 'No'], n_records),
    'multiple_lines': np.random.choice(['Yes', 'No'], n_records),
    'internet_service': np.random.choice(['Yes', 'No'], n_records),
    'avg_monthly_gb_download': np.random.uniform(0, 200, n_records).round(1),
    'avg_monthly_gb_download_6_months': np.random.uniform(0, 200, n_records).round(1),
    'avg_monthly_gb_download_12_months': np.random.uniform(0, 200, n_records).round(1),
    'monthly_usage_gb': np.random.uniform(0, 3000, n_records).round(0),
    'overage_fees': np.random.uniform(0, 50, n_records).round(2),
    'roaming_charges': np.random.uniform(0, 20, n_records).round(2),
    'international_plan': np.random.choice(['Yes', 'No'], n_records),
    'voice_mail_plan': np.random.choice(['Yes', 'No'], n_records),
    'number_vmail_messages': np.random.randint(0, 50, n_records),
    'number_customer_service_calls': np.random.randint(0, 20, n_records),
    'number_calls_placed': np.random.randint(0, 100, n_records),
    'number_calls_received': np.random.randint(0, 100, n_records),
    'total_minutes_used': np.random.randint(0, 3000, n_records),
    'total_data_used_gb': np.random.uniform(0, 100, n_records).round(1),
    'avg_call_duration_minutes': np.random.uniform(1, 20, n_records).round(1),
    'avg_call_duration_6_months': np.random.uniform(1, 20, n_records).round(1),
    'avg_call_duration_12_months': np.random.uniform(1, 20, n_records).round(1),
    'payment_delay_days': np.random.randint(0, 30, n_records),
    'late_payment_count': np.random.randint(0, 5, n_records),
    'missed_payment_count': np.random.randint(0, 3, n_records),
    'contract_renewal_days': np.random.randint(30, 1095, n_records),
    'days_since_last_upgrade': np.random.randint(0, 500, n_records),
    'days_since_last_downgrade': np.random.randint(0, 200, n_records),
    'days_since_last_complaint': np.random.randint(0, 100, n_records),
    'complaint_count': np.random.randint(0, 10, n_records),
    'positive_feedback_count': np.random.randint(0, 5, n_records),
    'negative_feedback_count': np.random.randint(0, 5, n_records),
    'social_media_mentions': np.random.randint(0, 10, n_records),
    'satisfaction_score': np.random.randint(1, 11, n_records)
}

# Criar DataFrame
df = pd.DataFrame(data)

# Gerar churn baseado em algumas regras de negócio
churn_probability = (
    # Contratos month-to-month têm maior risco
    (df['contract_type'] == 'Month-to-month') * 0.3 +
    # Muitas chamadas para suporte indicam insatisfação
    (df['number_customer_service_calls'] > 5) * 0.2 +
    # Pagamentos atrasados
    (df['late_payment_count'] > 0) * 0.15 +
    # Baixa satisfação
    (df['satisfaction_score'] < 5) * 0.25 +
    # Assinaturas caras
    (df['monthly_charge'] > 80) * 0.1 +
    # Sem serviços premium
    (df['tech_support'] == 'No') * 0.05 +
    # Base probability
    0.1
)

# Normalizar probabilidade
churn_probability = np.clip(churn_probability, 0, 1)

# Gerar churn baseado na probabilidade
df['churn'] = np.random.binomial(1, churn_probability, n_records)
df['churn'] = df['churn'].map({1: 'Yes', 0: 'No'})

# Salvar CSV
df.to_csv('churn_dataset.csv', index=False)

print(f"✅ Dataset gerado com {n_records} registros")
print(f"📊 Taxa de churn: {(df['churn'] == 'Yes').mean():.2%}")
print(f"📁 Arquivo salvo como: churn_dataset.csv")

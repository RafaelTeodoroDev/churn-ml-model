#!/usr/bin/env python3
"""
Demonstração do Modelo de Predição de Churn
============================================

Este script demonstra como usar o modelo treinado para fazer predições
de churn para novos clientes.
"""

import pandas as pd
import numpy as np
from churn_model import ChurnPredictor

def create_sample_customers():
    """Cria exemplos de clientes para demonstração"""

    customers = [
        {
            'name': 'João Silva',
            'age': 35,
            'gender': 'M',
            'subscription_length_months': 12,
            'monthly_charge': 45.20,
            'total_charges': 542.40,
            'contract_type': 'One year',
            'payment_method': 'Bank transfer',
            'paperless_billing': 'Yes',
            'tech_support': 'No',
            'online_security': 'No',
            'online_backup': 'No',
            'device_protection': 'No',
            'premium_tech_support': 'No',
            'streaming_tv': 'No',
            'streaming_movies': 'No',
            'streaming_music': 'No',
            'unlimited_data': 'No',
            'internet_service_type': 'DSL',
            'phone_service': 'Yes',
            'multiple_lines': 'No',
            'internet_service': 'Yes',
            'avg_monthly_gb_download': 12.5,
            'avg_monthly_gb_download_6_months': 15.2,
            'avg_monthly_gb_download_12_months': 13.8,
            'monthly_usage_gb': 200,
            'overage_fees': 0,
            'roaming_charges': 0,
            'international_plan': 'No',
            'voice_mail_plan': 'No',
            'number_vmail_messages': 0,
            'number_customer_service_calls': 5,
            'number_calls_placed': 12,
            'number_calls_received': 8,
            'total_minutes_used': 300,
            'total_data_used_gb': 5.2,
            'avg_call_duration_minutes': 4.8,
            'avg_call_duration_6_months': 5.5,
            'avg_call_duration_12_months': 3,
            'payment_delay_days': 1,
            'late_payment_count': 0,
            'missed_payment_count': 0,
            'contract_renewal_days': 365,
            'days_since_last_upgrade': 90,
            'days_since_last_downgrade': 0,
            'days_since_last_complaint': 30,
            'complaint_count': 2,
            'positive_feedback_count': 1,
            'negative_feedback_count': 0,
            'social_media_mentions': 0,
            'satisfaction_score': 5
        },
        {
            'name': 'Maria Santos',
            'age': 28,
            'gender': 'F',
            'subscription_length_months': 3,
            'monthly_charge': 19.99,
            'total_charges': 59.97,
            'contract_type': 'Month-to-month',
            'payment_method': 'Electronic check',
            'paperless_billing': 'No',
            'tech_support': 'No',
            'online_security': 'No',
            'online_backup': 'No',
            'device_protection': 'No',
            'premium_tech_support': 'No',
            'streaming_tv': 'No',
            'streaming_movies': 'No',
            'streaming_music': 'No',
            'unlimited_data': 'No',
            'internet_service_type': 'DSL',
            'phone_service': 'No',
            'multiple_lines': 'No',
            'internet_service': 'No',
            'avg_monthly_gb_download': 5.2,
            'avg_monthly_gb_download_6_months': 6.1,
            'avg_monthly_gb_download_12_months': 5.8,
            'monthly_usage_gb': 100,
            'overage_fees': 0,
            'roaming_charges': 0,
            'international_plan': 'No',
            'voice_mail_plan': 'No',
            'number_vmail_messages': 0,
            'number_customer_service_calls': 12,
            'number_calls_placed': 8,
            'number_calls_received': 3,
            'total_minutes_used': 200,
            'total_data_used_gb': 4.2,
            'avg_call_duration_minutes': 3.9,
            'avg_call_duration_6_months': 4.1,
            'avg_call_duration_12_months': 15,
            'payment_delay_days': 3,
            'late_payment_count': 2,
            'missed_payment_count': 1,
            'contract_renewal_days': 90,
            'days_since_last_upgrade': 30,
            'days_since_last_downgrade': 0,
            'days_since_last_complaint': 5,
            'complaint_count': 4,
            'positive_feedback_count': 3,
            'negative_feedback_count': 2,
            'social_media_mentions': 2,
            'satisfaction_score': 2
        },
        {
            'name': 'Carlos Oliveira',
            'age': 52,
            'gender': 'M',
            'subscription_length_months': 36,
            'monthly_charge': 99.99,
            'total_charges': 3599.64,
            'contract_type': 'Two year',
            'payment_method': 'Credit card',
            'paperless_billing': 'Yes',
            'tech_support': 'Yes',
            'online_security': 'Yes',
            'online_backup': 'Yes',
            'device_protection': 'Yes',
            'premium_tech_support': 'Yes',
            'streaming_tv': 'Yes',
            'streaming_movies': 'Yes',
            'streaming_music': 'Yes',
            'unlimited_data': 'Yes',
            'internet_service_type': 'Fiber optic',
            'phone_service': 'Yes',
            'multiple_lines': 'Yes',
            'internet_service': 'Yes',
            'avg_monthly_gb_download': 150.8,
            'avg_monthly_gb_download_6_months': 145.2,
            'avg_monthly_gb_download_12_months': 148.5,
            'monthly_usage_gb': 2000,
            'overage_fees': 0,
            'roaming_charges': 0,
            'international_plan': 'No',
            'voice_mail_plan': 'Yes',
            'number_vmail_messages': 45,
            'number_customer_service_calls': 0,
            'number_calls_placed': 78,
            'number_calls_received': 65,
            'total_minutes_used': 2000,
            'total_data_used_gb': 12.5,
            'avg_call_duration_minutes': 11.8,
            'avg_call_duration_6_months': 12.2,
            'avg_call_duration_12_months': 0,
            'payment_delay_days': 0,
            'late_payment_count': 0,
            'missed_payment_count': 0,
            'contract_renewal_days': 1095,
            'days_since_last_upgrade': 365,
            'days_since_last_downgrade': 0,
            'days_since_last_complaint': 0,
            'complaint_count': 0,
            'positive_feedback_count': 0,
            'negative_feedback_count': 0,
            'social_media_mentions': 0,
            'satisfaction_score': 9
        }
    ]

    return customers

def get_risk_level(probability):
    """Determina o nível de risco baseado na probabilidade"""
    if probability > 0.7:
        return "🔴 ALTO RISCO", "Ação imediata necessária"
    elif probability > 0.4:
        return "🟡 RISCO MÉDIO", "Monitoramento recomendado"
    else:
        return "🟢 BAIXO RISCO", "Cliente estável"

def get_recommendations(probability, customer_data):
    """Gera recomendações baseadas na probabilidade de churn"""
    recommendations = []

    if probability > 0.7:
        recommendations.extend([
            "📞 Contato imediato com o cliente",
            "🎁 Oferta de desconto ou benefício especial",
            "🔧 Revisão dos serviços contratados",
            "📋 Análise detalhada das reclamações"
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
            "📈 Oportunidades de upsell",
            "🌟 Programa de fidelidade",
            "📱 Comunicação regular sobre novos recursos"
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

def main():
    """Função principal da demonstração"""
    print("🎯 DEMONSTRAÇÃO DO MODELO DE PREDIÇÃO DE CHURN")
    print("=" * 60)

    # Inicializar o predictor
    predictor = ChurnPredictor()

    # Carregar e treinar o modelo
    print("🔄 Carregando e treinando o modelo...")
    predictor.load_data('churn_dataset.csv')
    predictor.preprocess_data()
    predictor.train_models()
    predictor.evaluate_models()

    print("\n" + "=" * 60)
    print("📊 ANÁLISE DE CLIENTES")
    print("=" * 60)

    # Criar exemplos de clientes
    customers = create_sample_customers()

    for i, customer in enumerate(customers, 1):
        print(f"\n👤 CLIENTE {i}: {customer['name']}")
        print("-" * 40)

        # Remover o nome para a predição
        customer_data = {k: v for k, v in customer.items() if k != 'name'}

        # Fazer predição
        probability = predictor.predict_churn_probability(customer_data)

        # Determinar nível de risco
        risk_level, risk_description = get_risk_level(probability)

        # Gerar recomendações
        recommendations = get_recommendations(probability, customer_data)

        # Exibir resultados
        print(f"📊 Probabilidade de churn: {probability:.2%}")
        print(f"⚠️  Nível de risco: {risk_level}")
        print(f"📝 Descrição: {risk_description}")

        print(f"\n📋 Recomendações:")
        for rec in recommendations:
            print(f"   • {rec}")

        # Informações adicionais do cliente
        print(f"\n📈 Perfil do cliente:")
        print(f"   • Idade: {customer['age']} anos")
        print(f"   • Contrato: {customer['contract_type']}")
        print(f"   • Valor mensal: R$ {customer['monthly_charge']:.2f}")
        print(f"   • Chamadas para suporte: {customer['number_customer_service_calls']}")
        print(f"   • Score de satisfação: {customer['satisfaction_score']}/10")

        print("\n" + "=" * 60)

    print("\n✅ Demonstração concluída!")
    print("📁 Arquivos gerados:")
    print("   - feature_importance.png")
    print("   - roc_curves.png")
    print("   - confusion_matrix.png")
    print("   - probability_analysis.png")

if __name__ == "__main__":
    main()

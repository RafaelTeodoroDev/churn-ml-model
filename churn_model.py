import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split, cross_val_score, GridSearchCV
from sklearn.preprocessing import StandardScaler, LabelEncoder
from sklearn.ensemble import RandomForestClassifier, GradientBoostingClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import classification_report, confusion_matrix, roc_auc_score, roc_curve
from sklearn.feature_selection import SelectKBest, f_classif
import warnings
warnings.filterwarnings('ignore')

# Configuração para exibir gráficos
plt.style.use('seaborn-v0_8')
sns.set_palette("husl")

class ChurnPredictor:
    def __init__(self):
        self.model = None
        self.scaler = StandardScaler()
        self.label_encoders = {}
        self.feature_columns = []
        self.target_column = 'churn'

    def load_data(self, file_path):
        """Carrega os dados do CSV"""
        print("📊 Carregando dados...")
        self.data = pd.read_csv(file_path)
        print(f"✅ Dados carregados: {self.data.shape[0]} registros e {self.data.shape[1]} colunas")
        return self.data

    def explore_data(self):
        """Explora os dados e mostra estatísticas básicas"""
        print("\n🔍 EXPLORAÇÃO DOS DADOS")
        print("=" * 50)

        # Informações básicas
        print(f"📈 Formato dos dados: {self.data.shape}")

        # Verificar valores únicos no target
        churn_counts = self.data['churn'].value_counts(normalize=True)
        print(f"🎯 Valores únicos no target: {self.data['churn'].unique()}")
        if 'Yes' in churn_counts.index:
            print(f"🎯 Taxa de churn: {churn_counts['Yes']:.2%}")
        elif len(churn_counts) > 0:
            print(f"🎯 Taxa de churn: {churn_counts.iloc[0]:.2%}")
        else:
            print("🎯 Taxa de churn: Não disponível")

        # Estatísticas descritivas
        print("\n📊 Estatísticas descritivas:")
        print(self.data.describe())

        # Verificar valores nulos
        print("\n❓ Valores nulos:")
        print(self.data.isnull().sum())

        # Distribuição do target
        print("\n🎯 Distribuição do target (churn):")
        print(self.data['churn'].value_counts())

    def preprocess_data(self):
        """Preprocessa os dados para o modelo"""
        print("\n🔧 PRÉ-PROCESSAMENTO DOS DADOS")
        print("=" * 50)

        # Criar cópia dos dados
        df = self.data.copy()

        # Converter target para binário
        df['churn'] = df['churn'].map({'Yes': 1, 'No': 0})

        # Separar features numéricas e categóricas
        numeric_features = df.select_dtypes(include=[np.number]).columns.tolist()
        categorical_features = df.select_dtypes(include=['object']).columns.tolist()

        # Remover target das features
        if 'churn' in numeric_features:
            numeric_features.remove('churn')
        if 'customer_id' in numeric_features:
            numeric_features.remove('customer_id')

        print(f"📊 Features numéricas: {len(numeric_features)}")
        print(f"📝 Features categóricas: {len(categorical_features)}")

        # Codificar features categóricas
        for col in categorical_features:
            if col != 'customer_id':
                le = LabelEncoder()
                df[col] = le.fit_transform(df[col])
                self.label_encoders[col] = le

        # Selecionar features para o modelo
        self.feature_columns = numeric_features + [col for col in categorical_features if col != 'customer_id']

        # Separar features e target
        X = df[self.feature_columns]
        y = df[self.target_column]

        # Normalizar features numéricas
        X_scaled = self.scaler.fit_transform(X)

        # Dividir em treino e teste
        self.X_train, self.X_test, self.y_train, self.y_test = train_test_split(
            X_scaled, y, test_size=0.2, random_state=42, stratify=y
        )

        print(f"✅ Dados pré-processados:")
        print(f"   - Treino: {self.X_train.shape}")
        print(f"   - Teste: {self.X_test.shape}")

        return X_scaled, y

    def feature_importance_analysis(self):
        """Análise de importância das features"""
        print("\n🔍 ANÁLISE DE IMPORTÂNCIA DAS FEATURES")
        print("=" * 50)

        # Usar Random Forest para análise de importância
        rf = RandomForestClassifier(n_estimators=100, random_state=42)
        rf.fit(self.X_train, self.y_train)

        # Criar DataFrame com importância das features
        feature_importance = pd.DataFrame({
            'feature': self.feature_columns,
            'importance': rf.feature_importances_
        }).sort_values('importance', ascending=False)

        print("🏆 Top 10 features mais importantes:")
        print(feature_importance.head(10))

        # Plotar importância das features
        plt.figure(figsize=(12, 8))
        top_features = feature_importance.head(15)
        plt.barh(range(len(top_features)), top_features['importance'])
        plt.yticks(range(len(top_features)), top_features['feature'])
        plt.xlabel('Importância')
        plt.title('Top 15 Features Mais Importantes para Prever Churn')
        plt.gca().invert_yaxis()
        plt.tight_layout()
        plt.savefig('feature_importance.png', dpi=300, bbox_inches='tight')
        plt.show()

        return feature_importance

    def train_models(self):
        """Treina diferentes modelos de machine learning"""
        print("\n🤖 TREINAMENTO DOS MODELOS")
        print("=" * 50)

        models = {
            'Random Forest': RandomForestClassifier(n_estimators=100, random_state=42),
            'Gradient Boosting': GradientBoostingClassifier(n_estimators=100, random_state=42),
            'Logistic Regression': LogisticRegression(random_state=42, max_iter=1000)
        }

        self.results = {}

        for name, model in models.items():
            print(f"\n🔄 Treinando {name}...")

            # Treinar modelo
            model.fit(self.X_train, self.y_train)

            # Fazer predições
            y_pred = model.predict(self.X_test)
            y_pred_proba = model.predict_proba(self.X_test)[:, 1]

            # Calcular métricas
            accuracy = model.score(self.X_test, self.y_test)
            auc = roc_auc_score(self.y_test, y_pred_proba)

            # Cross-validation
            cv_scores = cross_val_score(model, self.X_train, self.y_train, cv=5, scoring='accuracy')

            self.results[name] = {
                'model': model,
                'accuracy': accuracy,
                'auc': auc,
                'cv_mean': cv_scores.mean(),
                'cv_std': cv_scores.std(),
                'y_pred': y_pred,
                'y_pred_proba': y_pred_proba
            }

            print(f"   ✅ Acurácia: {accuracy:.4f}")
            print(f"   📊 AUC: {auc:.4f}")
            print(f"   🔄 CV Score: {cv_scores.mean():.4f} (+/- {cv_scores.std() * 2:.4f})")

        return self.results

    def evaluate_models(self):
        """Avalia e compara os modelos treinados"""
        print("\n📊 AVALIAÇÃO DOS MODELOS")
        print("=" * 50)

        # Comparar métricas
        comparison = pd.DataFrame({
            'Modelo': list(self.results.keys()),
            'Acurácia': [self.results[name]['accuracy'] for name in self.results.keys()],
            'AUC': [self.results[name]['auc'] for name in self.results.keys()],
            'CV Score': [self.results[name]['cv_mean'] for name in self.results.keys()]
        })

        print("🏆 Comparação dos Modelos:")
        print(comparison.sort_values('AUC', ascending=False))

        # Plotar ROC curves
        plt.figure(figsize=(10, 8))
        for name, result in self.results.items():
            fpr, tpr, _ = roc_curve(self.y_test, result['y_pred_proba'])
            plt.plot(fpr, tpr, label=f'{name} (AUC = {result["auc"]:.3f})')

        plt.plot([0, 1], [0, 1], 'k--', label='Random')
        plt.xlabel('Taxa de Falsos Positivos')
        plt.ylabel('Taxa de Verdadeiros Positivos')
        plt.title('Curvas ROC dos Modelos')
        plt.legend()
        plt.grid(True)
        plt.savefig('roc_curves.png', dpi=300, bbox_inches='tight')
        plt.show()

        # Selecionar melhor modelo
        best_model_name = max(self.results.keys(), key=lambda x: self.results[x]['auc'])
        self.best_model = self.results[best_model_name]['model']

        print(f"\n🏆 Melhor modelo: {best_model_name}")
        print(f"   📊 AUC: {self.results[best_model_name]['auc']:.4f}")
        print(f"   ✅ Acurácia: {self.results[best_model_name]['accuracy']:.4f}")

        return best_model_name

    def detailed_analysis(self, model_name):
        """Análise detalhada do melhor modelo"""
        print(f"\n🔍 ANÁLISE DETALHADA - {model_name}")
        print("=" * 50)

        result = self.results[model_name]
        model = result['model']
        y_pred = result['y_pred']
        y_pred_proba = result['y_pred_proba']

        # Matriz de confusão
        cm = confusion_matrix(self.y_test, y_pred)
        plt.figure(figsize=(8, 6))
        sns.heatmap(cm, annot=True, fmt='d', cmap='Blues',
                    xticklabels=['Não Churn', 'Churn'],
                    yticklabels=['Não Churn', 'Churn'])
        plt.title(f'Matriz de Confusão - {model_name}')
        plt.ylabel('Valor Real')
        plt.xlabel('Valor Predito')
        plt.savefig('confusion_matrix.png', dpi=300, bbox_inches='tight')
        plt.show()

        # Relatório de classificação
        print("\n📋 Relatório de Classificação:")
        print(classification_report(self.y_test, y_pred,
                                  target_names=['Não Churn', 'Churn']))

        # Análise de probabilidades
        plt.figure(figsize=(12, 5))

        # Histograma de probabilidades
        plt.subplot(1, 2, 1)
        plt.hist(y_pred_proba[self.y_test == 0], alpha=0.7, label='Não Churn', bins=20)
        plt.hist(y_pred_proba[self.y_test == 1], alpha=0.7, label='Churn', bins=20)
        plt.xlabel('Probabilidade de Churn')
        plt.ylabel('Frequência')
        plt.title('Distribuição das Probabilidades')
        plt.legend()

        # Box plot das probabilidades
        plt.subplot(1, 2, 2)
        data_to_plot = [y_pred_proba[self.y_test == 0], y_pred_proba[self.y_test == 1]]
        plt.boxplot(data_to_plot, labels=['Não Churn', 'Churn'])
        plt.ylabel('Probabilidade de Churn')
        plt.title('Box Plot das Probabilidades')

        plt.tight_layout()
        plt.savefig('probability_analysis.png', dpi=300, bbox_inches='tight')
        plt.show()

    def predict_churn_probability(self, customer_data):
        """Prediz a probabilidade de churn para um novo cliente"""
        if self.best_model is None:
            print("❌ Modelo não foi treinado ainda!")
            return None

        # Preprocessar dados do cliente
        processed_data = self.preprocess_single_customer(customer_data)

        # Fazer predição
        probability = self.best_model.predict_proba(processed_data)[0][1]

        return probability

    def preprocess_single_customer(self, customer_data):
        """Preprocessa dados de um único cliente"""
        # Converter para DataFrame
        df = pd.DataFrame([customer_data])

        # Aplicar label encoding nas features categóricas
        for col in self.label_encoders:
            if col in df.columns:
                df[col] = self.label_encoders[col].transform(df[col])

        # Selecionar apenas as features necessárias
        df = df[self.feature_columns]

        # Normalizar
        df_scaled = self.scaler.transform(df)

        return df_scaled

    def create_sample_customer(self):
        """Cria um exemplo de cliente para teste"""
        sample_customer = {
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
        }

        return sample_customer

def main():
    """Função principal para executar o pipeline completo"""
    print("🚀 INICIANDO MODELO DE PREDIÇÃO DE CHURN")
    print("=" * 60)

    # Inicializar o predictor
    predictor = ChurnPredictor()

    # Carregar dados
    data = predictor.load_data('churn_dataset.csv')

    # Explorar dados
    predictor.explore_data()

    # Pré-processar dados
    X, y = predictor.preprocess_data()

    # Análise de importância das features
    feature_importance = predictor.feature_importance_analysis()

    # Treinar modelos
    results = predictor.train_models()

    # Avaliar modelos
    best_model_name = predictor.evaluate_models()

    # Análise detalhada do melhor modelo
    predictor.detailed_analysis(best_model_name)

    # Exemplo de predição
    print("\n🎯 EXEMPLO DE PREDIÇÃO")
    print("=" * 50)

    sample_customer = predictor.create_sample_customer()
    probability = predictor.predict_churn_probability(sample_customer)

    print(f"📊 Probabilidade de churn para o cliente exemplo: {probability:.2%}")

    if probability > 0.7:
        risk_level = "🔴 ALTO RISCO"
    elif probability > 0.4:
        risk_level = "🟡 RISCO MÉDIO"
    else:
        risk_level = "🟢 BAIXO RISCO"

    print(f"⚠️  Nível de risco: {risk_level}")

    print("\n✅ Pipeline completo executado com sucesso!")
    print("📁 Arquivos gerados:")
    print("   - feature_importance.png")
    print("   - roc_curves.png")
    print("   - confusion_matrix.png")
    print("   - probability_analysis.png")

if __name__ == "__main__":
    main()

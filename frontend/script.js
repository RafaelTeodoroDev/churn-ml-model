// Configuração da API
const API_BASE_URL = window.location.hostname === 'localhost'
    ? 'http://localhost:8000'
    : `${window.location.protocol}//${window.location.hostname}/api`;

// Elementos do DOM
const customerForm = document.getElementById('customerForm');
const loadSampleBtn = document.getElementById('loadSampleBtn');
const resultsSection = document.getElementById('resultsSection');
const closeResultsBtn = document.getElementById('closeResultsBtn');
const loadingOverlay = document.getElementById('loadingOverlay');

// Elementos de resultado
const probabilityValue = document.getElementById('probabilityValue');
const riskLevel = document.getElementById('riskLevel');
const riskDescription = document.getElementById('riskDescription');
const churnProbability = document.getElementById('churnProbability');
const riskLevelDetail = document.getElementById('riskLevelDetail');
const riskDescriptionDetail = document.getElementById('riskDescriptionDetail');
const timestamp = document.getElementById('timestamp');
const recommendationsList = document.getElementById('recommendationsList');
const modelType = document.getElementById('modelType');
const modelAccuracy = document.getElementById('modelAccuracy');
const modelAuc = document.getElementById('modelAuc');
const featuresUsed = document.getElementById('featuresUsed');

// Dados de exemplo
const sampleCustomerData = {
    age: 35,
    gender: "M",
    subscription_length_months: 12,
    monthly_charge: 45.20,
    total_charges: 542.40,
    contract_type: "One year",
    payment_method: "Bank transfer",
    paperless_billing: "Yes",
    tech_support: "No",
    online_security: "No",
    online_backup: "No",
    device_protection: "No",
    premium_tech_support: "No",
    streaming_tv: "No",
    streaming_movies: "No",
    streaming_music: "No",
    unlimited_data: "No",
    internet_service_type: "DSL",
    phone_service: "Yes",
    multiple_lines: "No",
    internet_service: "Yes",
    avg_monthly_gb_download: 12.5,
    avg_monthly_gb_download_6_months: 15.2,
    avg_monthly_gb_download_12_months: 13.8,
    monthly_usage_gb: 200,
    overage_fees: 0,
    roaming_charges: 0,
    international_plan: "No",
    voice_mail_plan: "No",
    number_vmail_messages: 0,
    number_customer_service_calls: 5,
    number_calls_placed: 12,
    number_calls_received: 8,
    total_minutes_used: 300,
    total_data_used_gb: 5.2,
    avg_call_duration_minutes: 4.8,
    avg_call_duration_6_months: 5.5,
    avg_call_duration_12_months: 3,
    payment_delay_days: 1,
    late_payment_count: 0,
    missed_payment_count: 0,
    contract_renewal_days: 365,
    days_since_last_upgrade: 90,
    days_since_last_downgrade: 0,
    days_since_last_complaint: 30,
    complaint_count: 2,
    positive_feedback_count: 1,
    negative_feedback_count: 0,
    social_media_mentions: 0,
    satisfaction_score: 5
};

// Função para mostrar loading
function showLoading() {
    loadingOverlay.style.display = 'flex';
}

// Função para esconder loading
function hideLoading() {
    loadingOverlay.style.display = 'none';
}

// Função para mostrar erro
function showError(message) {
    alert(`Erro: ${message}`);
}

// Função para carregar dados de exemplo
function loadSampleData() {
    Object.keys(sampleCustomerData).forEach(key => {
        const element = document.getElementById(key);
        if (element) {
            element.value = sampleCustomerData[key];
        }
    });
}

// Função para coletar dados do formulário
function collectFormData() {
    const formData = {};
    const formElements = customerForm.elements;

    for (let element of formElements) {
        if (element.name && element.value !== '') {
            // Converter valores numéricos
            if (element.type === 'number') {
                formData[element.name] = parseFloat(element.value);
            } else {
                formData[element.name] = element.value;
            }
        }
    }

    return formData;
}

// Função para fazer predição
async function makePrediction(customerData) {
    try {
        const response = await fetch(`${API_BASE_URL}/predict`, {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify(customerData)
        });

        if (!response.ok) {
            throw new Error(`HTTP error! status: ${response.status}`);
        }

        const result = await response.json();
        return result;
    } catch (error) {
        console.error('Erro na predição:', error);
        throw error;
    }
}

// Função para atualizar a interface com os resultados
function updateResults(result) {
    // Atualizar probabilidade
    const probability = (result.churn_probability * 100).toFixed(1);
    probabilityValue.textContent = `${probability}%`;
    churnProbability.textContent = `${probability}%`;

    // Atualizar nível de risco
    riskLevel.textContent = result.risk_level;
    riskLevelDetail.textContent = result.risk_level;
    riskDescription.textContent = result.risk_description;
    riskDescriptionDetail.textContent = result.risk_description;

    // Atualizar timestamp
    const timestampDate = new Date(result.timestamp);
    timestamp.textContent = timestampDate.toLocaleString('pt-BR');

    // Atualizar recomendações
    recommendationsList.innerHTML = '';
    result.recommendations.forEach(recommendation => {
        const li = document.createElement('li');
        li.textContent = recommendation;
        recommendationsList.appendChild(li);
    });

    // Atualizar informações do modelo
    modelType.textContent = result.model_info.model_type;
    modelAccuracy.textContent = `${(result.model_info.accuracy * 100).toFixed(1)}%`;
    modelAuc.textContent = `${(result.model_info.auc * 100).toFixed(2)}%`;
    featuresUsed.textContent = result.model_info.features_used;

    // Aplicar cores baseadas no nível de risco
    const probabilityNum = parseFloat(probability);
    if (probabilityNum < 40) {
        riskLevel.className = 'risk-low';
        riskLevelDetail.className = 'risk-low';
    } else if (probabilityNum < 70) {
        riskLevel.className = 'risk-medium';
        riskLevelDetail.className = 'risk-medium';
    } else {
        riskLevel.className = 'risk-high';
        riskLevelDetail.className = 'risk-high';
    }
}

// Função para mostrar resultados
function showResults() {
    resultsSection.style.display = 'block';
    resultsSection.scrollIntoView({ behavior: 'smooth' });
}

// Função para esconder resultados
function hideResults() {
    resultsSection.style.display = 'none';
}

// Event listener para carregar dados de exemplo
loadSampleBtn.addEventListener('click', (e) => {
    e.preventDefault();
    loadSampleData();

    // Feedback visual
    loadSampleBtn.innerHTML = '<i class="fas fa-check"></i> Carregado!';
    loadSampleBtn.classList.add('success');

    setTimeout(() => {
        loadSampleBtn.innerHTML = '<i class="fas fa-download"></i> Carregar Exemplo';
        loadSampleBtn.classList.remove('success');
    }, 2000);
});

// Event listener para fechar resultados
closeResultsBtn.addEventListener('click', hideResults);

// Event listener para o formulário
customerForm.addEventListener('submit', async (e) => {
    e.preventDefault();

    try {
        showLoading();

        // Coletar dados do formulário
        const customerData = collectFormData();

        // Validar dados obrigatórios
        const requiredFields = [
            'age', 'gender', 'subscription_length_months', 'monthly_charge',
            'total_charges', 'contract_type', 'payment_method', 'satisfaction_score'
        ];

        const missingFields = requiredFields.filter(field => !customerData[field]);
        if (missingFields.length > 0) {
            throw new Error(`Campos obrigatórios não preenchidos: ${missingFields.join(', ')}`);
        }

        // Fazer predição
        const result = await makePrediction(customerData);

        // Atualizar interface
        updateResults(result);
        showResults();

    } catch (error) {
        console.error('Erro:', error);
        showError(error.message);
    } finally {
        hideLoading();
    }
});

// Função para validar campos em tempo real
function setupFieldValidation() {
    const numberInputs = document.querySelectorAll('input[type="number"]');

    numberInputs.forEach(input => {
        input.addEventListener('input', (e) => {
            const value = parseFloat(e.target.value);
            const min = parseFloat(e.target.min);
            const max = parseFloat(e.target.max);

            if (e.target.min && value < min) {
                e.target.classList.add('error');
            } else if (e.target.max && value > max) {
                e.target.classList.add('error');
            } else {
                e.target.classList.remove('error');
            }
        });
    });
}

// Função para adicionar tooltips
function setupTooltips() {
    const tooltipElements = document.querySelectorAll('[data-tooltip]');

    tooltipElements.forEach(element => {
        element.addEventListener('mouseenter', (e) => {
            const tooltip = e.target.getAttribute('data-tooltip');
            if (tooltip) {
                e.target.setAttribute('title', tooltip);
            }
        });
    });
}

// Função para verificar status da API
async function checkAPIStatus() {
    try {
        const response = await fetch(`${API_BASE_URL}/health`);
        if (response.ok) {
            console.log('✅ API está funcionando');
            return true;
        } else {
            console.error('❌ API não está respondendo');
            return false;
        }
    } catch (error) {
        console.error('❌ Erro ao conectar com a API:', error);
        return false;
    }
}

// Função para inicializar a aplicação
async function initializeApp() {
    console.log('🚀 Inicializando aplicação...');

    // Verificar status da API
    const apiStatus = await checkAPIStatus();
    if (!apiStatus) {
        showError('API não está disponível. Certifique-se de que ela está rodando em http://localhost:8000');
    }

    // Configurar validações
    setupFieldValidation();

    // Configurar tooltips
    setupTooltips();

    console.log('✅ Aplicação inicializada');
}

// Inicializar quando o DOM estiver carregado
document.addEventListener('DOMContentLoaded', initializeApp);

// Função para exportar dados
function exportData() {
    const customerData = collectFormData();
    const dataStr = JSON.stringify(customerData, null, 2);
    const dataBlob = new Blob([dataStr], { type: 'application/json' });
    const url = URL.createObjectURL(dataBlob);
    const link = document.createElement('a');
    link.href = url;
    link.download = 'customer_data.json';
    link.click();
    URL.revokeObjectURL(url);
}

// Função para importar dados
function importData(file) {
    const reader = new FileReader();
    reader.onload = function(e) {
        try {
            const data = JSON.parse(e.target.result);
            Object.keys(data).forEach(key => {
                const element = document.getElementById(key);
                if (element) {
                    element.value = data[key];
                }
            });
        } catch (error) {
            showError('Erro ao importar arquivo: formato inválido');
        }
    };
    reader.readAsText(file);
}

// Adicionar botões de import/export se necessário
function addImportExportButtons() {
    const formHeader = document.querySelector('.form-header');

    const importBtn = document.createElement('button');
    importBtn.className = 'btn btn-secondary';
    importBtn.innerHTML = '<i class="fas fa-upload"></i> Importar';
    importBtn.onclick = () => {
        const input = document.createElement('input');
        input.type = 'file';
        input.accept = '.json';
        input.onchange = (e) => {
            if (e.target.files.length > 0) {
                importData(e.target.files[0]);
            }
        };
        input.click();
    };

    const exportBtn = document.createElement('button');
    exportBtn.className = 'btn btn-secondary';
    exportBtn.innerHTML = '<i class="fas fa-download"></i> Exportar';
    exportBtn.onclick = exportData;

    formHeader.appendChild(importBtn);
    formHeader.appendChild(exportBtn);
}

// Adicionar botões de import/export
addImportExportButtons();

// Função para salvar dados no localStorage
function saveToLocalStorage() {
    const customerData = collectFormData();
    localStorage.setItem('churn_prediction_data', JSON.stringify(customerData));
}

// Função para carregar dados do localStorage
function loadFromLocalStorage() {
    const savedData = localStorage.getItem('churn_prediction_data');
    if (savedData) {
        try {
            const data = JSON.parse(savedData);
            Object.keys(data).forEach(key => {
                const element = document.getElementById(key);
                if (element) {
                    element.value = data[key];
                }
            });
        } catch (error) {
            console.error('Erro ao carregar dados salvos:', error);
        }
    }
}

// Auto-save a cada 30 segundos
setInterval(saveToLocalStorage, 30000);

// Carregar dados salvos ao inicializar
document.addEventListener('DOMContentLoaded', () => {
    loadFromLocalStorage();
});

// Função para limpar formulário
function clearForm() {
    customerForm.reset();
    localStorage.removeItem('churn_prediction_data');
}

// Adicionar botão de limpar
function addClearButton() {
    const formActions = document.querySelector('.form-actions');

    const clearBtn = document.createElement('button');
    clearBtn.type = 'button';
    clearBtn.className = 'btn btn-secondary';
    clearBtn.innerHTML = '<i class="fas fa-trash"></i> Limpar';
    clearBtn.onclick = clearForm;

    formActions.appendChild(clearBtn);
}

// Adicionar botão de limpar
addClearButton();

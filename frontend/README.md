# 🎨 Interface Frontend - Predição de Churn

## 📋 Visão Geral

Interface web moderna e responsiva para testar o modelo de predição de churn. Permite inserir dados de clientes e visualizar predições em tempo real.

## 🚀 Como Usar

### 1. Iniciar a API
```bash
# No diretório raiz do projeto
python3 api.py
```

### 2. Iniciar o Frontend
```bash
# No diretório frontend
python3 server.py
```

### 3. Acessar a Interface
A interface será aberta automaticamente em: http://localhost:3000

## 🎯 Funcionalidades

### ✅ Formulário Completo
- **Informações Básicas**: Idade, gênero
- **Assinatura**: Tempo, valor, tipo de contrato
- **Serviços**: Suporte técnico, segurança, backup
- **Streaming**: TV, filmes, música
- **Internet**: Tipo, dados ilimitados, telefone
- **Uso de Dados**: Médias mensais, taxas
- **Telefonia**: Planos, chamadas, duração
- **Pagamento**: Atrasos, histórico
- **Histórico**: Renovações, upgrades, reclamações
- **Feedback**: Positivo/negativo, satisfação

### 🎨 Interface Moderna
- Design responsivo e intuitivo
- Validação em tempo real
- Loading states
- Feedback visual
- Cores baseadas no nível de risco

### 📊 Resultados Detalhados
- Probabilidade de churn
- Nível de risco (🟢🟡🔴)
- Recomendações personalizadas
- Informações do modelo
- Timestamp da predição

### 💾 Recursos Avançados
- **Auto-save**: Dados salvos automaticamente
- **Import/Export**: JSON files
- **Dados de Exemplo**: Carregamento rápido
- **Validação**: Campos obrigatórios
- **Responsivo**: Mobile-friendly

## 🎨 Design

### Cores
- **Primária**: Gradiente azul/roxo (#667eea → #764ba2)
- **Sucesso**: Verde (#38a169)
- **Atenção**: Amarelo (#d69e2e)
- **Erro**: Vermelho (#e53e3e)

### Tipografia
- **Fonte**: Inter (Google Fonts)
- **Ícones**: Font Awesome 6

### Layout
- **Grid**: 2 colunas (form + resultados)
- **Responsivo**: 1 coluna em mobile
- **Scroll**: Suave e customizado

## 🔧 Tecnologias

- **HTML5**: Estrutura semântica
- **CSS3**: Flexbox, Grid, Animations
- **JavaScript**: ES6+, Fetch API
- **Python**: Servidor simples

## 📱 Responsividade

### Desktop (>1200px)
- Layout em 2 colunas
- Formulário à esquerda
- Resultados à direita

### Tablet (768px-1200px)
- Layout em 1 coluna
- Elementos empilhados

### Mobile (<768px)
- Layout otimizado
- Botões maiores
- Scroll vertical

## 🚀 Como Testar

### 1. Dados de Exemplo
```javascript
// Clique em "Carregar Exemplo" para preencher automaticamente
```

### 2. Validação
```javascript
// Campos obrigatórios são validados automaticamente
// Números têm limites min/max
// Feedback visual em tempo real
```

### 3. Predição
```javascript
// Clique em "Fazer Predição"
// Loading spinner aparece
// Resultados são exibidos
```

## 🔗 Integração com API

### Endpoints Utilizados
- `POST /predict` - Predição individual
- `GET /health` - Status da API

### Formato dos Dados
```json
{
  "age": 35,
  "gender": "M",
  "subscription_length_months": 12,
  "monthly_charge": 45.20,
  // ... todos os 50+ campos
}
```

### Resposta Esperada
```json
{
  "churn_probability": 0.53,
  "risk_level": "🟡 RISCO MÉDIO",
  "risk_description": "Monitoramento recomendado",
  "recommendations": [...],
  "model_info": {...}
}
```

## 🛠️ Desenvolvimento

### Estrutura de Arquivos
```
frontend/
├── index.html      # Página principal
├── styles.css      # Estilos CSS
├── script.js       # Lógica JavaScript
├── server.py       # Servidor local
└── README.md       # Documentação
```

### Personalização
```css
/* Cores principais */
:root {
  --primary: #667eea;
  --secondary: #764ba2;
  --success: #38a169;
  --warning: #d69e2e;
  --error: #e53e3e;
}
```

### Adicionar Novos Campos
1. Adicionar no HTML
2. Incluir no `sampleCustomerData`
3. Atualizar validação se necessário

## 🐛 Troubleshooting

### API não conecta
```bash
# Verificar se a API está rodando
curl http://localhost:8000/health
```

### CORS Errors
```python
# Headers CORS já configurados no server.py
```

### Dados não salvam
```javascript
// Verificar localStorage no DevTools
localStorage.getItem('churn_prediction_data')
```

## 📈 Performance

### Otimizações
- **Lazy Loading**: Dados carregados sob demanda
- **Debounce**: Validação otimizada
- **Caching**: Dados salvos localmente
- **Minificação**: Arquivos otimizados

### Métricas
- **Tempo de Carregamento**: <2s
- **Tamanho**: ~50KB total
- **Compatibilidade**: Todos os navegadores modernos

## 🔒 Segurança

### Validação
- **Client-side**: Validação em tempo real
- **Server-side**: API valida dados
- **Sanitização**: Dados limpos antes do envio

### CORS
- **Configurado**: Headers apropriados
- **Seguro**: Apenas métodos necessários

## 📚 Próximos Passos

### Melhorias Planejadas
- [ ] Gráficos interativos
- [ ] Histórico de predições
- [ ] Comparação de clientes
- [ ] Exportação de relatórios
- [ ] Temas dark/light
- [ ] PWA (Progressive Web App)

### Integrações
- [ ] Dashboard analytics
- [ ] Notificações push
- [ ] Autenticação
- [ ] Multi-tenant

---

**Desenvolvido para o Hackathon** 🚀

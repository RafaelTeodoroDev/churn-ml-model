# 🚀 Deploy na Vercel

## 📋 Pré-requisitos

1. **Conta Vercel**: Crie uma conta em [vercel.com](https://vercel.com)
2. **Vercel CLI** (opcional): `npm i -g vercel`
3. **Git**: Repositório no GitHub/GitLab

## 🚀 Deploy Automático

### Opção 1: Deploy via GitHub (Recomendado)

1. **Push para GitHub**:
   ```bash
   git add .
   git commit -m "Deploy para Vercel"
   git push origin main
   ```

2. **Conectar no Vercel**:
   - Acesse [vercel.com](https://vercel.com)
   - Clique em "New Project"
   - Importe seu repositório do GitHub
   - Clique em "Deploy"

### Opção 2: Deploy via CLI

1. **Instalar Vercel CLI**:
   ```bash
   npm i -g vercel
   ```

2. **Login**:
   ```bash
   vercel login
   ```

3. **Deploy**:
   ```bash
   vercel
   ```

## 📁 Estrutura do Projeto

```
churn-model/
├── api/
│   ├── index.py          # Entry point para Vercel
│   └── vercel_api.py     # API adaptada
├── frontend/
│   ├── index.html        # Interface web
│   ├── styles.css        # Estilos
│   ├── script.js         # JavaScript
│   └── README.md         # Documentação
├── vercel.json           # Configuração Vercel
├── requirements.txt      # Dependências Python
└── DEPLOY_VERCEL.md     # Este arquivo
```

## 🔧 Configuração

### vercel.json
```json
{
  "version": 2,
  "builds": [
    {
      "src": "api/index.py",
      "use": "@vercel/python"
    },
    {
      "src": "frontend/*",
      "use": "@vercel/static"
    }
  ],
  "routes": [
    {
      "src": "/api/(.*)",
      "dest": "/api/index.py"
    },
    {
      "src": "/(.*)",
      "dest": "/frontend/$1"
    }
  ]
}
```

### API Adaptada
- **CORS**: Configurado para todas as origens
- **Fallback**: Dados mock se modelo não carregar
- **Error Handling**: Tratamento robusto de erros

## 🌐 URLs Após Deploy

### Produção
- **Frontend**: `https://seu-projeto.vercel.app`
- **API**: `https://seu-projeto.vercel.app/api`
- **Docs**: `https://seu-projeto.vercel.app/api/docs`

### Desenvolvimento
- **Frontend**: `http://localhost:3000`
- **API**: `http://localhost:8000`

## 🔄 Atualizações

### Deploy Automático
- Push para `main` → Deploy automático
- Push para outras branches → Preview deployments

### Deploy Manual
```bash
vercel --prod
```

## 🐛 Troubleshooting

### Erro: "Module not found"
```bash
# Verificar se requirements.txt está correto
pip install -r requirements.txt
```

### Erro: "CORS policy"
```python
# CORS já configurado na API
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
```

### Erro: "Model not loaded"
- A API usa dados mock em produção
- Funciona mesmo sem o dataset

## 📊 Monitoramento

### Vercel Dashboard
- **Analytics**: Visitas, performance
- **Functions**: Logs da API
- **Deployments**: Histórico de deploys

### Logs
```bash
# Ver logs da API
vercel logs --follow
```

## 🔒 Variáveis de Ambiente

### Opcional
```bash
# No Vercel Dashboard
VERCEL_ENV=production
API_URL=https://seu-projeto.vercel.app/api
```

## 🚀 Otimizações

### Performance
- **CDN**: Arquivos estáticos otimizados
- **Edge Functions**: API serverless
- **Caching**: Headers apropriados

### SEO
- **Meta tags**: Configuradas no HTML
- **Sitemap**: Gerado automaticamente
- **Analytics**: Google Analytics (opcional)

## 📱 PWA (Opcional)

### manifest.json
```json
{
  "name": "Churn Prediction",
  "short_name": "ChurnPred",
  "start_url": "/",
  "display": "standalone",
  "theme_color": "#667eea"
}
```

## 🔄 CI/CD

### GitHub Actions (Opcional)
```yaml
name: Deploy to Vercel
on:
  push:
    branches: [main]
jobs:
  deploy:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v2
      - uses: amondnet/vercel-action@v20
        with:
          vercel-token: ${{ secrets.VERCEL_TOKEN }}
          vercel-org-id: ${{ secrets.ORG_ID }}
          vercel-project-id: ${{ secrets.PROJECT_ID }}
```

## 📈 Analytics

### Google Analytics
```html
<!-- Adicionar no index.html -->
<script async src="https://www.googletagmanager.com/gtag/js?id=GA_MEASUREMENT_ID"></script>
```

## 🎯 Próximos Passos

### Melhorias
- [ ] Custom domain
- [ ] SSL certificate
- [ ] Environment variables
- [ ] Database integration
- [ ] Authentication

### Monitoramento
- [ ] Error tracking (Sentry)
- [ ] Performance monitoring
- [ ] Uptime monitoring
- [ ] User analytics

---

## ✅ Checklist de Deploy

- [ ] Código testado localmente
- [ ] Dependências atualizadas
- [ ] CORS configurado
- [ ] Error handling implementado
- [ ] Fallback para dados mock
- [ ] URLs configuradas corretamente
- [ ] Documentação atualizada

**Deploy pronto! 🚀**

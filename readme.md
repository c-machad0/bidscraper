# 🏛️ Radar Licita

**Sistema de raspagem e monitoramento automatizado de licitações municipais**

Uma aplicação desenvolvida para empresas que desejam mapear e acompanhar licitações públicas em tempo real nos municípios da região Sul da Bahia.

## 👨‍💻 Sobre o Desenvolvedor

**Christian Machado**  
📧 realchris.machado@gmail.com  
🐙 GitHub: @c-machad0

Desenvolvedor Python e funcionário do setor de licitações da Prefeitura de Itajuípe. Este projeto nasceu da experiência prática no acompanhamento de processos licitatórios e da necessidade de automatizar a coleta e análise de dados de transparência municipal.

## 🎯 Objetivo da Aplicação

O **Radar Licita** foi desenvolvido especificamente para **empresas que desejam mapear licitações** nas cidades disponíveis no sistema. A ferramenta permite:

- **Monitoramento automatizado** de portais de transparência municipal
- **Centralização de dados** de múltiplas cidades em um único banco
- **Filtragem inteligente** por modalidade de licitação e status
- **Notificações em tempo real** via Telegram
- **Acompanhamento contínuo** de novas oportunidades de negócio

### 🏘️ Municípios Monitorados

Atualmente, o sistema monitora os seguintes municípios da Bahia:

- **Itajuípe** - https://diario.itajuipe.ba.gov.br
- **Itapitanga** - https://diario.itapitanga.ba.gov.br  
- **Almadina** - https://diario.almadina.ba.gov.br
- **Ibicaraí** - https://diario.ibicarai.ba.gov.br
- **Ubaitaba** - https://diario.ubaitaba.ba.gov.br
- **Barro Preto** - https://diario.barropreto.ba.gov.br
- **Itapé** - https://diario.itape.ba.gov.br
- **Ubatã** - https://diario.ubata.ba.gov.br

## 🚀 Funcionalidades

### ✨ Scraping Automatizado

- Extração automática de dados dos portais de transparência
- Download e processamento de arquivos JSON
- Tratamento de alertas e exceções durante a navegação
- Renomeação padronizada de arquivos por data e município
- Configuração headless para execução em servidores

### 💾 Banco de Dados Centralizado

- Armazenamento SQLite com proteção contra duplicatas
- Estrutura otimizada para consultas rápidas
- Timestamps automáticos para controle de atualização
- Suporte a múltiplas cidades em uma única base
- Limpeza automática de registros antigos (dispensas > 7 dias)

### 📱 Sistema de Notificações

- Envio automático via Telegram para canal ou grupo
- Formatação estruturada das informações de licitação
- Links diretos para os portais de transparência
- Controle de volume - apenas licitações do dia atual
- Logs detalhados de mensagens enviadas

### 🔍 Filtragem Inteligente

Detecção automática por palavras-chave para modalidades:
- **Dispensas** - prazo de 3 dias para propostas
- **Pregão Eletrônico** - licitação online
- **Pregão Presencial** - licitação física  
- **Concorrência Pública** - licitação de grande valor

## 🛠️ Tecnologias Utilizadas

- **Python 3.12** - Linguagem principal
- **Selenium WebDriver** - Automação web
- **SQLite** - Banco de dados local
- **python-telegram-bot** - API para notificações
- **Chrome WebDriver** - Navegador automatizado headless
- **JSON** - Formato de dados dos portais
- **asyncio** - Programação assíncrona

## 📁 Estrutura do Projeto

```
bidscraper/
├── main.py # Orquestrador principal
├── scrapers.py # Classes de scraping por município
├── database.py # Gerenciamento do banco SQLite
├── messages.py # Sistema de notificações Telegram
├── logger.py # Sistema de logs centralizado
├── config.py # Configurações de URLs e keywords
├── config_private_example.py # Template para variáveis de ambiente
├── requirements.txt # Dependências Python
└── downloads/ # Diretório de arquivos temporários
```

## 🏃‍♂️ Como Executar

### Pré-requisitos

```
pip install -r requirements.txt
```

### Configuração

1. **Configure as variáveis de ambiente:**
```
export MY_TOKEN="seu_token_do_bot_telegram"
export CHAT_ID_CHANNEL="id_do_seu_canal_telegram"
```

2. **Configure o bot Telegram:**
   - Crie um bot via [@BotFather](https://t.me/BotFather)
   - Adicione o bot ao seu canal/grupo como administrador
   - Obtenha o chat ID usando [@userinfobot](https://t.me/userinfobot)

### Execução Completa
```
python main.py
```


Executa o scraping de todas as cidades, atualiza o banco de dados e envia notificações via Telegram.

## ☁️ Deploy em Produção

### Railway (Recomendado)

1. Conecte seu repositório GitHub ao Railway
2. Configure as variáveis de ambiente:  
   - `MY_TOKEN`: Token do bot Telegram  
   - `CHAT_ID_CHANNEL`: ID do canal/grupo  
   - `ENVIRONMENT`: production  
3. Configure o Cron Job:  
   - **Cron Schedule:** `30 16 * * *` (13:30 BRT diário)  
   - **Start Command:** `python main.py`

### Outras Opções

- **Render** - Suporte a Cron Jobs  
- **Heroku** - Com Heroku Scheduler  
- **VPS/Servidor** - Com crontab do sistema

## 💼 Para Empresas

### 🎯 Casos de Uso Empresariais

**Fornecedores de Construção Civil:**  
- Monitore licitações de obras públicas  
- Identifique oportunidades por modalidade  
- Acompanhe status de processos de interesse

**Prestadores de Serviços:**  
- Encontre licitações de serviços especializados  
- Mapeie demandas recorrentes por município  
- Antecipe-se à concorrência

**Consultores e Analistas:**      
- Gere relatórios de mercado público regional  
- Analise padrões de compras municipais  
- Identifique nichos de oportunidade

### 📊 Exemplo de Notificação
```
⚠️ Nova licitação encontrada ⚠️
Cidade: Itajuípe
Modalidade: Pregão Eletrônico
Resumo: Aquisição de equipamentos de informática...
Portal: https://diario.itajuipe.ba.gov.br
```


## 🔧 Arquitetura Técnica

### Padrões Implementados

- **Herança**: Classe base `BidScraper` com especializações por município
- **Factory Pattern**: Criação automática de scrapers
- **Separation of Concerns**: Módulos independentes para scraping, banco e mensagens
- **Environment Variables**: Configuração segura para produção

### Robustez

- Timeouts configuráveis para elementos web
- Tratamento de alertas e pop-ups
- Proteção contra registros duplicados
- Renomeação automática de arquivos conflitantes
- Logs detalhados para debugging e monitoramento

## 📈 Roadmap

### Próximas Versões

- Interface web para consultas e dashboard
- API REST para integração com sistemas externos
- Notificações por email como alternativa  
- Webhooks para integração empresarial
- Suporte a mais municípios e estados
- Dashboard de métricas empresariais
- Filtros avançados (valor, data, categoria)
- Sistema de alertas personalizados

## 📞 Contato e Suporte

Para dúvidas técnicas, sugestões de melhoria ou interesse em customizações:

**Christian Machado**  
📧 Email: realchris.machado@gmail.com  
🐙 GitHub: [@c-machad0](https://github.com/c-machad0)  
💼 LinkedIn: [Christian Machado](https://linkedin.com/in/christian-machado)

### Serviços Disponíveis

- Customização para novos municípios  
- Integração com sistemas empresariais  
- Consultoria em automação de processos públicos  
- Desenvolvimento de funcionalidades específicas  
- Suporte técnico especializado

## 📄 Licença

Este projeto foi desenvolvido para uso comercial e empresarial. Entre em contato para informações sobre licenciamento e customizações.

---

*Desenvolvido com 💜 por Christian Machado - Transformando transparência pública em oportunidades de negócio*

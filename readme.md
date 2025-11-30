# 🏛️ Radar Licita

**Sistema de raspagem e monitoramento automatizado de licitações municipais com interface web para apresentação**

Uma aplicação desenvolvida para micro e pequenas empresas que desejam mapear e acompanhar licitações públicas em tempo real nos municípios da região Sul da Bahia.

## 👨‍💻 Sobre o Desenvolvedor

**Christian Machado**  
📧 realchris.machado@gmail.com  
🐙 GitHub: [@c-machad0](https://github.com/c-machad0)

Desenvolvedor Backend e funcionário do setor de licitações da Prefeitura de Itajuípe. Este projeto nasceu da experiência prática no acompanhamento de processos licitatórios e da necessidade de automatizar a coleta e análise de dados de transparência municipal.

## 🎯 Objetivo da Aplicação

O **Radar Licita** foi desenvolvido especificamente para **empresas que desejam mapear licitações** nas cidades disponíveis no sistema. A ferramenta permite:

- **Monitoramento automatizado** de portais de transparência municipal
- **Centralização de dados** de múltiplas cidades em um único banco
- **Filtragem inteligente** por modalidade de licitação e status
- **Notificações em tempo real** via Telegram
- **Acompanhamento contínuo** de novas oportunidades de negócio
- **Interface web interativa** para apresentações e demonstrações

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
- Limpeza automática de registros antigos

### 📱 Sistema de Notificações

- Envio automático via Telegram para canal ou grupo
- Formatação estruturada das informações de licitação
- Links diretos para os portais de transparência
- Controle de volume - apenas licitações do dia atual
- Logs detalhados de mensagens enviadas

### 🖥️ Interface Web de Apresentação (NOVO)

- **Dashboard visual interativo** com estatísticas em tempo real
- **Execução sob demanda** através de botão na interface
- **Barra de progresso** mostrando processamento de cada município
- **Logs em tempo real** com código de cores
- **Visualização de resultados** em cards organizados
- **Design responsivo** para apresentações em projetores
- **Comunicação WebSocket** para atualizações instantâneas

### 🔍 Filtragem Inteligente

Detecção automática por palavras-chave para modalidades:
- **Dispensas** - prazo de 3 dias para propostas
- **Pregão Eletrônico** - licitação online
- **Pregão Presencial** - licitação física  
- **Concorrência Pública** - licitação de grande valor

## 🛠️ Tecnologias Utilizadas

### Backend
- **Python 3.12** - Linguagem principal
- **Selenium WebDriver** - Automação web
- **SQLite** - Banco de dados local
- **python-telegram-bot** - API para notificações
- **asyncio** - Programação assíncrona

### Frontend & Interface
- **Flask** - Framework web Python
- **Flask-SocketIO** - Comunicação em tempo real
- **HTML5/CSS3** - Interface moderna e responsiva
- **JavaScript** - Interatividade do frontend
- **Socket.IO** - WebSocket para atualizações ao vivo

## 📁 Estrutura do Projeto

```
bidscraper/
├── app.py                      # 🆕 Interface web Flask
├── main.py                     # Orquestrador principal (atualizado com callbacks)
├── scrapers.py                 # Classes de scraping por município
├── database.py                 # Gerenciamento do banco SQLite
├── messages.py                 # Sistema de notificações Telegram
├── logger.py                   # Sistema de logs centralizado
├── config.py                   # Configurações de URLs e keywords
├── radarlicita.bat             # 🆕 Script de inicialização rápida (Windows)
├── requirements.txt            # Dependências Python completas
├── templates/
│   └── index.html              # 🆕 Template da interface web
├── static/
│   └── images/
│       └── radar_licita.jpg    # 🆕 Logo da aplicação
└── downloads/                  # Diretório de arquivos temporários
```

## 🏃‍♂️ Como Executar

### Pré-requisitos

```bash
pip install -r requirements.txt
```

### Configuração

1. **Configure as variáveis de ambiente:**
```bash
export MY_TOKEN="seu_token_do_bot_telegram"
export CHAT_ID_CHANNEL="id_do_seu_canal_telegram"
```

2. **Configure o bot Telegram:**
   - Crie um bot via [@BotFather](https://t.me/BotFather)
   - Adicione o bot ao seu canal/grupo como administrador
   - Obtenha o chat ID usando [@userinfobot](https://t.me/userinfobot)

### Modo 1: Interface Web de Apresentação (RECOMENDADO) 🆕

**Forma mais fácil - Duplo clique (Windows):**
```
Duplo clique em: radarlicita.bat
```

**Ou execute manualmente:**
```bash
python app.py
```

Acesse no navegador:
```
http://localhost:5000
```

**Recursos da Interface:**
- ✅ Clique no botão "Executar Rastreio de Licitações"
- ✅ Acompanhe o progresso em tempo real
- ✅ Visualize logs coloridos da execução
- ✅ Veja os resultados organizados em cards
- ✅ Ideal para apresentações e demonstrações

### Modo 2: Linha de Comando (Modo Tradicional)

Para execução via terminal sem interface:
```bash
python main.py
```

Executa o scraping de todas as cidades, atualiza o banco de dados e envia notificações via Telegram.

## ☁️ Deploy em Produção

### Railway (Recomendado para produção)

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

### 🎨 Interface de Apresentação

A nova interface web oferece:
- **Dashboard profissional** com estatísticas em tempo real
- **Execução interativa** ideal para demonstrações comerciais
- **Visualização clara** dos resultados para stakeholders
- **Design moderno** que impressiona em apresentações

## 🔧 Arquitetura Técnica

### Padrões Implementados

- **Herança**: Classe base `BidScraper` com especializações por município
- **Callback Pattern**: Sistema de notificações para interface web
- **Factory Pattern**: Criação automática de scrapers
- **Separation of Concerns**: Módulos independentes para scraping, banco e mensagens
- **Real-time Communication**: WebSocket para atualizações instantâneas
- **MVC Pattern**: Separação entre lógica, visualização e controle

### Robustez

- Timeouts configuráveis para elementos web
- Tratamento de alertas e pop-ups
- Proteção contra registros duplicados
- Renomeação automática de arquivos conflitantes
- Logs detalhados para debugging e monitoramento
- Thread-safe execution para interface web

## 📈 Roadmap

### Próximas Versões

- ✅ Interface web para consultas e dashboard (CONCLUÍDO)
- ✅ Sistema de execução sob demanda (CONCLUÍDO)
- API REST para integração com sistemas externos
- Notificações por email como alternativa  
- Webhooks para integração empresarial
- Suporte a mais municípios e estados
- Dashboard de métricas empresariais
- Filtros avançados (valor, data, categoria)
- Sistema de alertas personalizados
- Modo de apresentação offline

## 🎓 Para Apresentações Acadêmicas

A branch `lorena` foi especialmente preparada para apresentações em projetos acadêmicos de Administração:

### Vantagens para Apresentação:
- ✅ Interface visual profissional
- ✅ Execução controlada na hora da apresentação
- ✅ Demonstração ao vivo sem necessidade de servidor
- ✅ Feedback visual em tempo real
- ✅ Ideal para mostrar valor comercial do produto
- ✅ Um clique para executar tudo

### Roteiro Sugerido:
1. Abrir a interface (duplo clique no `radarlicita.bat`)
2. Explicar o conceito e problema resolvido
3. Clicar no botão de execução durante a apresentação
4. Comentar o progresso enquanto executa
5. Mostrar os resultados encontrados
6. Demonstrar as notificações do Telegram

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
- Preparação para apresentações e demonstrações

## 📄 Licença

Este projeto foi desenvolvido para uso comercial e empresarial. Entre em contato para informações sobre licenciamento e customizações.

---

*Desenvolvido com 💜 por Christian Machado - Transformando transparência pública em oportunidades de negócio*

---

## 🆕 Novidades da Versão 2.0 (Branch Lorena)

### Interface Web Interativa
- Dashboard visual com Flask e Socket.IO
- Execução em tempo real com feedback visual
- Barra de progresso por município
- Logs coloridos e animados
- Cards organizados para visualização de resultados

### Melhorias de UX
- Script `.bat` para execução com um clique
- Logo personalizada na interface
- Design responsivo e profissional
- Ideal para demonstrações comerciais e acadêmicas

### Arquitetura Aprimorada
- Sistema de callbacks para comunicação com interface
- Threading para execução não bloqueante
- WebSocket para atualizações em tempo real
- Separação clara entre modo CLI e modo Web
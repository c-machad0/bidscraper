# 🏛️ Municipal Bid Tracker

**Sistema de raspagem e monitoramento automatizado de licitações municipais**

Uma aplicação desenvolvida para empresas que desejam mapear e acompanhar licitações públicas em tempo real nos municípios da região Sul da Bahia.

---

## 👨‍💻 Sobre o Desenvolvedor

**Christian Machado**  
📧 [realchris.machado@gmail.com](mailto:realchris.machado@gmail.com)  
🐙 GitHub: [@c-machad0](https://github.com/c-machad0)

Desenvolvedor Python e funcionário do setor de licitações da Prefeitura de Itajuípe. Este projeto nasceu da experiência prática no acompanhamento de processos licitatórios e da necessidade de automatizar a coleta e análise de dados de transparência municipal.

---

## 🎯 Objetivo da Aplicação

O **Municipal Bid Tracker** foi desenvolvido especificamente para **empresas que desejam mapear licitações** nas cidades disponíveis no sistema. A ferramenta permite:

- **Monitoramento automatizado** de portais de transparência municipal
- **Centralização de dados** de múltiplas cidades em um único banco
- **Filtragem inteligente** por objeto da licitação e status
- **Acompanhamento em tempo real** de novas oportunidades de negócio

### 🏘️ Municípios Monitorados

Atualmente, o sistema monitora os seguintes municípios da Bahia:

- **Itajuípe** - transparencia.itajuipe.ba.gov.br
- **Itapitanga** - transparencia.itapitanga.ba.gov.br  
- **Almadina** - transparencia.almadina.ba.gov.br
- **Ibicaraí** - transparencia.ibicarai.ba.gov.br
- **Ubaitaba** - transparencia.ubaitaba.ba.gov.br

---

## 🚀 Funcionalidades

### ✨ Scraping Automatizado
- Extração automática de dados dos portais de transparência
- Download e processamento de arquivos JSON
- Tratamento de alertas e exceções durante a navegação
- Renomeação padronizada de arquivos por data e município

### 💾 Banco de Dados Centralizado
- Armazenamento SQLite com proteção contra duplicatas
- Estrutura otimizada para consultas rápidas
- Timestamps automáticos para controle de atualização
- Suporte a múltiplas cidades em uma única base

### 🔍 Sistema de Consultas
- Interface CLI para pesquisas filtradas
- Busca por palavra-chave no objeto da licitação
- Filtros por status do processo licitatório
- Resultados formatados e legíveis

---

## 🛠️ Tecnologias Utilizadas

- **Python 3.x** - Linguagem principal
- **Selenium WebDriver** - Automação web
- **SQLite** - Banco de dados local
- **Chrome WebDriver** - Navegador automatizado
- **JSON** - Formato de dados dos portais

---

## 📁 Estrutura do Projeto

```
municipal-bid-tracker/
├── main.py              # Orquestrador principal
├── scrapers.py          # Classes de scraping por município
├── database.py          # Gerenciamento do banco SQLite
├── query.py             # Interface de consultas
├── downloads/           # Diretório de arquivos temporários
└── dados_licitacao.db   # Banco de dados SQLite
```

---

## 🏃‍♂️ Como Executar

### Pré-requisitos
```bash
pip install selenium webdriver-manager
```

### Execução Completa
```bash
python main.py
```
*Executa o scraping de todas as cidades e atualiza o banco de dados*

### Consulta de Dados
```bash
python query.py
```
*Interface interativa para pesquisar licitações já coletadas*

---

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

### 📊 Exemplo de Consulta

```
Palavra-chave: "construção"
Status: "aberto"

Resultado: Todas as licitações abertas relacionadas à construção
em todos os municípios monitorados
```

---

## 🔧 Arquitetura Técnica

### Padrões Implementados
- **Herança**: Classe base `BidScraper` com especializações por município
- **Factory Pattern**: Criação automática de scrapers
- **Separation of Concerns**: Módulos independentes para scraping, banco e consultas

### Robustez
- Timeouts configuráveis para elementos web
- Tratamento de alertas e pop-ups
- Proteção contra registros duplicados
- Renomeação automática de arquivos conflitantes

---

## 📈 Roadmap

### Próximas Versões
- [ ] Interface web para consultas
- [ ] Notificações por email/webhook
- [ ] Suporte a mais municípios
- [ ] Dashboard de métricas empresariais
- [ ] API REST para integração
- [ ] Filtros avançados (valor, data, categoria)

---

## 📞 Contato e Suporte

Para dúvidas técnicas, sugestões de melhoria ou interesse em customizações:

**Christian Machado**  
📧 **Email:** [realchris.machado@gmail.com](mailto:realchris.machado@gmail.com)  
🐙 **GitHub:** [@c-machad0](https://github.com/c-machad0)  
💼 **LinkedIn:** [Christian Machado](https://www.linkedin.com/in/devchristianmachado/)

---

## 📄 Licença

Este projeto foi desenvolvido para uso comercial e empresarial. Entre em contato para informações sobre licenciamento e customizações.

---

*Desenvolvido com 💜 por Christian Machado - Transformando transparência pública em oportunidades de negócio*
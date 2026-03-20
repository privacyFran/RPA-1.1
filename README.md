# 🤖 RPA Coletor de Faturas — v1.1

Robô de automação desenvolvido em Python com Selenium para realizar o **login automático** e o **download de faturas** no portal da CPFL Empresas. Projetado com arquitetura modular, suporte a modo headless e log estruturado.

---

## 📋 Funcionalidades

- Login automático no portal CPFL Empresas
- Seleção automática do perfil empresarial
- Navegação até a seção de débitos e segunda via
- Download automático de faturas em PDF para todas as instalações cadastradas
- Suporte a **modo headless** (execução sem interface gráfica)
- **Logs detalhados** em console e arquivo (`logs/robot.log`)
- Gerenciamento automático do ChromeDriver via `webdriver-manager`
- Download organizado por empresa em diretórios separados (`downloads/<empresa>/`)

---

## 🗂️ Estrutura do Projeto

```
RPA-1.1/
├── main.py               # Ponto de entrada — argumentos CLI e orquestração
├── config_loader.py      # Carregamento do arquivo de configuração JSON
├── logger_config.py      # Configuração do sistema de logs
├── browser_manager.py    # Instanciamento e configuração do Chrome WebDriver
├── robot_runner.py       # Orquestrador — itera sobre as empresas e delega automações
├── site_automation.py    # Lógica de automação (BaseSiteAutomation + CPFLAutomation)
├── requirements.txt      # Dependências Python
├── config/
│   └── empresas.json     # ⚙️ Arquivo de configuração das empresas (não versionado)
├── downloads/            # PDFs baixados, organizados por empresa (gerado em execução)
└── logs/
    └── robot.log         # Logs de execução (gerado em execução)
```

---

## ⚙️ Configuração

Crie o arquivo `config/empresas.json` com as credenciais e parâmetros de cada empresa. Exemplo:

```json
[
  {
    "empresa": "cpfl",
    "url_login": "https://www.cpfl.com.br/login",
    "usuario": "seu_email@empresa.com",
    "senha": "sua_senha"
  }
]
```

> ⚠️ **Atenção:** Nunca versione o arquivo `config/empresas.json`. Adicione-o ao `.gitignore`.

---

## 🚀 Instalação e Execução

### 1. Pré-requisitos

- Python 3.8+
- Google Chrome instalado

### 2. Instalar dependências

```bash
pip install -r requirements.txt
```

### 3. Executar o robô

**Modo normal** (com interface gráfica do navegador):
```bash
python main.py
```

**Modo headless** (sem interface gráfica — ideal para servidores):
```bash
python main.py --headless
```

---

## 📦 Dependências

| Pacote | Descrição |
|---|---|
| `selenium` | Automação do navegador |
| `webdriver-manager` | Gerenciamento automático do ChromeDriver |
| `python-dotenv` | Suporte a variáveis de ambiente (`.env`) |

---

## 📄 Logs

Os logs são gerados simultaneamente no **console** e no arquivo `logs/robot.log` com o seguinte formato:

```
2025-06-10 14:32:01 INFO [CPFL] Acessando página de login...
2025-06-10 14:32:06 INFO [CPFL] Login enviado. Aguardando processamento...
2025-06-10 14:32:11 INFO [CPFL] Coleta finalizada com sucesso.
```

---

## 🏗️ Arquitetura

O projeto segue uma separação clara de responsabilidades:

```
main.py
  └── config_loader.py      → lê empresas.json
  └── RobotRunner           → itera sobre as empresas
        └── browser_manager → instancia o Chrome
        └── CPFLAutomation  → executa os passos de automação
              ├── _realizar_login()
              ├── _selecionar_perfil_empresas()
              ├── _navegar_e_acessar_instalacao()
              ├── _baixar_faturas_instalacao_principal()
              └── _baixar_faturas_outras_instalacoes()
```

Para adicionar suporte a um novo portal, basta criar uma nova classe herdando de `BaseSiteAutomation` em `site_automation.py` e registrá-la no `robot_runner.py`.

---

## 🔒 Segurança

- Credenciais nunca devem ser inseridas diretamente no código
- Use o arquivo `config/empresas.json` (fora do versionamento) ou variáveis de ambiente via `.env`
- O robô aplica técnicas básicas de anti-detecção de automação no navegador

---

## 📌 .gitignore recomendado

```gitignore
config/empresas.json
.env
logs/
downloads/
__pycache__/
*.pyc
```

---

## 🛠️ Melhorias Futuras

- [ ] Suporte a múltiplos portais além da CPFL
- [ ] Notificação por e-mail ao concluir coletas
- [ ] Agendamento automático (cron / Task Scheduler)
- [ ] Relatório consolidado dos downloads realizados
- [ ] Containerização com Docker

---

## 📝 Licença

Distribuído para uso interno. Consulte o responsável pelo projeto para informações sobre licenciamento.

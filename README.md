# 🐞 BuggyCarRacing - Testes Automatizados de API

Este projeto contém testes automatizados desenvolvidos em **Python** utilizando o **pytest**, com o apoio do **GitHub Copilot** para acelerar a escrita de código e gerar sugestões inteligentes. Os testes visam validar as principais funcionalidades da API do site [BuggyCarRacing](https://buggy.justtestit.org/).

## 📋 Funcionalidades testadas

Os testes cobrem os seguintes endpoints da API:

- 🔐 **Login** – Autenticação de usuários
- 🔑 **Token** – Geração e validação de token JWT
- 📊 **Dashboard** – Acesso às informações restritas da dashboard
- 👤 **Criar Usuário** – Registro de novos usuários no sistema
- ✅ **Get Current User** – Obtenção dos dados do usuário logado
- 🗳️ **API de Votação (Vote)** – Envio de votos para o ranking de carros

---

## 🧪 Tecnologias e ferramentas utilizadas

- **Python 3.10+**
- **pytest** – Framework de testes
- **requests** – Requisições HTTP
- **pytest-html** – Relatórios de teste em HTML
- **GitHub Copilot** – Assistente de codificação com IA
- **venv** – Ambiente virtual recomendado

---

## 📁 Estrutura do projeto

buggycar-api-tests/
├── tests/
│ ├── test_login.py
│ ├── test_token.py
│ ├── test_dashboard.py
│ ├── test_criar_usuario.py
│ ├── test_get_current_user.py
│ └── test_vote_api.py
├── utils/
│ └── helpers.py
├── requirements.txt
└── README.md

yaml
Copiar
Editar

---

## 🚀 Como executar os testes

### 1. Clone o repositório

```bash
git clone https://github.com/seu-usuario/buggycar-api-tests.git
cd buggycar-api-tests
2. Crie e ative um ambiente virtual
bash
Copiar
Editar
python -m venv venv
source venv/bin/activate  # Linux/macOS
venv\Scripts\activate     # Windows
3. Instale as dependências
bash
Copiar
Editar
pip install -r requirements.txt
4. Execute todos os testes
bash
Copiar
Editar
pytest -v
(Opcional) Gerar relatório HTML
bash
Copiar
Editar
pytest --html=report.html
🤖 Uso do GitHub Copilot
Durante o desenvolvimento dos testes, foi utilizado o GitHub Copilot como assistente de codificação. A ferramenta ajudou a sugerir estruturas de testes, identificar boas práticas e acelerar o desenvolvimento, principalmente na criação de payloads, assertions e organização dos testes com pytest.

📌 Autor
Desenvolvido por [Seu Nome]
Contato: [seuemail@dominio.com]
LinkedIn: linkedin.com/in/seunome

📜 Licença
Este projeto é de uso educacional e segue os princípios de código aberto (MIT).

yaml
Copiar
Editar

---

Se quiser, posso gerar o `requirements.txt` e exemplos dos testes também. Deseja isso?


Dito por si:
EMAIL wellingtonbrasil69@gmail.com  NOME WellingtoN MARTINS LINKEDIN https://www.linkedin.com/in/wellington-martins-6a145b269/

Dito pelo ChatGPT:
Perfeito! Aqui está o seu README.md completo, já com seus dados pessoais e profissionais atualizados:

markdown
Copiar
Editar
# 🐞 BuggyCarRacing - Testes Automatizados de API

Este projeto contém testes automatizados desenvolvidos em **Python** utilizando o **pytest**, com o apoio do **GitHub Copilot** para acelerar a escrita de código e gerar sugestões inteligentes. Os testes visam validar as principais funcionalidades da API do site [BuggyCarRacing](https://buggy.justtestit.org/).

## 📋 Funcionalidades testadas

Os testes cobrem os seguintes endpoints da API:

- 🔐 **Login** – Autenticação de usuários
- 🔑 **Token** – Geração e validação de token JWT
- 📊 **Dashboard** – Acesso às informações restritas da dashboard
- 👤 **Criar Usuário** – Registro de novos usuários no sistema
- ✅ **Get Current User** – Obtenção dos dados do usuário logado
- 🗳️ **API de Votação (Vote)** – Envio de votos para o ranking de carros

---

## 🧪 Tecnologias e ferramentas utilizadas

- **Python 3.10+**
- **pytest** – Framework de testes
- **requests** – Requisições HTTP
- **pytest-html** – Relatórios de teste em HTML
- **GitHub Copilot** – Assistente de codificação com IA
- **venv** – Ambiente virtual recomendado

---

## 📁 Estrutura do projeto

buggycar-api-tests/
├── tests/
│ ├── test_login.py
│ ├── test_token.py
│ ├── test_dashboard.py
│ ├── test_criar_usuario.py
│ ├── test_get_current_user.py
│ └── test_vote_api.py
├── utils/
│ └── helpers.py
├── requirements.txt
└── README.md

yaml
Copiar
Editar

---

## 🚀 Como executar os testes

### 1. Clone o repositório

```bash
git clone https://github.com/seu-usuario/buggycar-api-tests.git
cd buggycar-api-tests
2. Crie e ative um ambiente virtual
bash
Copiar
Editar
python -m venv venv
source venv/bin/activate  # Linux/macOS
venv\Scripts\activate     # Windows
3. Instale as dependências
bash
Copiar
Editar
pip install -r requirements.txt
4. Execute todos os testes
bash
Copiar
Editar
pytest -v
(Opcional) Gerar relatório HTML
bash
Copiar
Editar
pytest --html=report.html
🤖 Uso do GitHub Copilot
Durante o desenvolvimento dos testes, foi utilizado o GitHub Copilot como assistente de codificação. A ferramenta ajudou a sugerir estruturas de testes, identificar boas práticas e acelerar o desenvolvimento, principalmente na criação de payloads, assertions e organização dos testes com pytest.

📌 Autor
Desenvolvido por WellingtoN MARTINS
📧 Email: wellingtonbrasil69@gmail.com
🔗 LinkedIn: linkedin.com/in/wellington-martins-6a145b269

📜 Licença
Este projeto é de uso educacional e segue os princípios de código aberto (MIT).

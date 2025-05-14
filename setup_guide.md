# Guia de Configuração e Inicialização do Projeto UCHub Chatbot (Fase 2)

Este guia detalha os passos para configurar e executar a estrutura base do projeto UCHub Chatbot.

## ✅ FASE 1: CONFIGURAÇÃO E ESTRUTURA BASE

### 🔹 1. Pré-requisitos e Verificação de Versões

Antes de começar, certifique-se de que você tem as seguintes ferramentas instaladas nas versões especificadas ou compatíveis:

**1.1 ➤ Verificar versões no terminal:**

Abra o seu terminal e execute os seguintes comandos para verificar as versões instaladas:

*   **Python:**

    ```bash
    python3 --version
    ```

    A versão esperada é `Python 3.11.x` (o projeto foi desenvolvido com 3.11.0rc1, mas versões patch de 3.11 devem funcionar). Se você tiver o `python` como comando principal para Python 3, pode usar `python --version`.

*   **Node.js (Opcional para a Fase 1, mas bom verificar para fases futuras):**

    ```bash
    node -v
    ```

    A versão mencionada pelo usuário foi `v18.20.4`.

*   **npm (Opcional para a Fase 1, gerenciador de pacotes do Node):**

    ```bash
    npm -v
    ```

    A versão mencionada pelo usuário foi `10.7.0`.

### 🔹 2. Download e Estrutura do Projeto

**2.1 ➤ Baixar e extrair os arquivos do projeto:**

Faça o download do arquivo `uchub_chatbot_fase2.zip` fornecido e extraia-o em um diretório de sua preferência. Por exemplo, `~/projetos/`.

```bash
# Exemplo de como criar o diretório e extrair (ajuste o caminho do zip)
# mkdir -p ~/projetos/uchub_chatbot_workspace
# cd ~/projetos/uchub_chatbot_workspace
# unzip /caminho/para/uchub_chatbot_fase1.zip
```

Após extrair, você terá uma pasta chamada `uchub_chatbot` com a seguinte estrutura principal:

```
uchub_chatbot/
├── backend/
│   ├── src/
│   │   ├── models/
│   │   ├── routes/
│   │   │   └── example_routes.py
│   │   ├── static/
│   │   └── main.py
│   └── requirements.txt
├── docs/
├── frontend/
│   ├── index.html
│   ├── script.js
│   └── style.css
├── venv/  (Ambiente virtual Python)
├── .gitignore
├── README.md
└── todo.md
```

**2.2 ➤ Navegar para a pasta do projeto:**

```bash
cd /caminho/para/uchub_chatbot
```

### 🔹 3. Configurar e Executar o Backend (Flask)

**3.1 ➤ Ativar o ambiente virtual Python:**

O projeto já inclui um ambiente virtual (`venv`). Para ativá-lo:

*   No Linux ou macOS:

    ```bash
    source venv/bin/activate
    ```

*   No Windows (usando Git Bash ou WSL é recomendado, mas se usar Command Prompt/PowerShell):

    ```bash
    .\venv\Scripts\activate
    ```

    Após a ativação, você deverá ver `(venv)` no início do prompt do seu terminal.

**3.2 ➤ Instalar as dependências do backend (se necessário):**

As dependências já devem estar no ambiente virtual incluído no zip. Caso precise reinstalar ou se o ambiente não estiver funcionando corretamente:

```bash
# Certifique-se que o ambiente virtual está ativo
pip install -r backend/requirements.txt
```

O `backend/requirements.txt` contém `Flask` e suas dependências.

**3.3 ➤ Executar o servidor de desenvolvimento do backend:**

Navegue até a pasta `src` do backend e execute o `main.py`:

```bash
# Se você estiver na raiz do projeto uchub_chatbot:
cd backend/src
python main.py
```

Ou, de forma mais direta da raiz do projeto:

```bash
# Se você estiver na raiz do projeto uchub_chatbot e o venv estiver ativo:
python backend/src/main.py
```

O servidor Flask iniciará e estará escutando em `http://localhost:5000` (ou `http://0.0.0.0:5000`). Você deverá ver mensagens no terminal indicando que o servidor está rodando, como:

```
 * Running on http://127.0.0.1:5000
 * Running on http://[your-local-ip]:5000
```

Você pode testar as rotas básicas no seu navegador ou usando uma ferramenta como o Postman/curl:
*   `http://localhost:5000/` (deve retornar: `{"message":"Welcome to UCHub Chatbot API!"}`)
*   `http://localhost:5000/api/health` (deve retornar: `{"status":"UP"}`)
*   `http://localhost:5000/api/example/` (deve retornar: `{"message":"This is an example route!"}`)

### 🔹 4. Visualizar a Interface Web (Frontend)

O frontend é composto por arquivos HTML, CSS e JavaScript simples e não requer um processo de build ou servidor Node.js nesta fase.

**4.1 ➤ Abrir o arquivo `index.html` no navegador:**

Navegue até a pasta `frontend` dentro do projeto `uchub_chatbot` e abra o arquivo `index.html` diretamente no seu navegador web preferido (Google Chrome, Firefox, Edge, etc.).

*   Exemplo de caminho: `file:///caminho/para/uchub_chatbot/frontend/index.html`

Você verá uma interface de chat básica. Você pode digitar mensagens e clicar em "Enviar" para ver uma resposta automática simulada (a integração com o backend será feita em fases posteriores).

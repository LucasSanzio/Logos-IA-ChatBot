# UCHub Chatbot

Este é o projeto do UCHub Chatbot, desenvolvido como parte da disciplina de IA.

## Descrição

O objetivo deste projeto é criar um chatbot educacional para apoiar estudantes com materiais de estudo, utilizando Processamento de Linguagem Natural (PLN) para fornecer respostas didáticas e indicar conteúdos relevantes.

## Estrutura do Projeto

- `/backend`: Contém o código-fonte do backend da aplicação, desenvolvido em Flask (Python).
  - `/src`: Código principal da aplicação backend.
    - `/models`: Modelos de dados (a serem definidos).
    - `/routes`: Definições das rotas da API.
    - `/static`: Arquivos estáticos para o backend (se necessário).
    - `main.py`: Ponto de entrada da aplicação Flask.
  - `requirements.txt`: Dependências Python do backend.
- `/frontend`: Contém o código-fonte da interface do usuário (HTML, CSS, JavaScript).
  - `index.html`: Página principal do chatbot.
  - `style.css`: Estilos da interface.
  - `script.js`: Lógica do lado do cliente.
- `/docs`: Documentação do projeto (relatórios, diagramas, etc.).
- `venv/`: Ambiente virtual Python.
- `.gitignore`: Especifica arquivos e pastas ignorados pelo Git.
- `todo.md`: Lista de tarefas do projeto.

## Como Executar

### Backend

1.  Navegue até o diretório do projeto: `cd uchub_chatbot`
2.  Ative o ambiente virtual: `source venv/bin/activate` (Linux/macOS) ou `venv\Scripts\activate` (Windows)
3.  Navegue até o diretório do backend: `cd backend`
4.  Instale as dependências: `pip install -r requirements.txt`
5.  Execute a aplicação Flask: `python src/main.py`
    A API estará disponível em `http://localhost:5000`.

### Frontend

1.  Abra o arquivo `frontend/index.html` em seu navegador web.

## Próximos Passos (Fase 2)

- Implementar o fluxo de conversa inicial.
- Integrar uma biblioteca de PLN.
- Desenvolver a lógica para processar entradas e gerar respostas.
- Conectar o frontend ao backend.


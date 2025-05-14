# Lista de Tarefas - Entrega 2: Protótipo Inicial do Chatbot

## Fase 1: Estrutura e Base do Projeto (Concluída)

- [x] 1.1. Configurar ambiente virtual Python para o backend.
- [x] 1.2. Criar estrutura de diretórios do projeto (`/backend`, `/frontend`, `/docs`).
- [x] 1.3. Inicializar o repositório Git localmente.
- [x] 1.4. Criar o repositório no GitHub na conta `LucasSanzio` e conectar ao repositório local (instruções fornecidas).
- [x] 1.5. Implementar a estrutura base do backend com Flask.
    - [x] 1.5.1. Criar arquivo `main.py` básico.
    - [x] 1.5.2. Criar diretório `src/routes` com um exemplo de rota.
    - [x] 1.5.3. Criar diretório `src/models` (mesmo que vazio inicialmente).
    - [x] 1.5.4. Criar diretório `src/static`.
    - [x] 1.5.5. Gerar `requirements.txt` inicial.
- [x] 1.6. Desenvolver a estrutura básica do frontend (HTML, CSS, JS simples).
    - [x] 1.6.1. Criar arquivo `index.html` básico no diretório `/frontend`.
    - [x] 1.6.2. Criar arquivos básicos de CSS e JS, se necessário.
- [x] 1.7. Adicionar um arquivo `README.md` inicial ao projeto com descrição e instruções básicas.
- [x] 1.8. Fazer o primeiro commit e push para o repositório GitHub (instruções fornecidas).
- [x] 1.9. Criar arquivo de guia passo a passo para download, configuração e inicialização (`setup_guide.md`).

## Fase 2: Implementar Lógica do Chatbot e PLN

- [x] 2.1. Definir e documentar o fluxo de conversa inicial do chatbot (perguntas e respostas esperadas, saudações, despedidas, tratamento de fallback).
- [x] 2.2. Pesquisar e selecionar uma biblioteca de Processamento de Linguagem Natural (PLN) adequada para o projeto (ex: NLTK, spaCy, ou uma API de PLN como Dialogflow/Rasa se o escopo permitir).
- [x] 2.3. Instalar e configurar a biblioteca de PLN escolhida no ambiente virtual do backend.
- [x] 2.4. Implementar a lógica no backend para receber a mensagem do usuário via API.
- [x] 2.5. Implementar o processamento básico da mensagem do usuário usando a biblioteca de PLN (ex: tokenização, identificação de intenção simples ou palavras-chave).
- [x] 2.6. Implementar a lógica para gerar respostas com base na análise da mensagem do usuário e no fluxo de conversa definido.
- [x] 2.7. Criar uma nova rota no backend (ex: `/api/chat`) para lidar com as mensagens do chatbot.
- [x] 2.8. Modificar o frontend (`script.js`) para enviar a mensagem do usuário para a nova rota `/api/chat` do backend.
- [x] 2.9. Modificar o frontend para exibir a resposta recebida do backend na interface de chat.
- [x] 2.10. Testar a comunicação básica entre frontend e backend para o envio de mensagens e recebimento de respostas.

## Fase 3: Fluxo e Testes

- [ ] 3.1. Refinar o fluxo de conversa com base nos testes iniciais.
- [ ] 3.2. Criar e executar casos de teste para as funcionalidades de PLN e lógica de resposta implementadas.
- [ ] 3.3. Coletar logs de funcionamento do backend durante os testes.
- [ ] 3.4. Testar a interação do usuário com o chatbot em diferentes cenários.

## Fase 4: Documentação

- [ ] 4.1. Escrever o relatório (3 a 5 páginas) da Entrega 2.
    - [ ] 4.1.1. Descrever a estrutura do banco de conhecimento (mesmo que conceitual ou inicial).
    - [ ] 4.1.2. Incluir prints e logs de funcionamento do chatbot (Fase 2 e 3).
    - [ ] 4.1.3. Explicar a arquitetura do chatbot implementada até o momento.
- [ ] 4.2. Garantir que o código-fonte esteja atualizado e bem comentado no GitHub.
- [ ] 4.3. Revisar todos os entregáveis da Entrega 2.

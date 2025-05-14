# Relatório da Entrega 2 – Protótipo Inicial do Chatbot (Fase 2)

## Introdução

Esta seção do relatório detalha o desenvolvimento da Fase 2 do projeto UCHub Chatbot, focada na implementação da lógica inicial do chatbot, processamento de linguagem natural (PLN) básico e a integração entre o frontend e o backend.

## 1. Estrutura do Banco de Conhecimento (Inicial)

Nesta fase inicial, o "banco de conhecimento" do chatbot é implementado diretamente no código Python, especificamente no arquivo `backend/src/chatbot_logic.py`. Ele consiste em:

*   **Padrões de Saudação, Despedida e Agradecimento:** Listas de palavras-chave e frases que o chatbot reconhece para iniciar, finalizar ou responder a cortesias durante a conversa.
*   **Respostas Pré-definidas para Perguntas Específicas:** Um conjunto de perguntas e respostas fixas sobre tópicos educacionais básicos (Teorema de Pitágoras, Descobrimento do Brasil, Fotossíntese) e sobre o próprio chatbot (quem o criou). Estas são identificadas por palavras-chave nas mensagens dos usuários.
*   **Mecanismo de Fallback:** Respostas genéricas para quando o chatbot não consegue entender a pergunta do usuário.

A lógica de `get_bot_response` no arquivo `chatbot_logic.py` consulta esses padrões para formular uma resposta.

## 2. Implementação do Processamento de Linguagem Natural (PLN)

Para o processamento de linguagem natural, adotamos uma abordagem inicial simplificada:

*   **Tokenização:** A mensagem do usuário é convertida para minúsculas e, em seguida, tokenizada (dividida em palavras individuais) utilizando uma expressão regular (`re.findall(r'\b\w+\b', text)`). Esta abordagem foi escolhida para remover a dependência de recursos externos do NLTK (como o `punkt_tab`) que causaram problemas de compatibilidade no ambiente.
*   **Remoção de Stopwords:** Palavras comuns da língua portuguesa (artigos, preposições, etc., como "o", "a", "de", "para") são removidas da lista de tokens. Para isso, utilizamos a lista de stopwords em português fornecida pela biblioteca NLTK (`nltk.corpus.stopwords`).
*   **Identificação de Intenção por Palavras-chave:** A identificação da intenção do usuário é feita buscando palavras-chave específicas (pré-processadas) na mensagem do usuário ou na mensagem original em minúsculas. Por exemplo, se a mensagem contém "pitágoras", o chatbot entende que o usuário está perguntando sobre o Teorema de Pitágoras.

Este método é eficaz para um conjunto limitado de interações e serve como base para futuras melhorias com técnicas de PLN mais avançadas.

## 3. Arquitetura do Chatbot (Protótipo Inicial)

A arquitetura implementada até o momento é composta por:

*   **Frontend (Interface do Usuário):**
    *   Desenvolvido com HTML, CSS e JavaScript (`frontend/index.html`, `frontend/style.css`, `frontend/script.js`).
    *   Permite ao usuário digitar mensagens e visualiza o histórico da conversa.
    *   Envia as mensagens do usuário para o backend via uma requisição HTTP POST (usando `fetch` API) para o endpoint `/api/chat`.
    *   Exibe as respostas recebidas do backend na interface.
*   **Backend (Servidor e Lógica do Chatbot):**
    *   Desenvolvido em Python com o framework Flask (`backend/src/main.py`).
    *   Expõe um endpoint de API (`/api/chat`) que recebe as mensagens do usuário em formato JSON.
    *   Utiliza o módulo `chatbot_logic.py` para processar a mensagem recebida.
    *   O `chatbot_logic.py` contém a função `preprocess_text` (para tokenização e remoção de stopwords) e `get_bot_response` (para identificar a intenção e selecionar uma resposta).
    *   Retorna a resposta do chatbot para o frontend em formato JSON.
    *   Utiliza Flask-CORS para permitir requisições do frontend (que roda localmente via `file://`).
*   **Comunicação:** A comunicação entre frontend e backend é feita de forma assíncrona via HTTP.

## 4. Prints e Logs de Funcionamento

Os prints de tela demonstrando o funcionamento do chatbot foram salvos no diretório `docs/fase2_prints_logs/` e incluem:

*   `saudacao_resposta.webp`: Demonstra o chatbot respondendo a uma saudação.
*   `pitagoras_resposta.webp`: Demonstra o chatbot respondendo a uma pergunta sobre o Teorema de Pitágoras.
*   `quem_criou_resposta_fallback.webp`: Demonstra o chatbot utilizando a resposta de fallback para uma pergunta não mapeada inicialmente (antes do ajuste para reconhecer "quem te criou") e, em seguida, a resposta correta após o ajuste na lógica para "Quem te criou?". (Nota: O print `quem_criou_resposta_fallback.webp` captura o momento do fallback, a resposta correta para "Quem te criou?" foi validada e pode ser vista nos logs ou testada diretamente).

**Logs de Funcionamento do Backend (Exemplo):**

```log
 * Serving Flask app 'main'
 * Debug mode: on
WARNING: This is a development server. Do not use it in a production deployment. Use a production WSGI server instead.
 * Running on all addresses (0.0.0.0)
 * Running on http://127.0.0.1:5000
 * Running on http://169.254.0.21:5000
Press CTRL+C to quit
 * Restarting with stat
 * Debugger is active!
 * Debugger PIN: 106-780-085
127.0.0.1 - - [14/May/2025 13:14:33] "OPTIONS /api/chat HTTP/1.1" 200 -
127.0.0.1 - - [14/May/2025 13:14:33] "POST /api/chat HTTP/1.1" 200 -
127.0.0.1 - - [14/May/2025 13:15:15] "OPTIONS /api/chat HTTP/1.1" 200 -
127.0.0.1 - - [14/May/2025 13:15:15] "POST /api/chat HTTP/1.1" 200 -
127.0.0.1 - - [14/May/2025 13:16:03] "OPTIONS /api/chat HTTP/1.1" 200 -
127.0.0.1 - - [14/May/2025 13:16:03] "POST /api/chat HTTP/1.1" 200 -
```
*(Estes logs são exemplos das interações bem-sucedidas após a correção da tokenização. O PIN do debugger varia a cada execução.)*

## Conclusão da Fase 2

A Fase 2 concluiu a implementação do protótipo inicial do chatbot, com um fluxo de conversa básico, processamento de linguagem natural simplificado e a interface de interação funcional. Os desafios com a tokenização específica para o português no NLTK foram superados com a adoção de uma abordagem baseada em regex, garantindo maior robustez. O sistema está pronto para as próximas fases de refinamento e expansão do banco de conhecimento.


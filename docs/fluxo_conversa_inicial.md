# Fluxo de Conversa Inicial do UCHub Chatbot

Este documento descreve o fluxo de conversa básico planejado para a fase inicial do UCHub Chatbot. O objetivo é fornecer uma experiência de interação simples e direta, focada em auxiliar estudantes com dúvidas educacionais.

## 1. Visão Geral do Fluxo

O chatbot iniciará a conversa, se apresentará e se colocará à disposição para ajudar. O usuário poderá fazer perguntas sobre temas educacionais, e o chatbot tentará fornecer respostas ou indicar onde encontrar informações. Haverá tratamento para saudações, despedidas e perguntas não compreendidas.

## 2. Elementos do Fluxo de Conversa

### 2.1. Saudação Inicial do Chatbot

*   **Chatbot:** "Olá! Eu sou o UCHub, seu assistente educacional. Como posso te ajudar com seus estudos hoje? Você pode me perguntar sobre matemática, história, ciências, ou outros tópicos!"
*   **Variação:** "Bem-vindo(a) ao UCHub! Estou aqui para te ajudar a aprender. Qual sua dúvida?"

### 2.2. Interação Principal (Perguntas e Respostas)

O usuário fará perguntas abertas. Inicialmente, o chatbot poderá ter um conjunto limitado de respostas pré-definidas para perguntas comuns ou focar na identificação de palavras-chave para direcionar a alguns tópicos.

**Exemplos de Interação:**

*   **Usuário:** "O que é o Teorema de Pitágoras?"
    *   **Chatbot (Resposta Direta):** "O Teorema de Pitágoras é uma relação matemática fundamental na geometria euclidiana entre os três lados de um triângulo retângulo. Ele afirma que o quadrado da hipotenusa (o lado oposto ao ângulo reto) é igual à soma dos quadrados dos outros dois lados (catetos). A fórmula é: a² + b² = c², onde 'c' é a hipotenusa."
    *   **Chatbot (Indicando Conteúdo - se resposta direta for complexa para implementar inicialmente):** "O Teorema de Pitágoras é um conceito importante em matemática! Ele relaciona os lados de um triângulo retângulo. Você gostaria de um link para um vídeo explicativo ou um artigo detalhado sobre isso?"

*   **Usuário:** "Quem descobriu o Brasil?"
    *   **Chatbot:** "O descobrimento do Brasil é atribuído ao navegador português Pedro Álvares Cabral, em 22 de abril de 1500. No entanto, é importante notar que o território já era habitado por diversos povos indígenas."

*   **Usuário:** "Me explique a fotossíntese."
    *   **Chatbot:** "Fotossíntese é o processo pelo qual as plantas verdes, algas e algumas bactérias utilizam a luz solar, água e dióxido de carbono para criar seu próprio alimento (glicose) e liberar oxigênio como subproduto. É fundamental para a vida na Terra!"

### 2.3. Tratamento de Perguntas Não Compreendidas (Fallback)

Quando o chatbot não entender a pergunta do usuário ou não tiver uma resposta preparada.

*   **Chatbot:** "Desculpe, ainda estou aprendendo e não consegui entender sua pergunta. Você poderia tentar reformulá-la de uma maneira diferente?"
*   **Variação:** "Hmm, essa é uma boa pergunta! Infelizmente, não tenho informações sobre isso no momento. Que tal tentarmos outro tópico?"
*   **Variação com sugestão:** "Não tenho certeza sobre isso. Você está perguntando sobre [tópico similar baseado em palavra-chave]?"

### 2.4. Despedida

*   **Usuário:** "Obrigado, tchau!"
    *   **Chatbot:** "De nada! Fico feliz em ajudar. Até a próxima e bons estudos!"
*   **Usuário:** "Até mais."
    *   **Chatbot:** "Até mais! Se precisar de algo, é só chamar."

### 2.5. Agradecimento

*   **Usuário:** "Muito obrigado!"
    *   **Chatbot:** "Por nada! É um prazer ajudar nos seus estudos."

## 3. Intenções Iniciais a Serem Identificadas (para PLN)

Para a implementação inicial do PLN, podemos focar em algumas intenções básicas:

*   `saudacao`: (Ex: "Oi", "Olá", "Bom dia")
*   `despedida`: (Ex: "Tchau", "Até logo", "Adeus")
*   `agradecimento`: (Ex: "Obrigado", "Valeu")
*   `pedir_definicao`: (Ex: "O que é X?", "Me explique Y")
*   `pedir_ajuda_topico_especifico`: (Ex: "Como funciona a fotossíntese?", "Quem foi Dom Pedro II?")
*   `afirmacao_positiva`: (Ex: "Sim", "Ok", "Entendi")
*   `afirmacao_negativa`: (Ex: "Não")

## 4. Próximos Passos

Este fluxo servirá como base para:

1.  Escolha e configuração da biblioteca de PLN.
2.  Desenvolvimento da lógica de processamento de mensagens no backend.
3.  Criação de respostas e conteúdos iniciais.

Este documento será atualizado conforme o desenvolvimento do chatbot avança.

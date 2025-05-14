# backend/src/chatbot_logic.py

import nltk # NLTK ainda é usado para stopwords
import random
import re # Importa regex para tokenização alternativa
from nltk.corpus import stopwords

# Baixar recursos do NLTK (apenas stopwords agora)
# Em produção, isso deve ser feito durante o setup/deploy.
try:
    stopwords.words("portuguese")
except LookupError: # Alterado para LookupError que é mais genérico para recursos não encontrados
    print("Baixando recurso 'stopwords' do NLTK... Isso pode levar um momento.")
    nltk.download("stopwords", quiet=True)
    print("Recurso 'stopwords' do NLTK baixado.")

stop_words_pt = set(stopwords.words("portuguese"))

def preprocess_text(text):
    """Tokeniza o texto usando regex, converte para minúsculas e remove stopwords."""
    if text is None:
        return []
    text = text.lower()
    # Tokenização manual usando regex para palavras alfanuméricas
    tokens = re.findall(r'\b\w+\b', text) 
    processed_tokens = [token for token in tokens if token not in stop_words_pt]
    # Não é mais necessário token.isalnum() pois o regex já cuida de pegar apenas palavras
    return processed_tokens

def get_bot_response(user_message):
    """Gera uma resposta do chatbot baseada na mensagem do usuário."""
    tokens = preprocess_text(user_message)
    original_message_lower = user_message.lower() # Usar para verificações que não dependem de tokenização exata

    # Lógica de saudação
    saudacoes = ["olá", "oi", "bom dia", "boa tarde", "boa noite", "e aí", "opa"]
    if any(saudacao in tokens for saudacao in saudacoes) or any(saudacao in original_message_lower for saudacao in saudacoes):
        respostas_saudacao = [
            "Olá! Eu sou o UCHub, seu assistente educacional. Como posso te ajudar com seus estudos hoje?",
            "Oi! Bem-vindo(a) ao UCHub! Pronto para aprender algo novo?",
            "Olá! Em que posso ser útil nos seus estudos hoje?"
        ]
        return random.choice(respostas_saudacao)

    # Lógica de despedida
    despedidas = ["tchau", "adeus", "até logo", "até mais", "falou", "flw"]
    if any(despedida in tokens for despedida in despedidas) or any(despedida in original_message_lower for despedida in despedidas):
        respostas_despedida = [
            "Até mais! Se precisar de algo, é só chamar.",
            "Tchau! Bons estudos e volte sempre!",
            "De nada! Fico feliz em ajudar. Até a próxima!"
        ]
        return random.choice(respostas_despedida)

    # Lógica de agradecimento
    agradecimentos = ["obrigado", "obrigada", "valeu", "vlw", "grato", "grata"]
    if any(agradecimento in tokens for agradecimento in agradecimentos) or any(agradecimento in original_message_lower for agradecimento in agradecimentos):
        respostas_agradecimento = [
            "Por nada! É um prazer ajudar nos seus estudos.",
            "De nada! Estou aqui para isso.",
            "Disponha! Se tiver mais dúvidas, pode perguntar."
        ]
        return random.choice(respostas_agradecimento)

    # Lógica para perguntas específicas (exemplos simples baseados em palavras-chave)
    if "pitágoras" in tokens or "pitagoras" in original_message_lower:
        return "O Teorema de Pitágoras é uma relação matemática fundamental na geometria euclidiana entre os três lados de um triângulo retângulo. Ele afirma que o quadrado da hipotenusa (o lado oposto ao ângulo reto) é igual à soma dos quadrados dos outros dois lados (catetos). A fórmula é: a² + b² = c², onde 'c' é a hipotenusa."
    
    if ("descobrimento" in tokens or "descobriu" in tokens) and "brasil" in tokens:
        return "O descobrimento do Brasil é atribuído ao navegador português Pedro Álvares Cabral, em 22 de abril de 1500. No entanto, é importante notar que o território já era habitado por diversos povos indígenas."

    if "fotossíntese" in tokens or "fotossintese" in original_message_lower:
        return "Fotossíntese é o processo pelo qual as plantas verdes, algas e algumas bactérias utilizam a luz solar, água e dióxido de carbono para criar seu próprio alimento (glicose) e liberar oxigênio como subproduto. É fundamental para a vida na Terra!"
    
    if "quem" in tokens and ("criou" in tokens or "inventou" in tokens) and ("uchub" in tokens or "você" in tokens or "vc" in tokens):
        return "Fui criado pela equipe Logos IA para o projeto UCHub!"

    # Fallback (resposta padrão se nenhuma regra for atendida)
    respostas_fallback = [
        "Desculpe, ainda estou aprendendo e não consegui entender sua pergunta. Você poderia tentar reformulá-la de uma maneira diferente?",
        "Hmm, essa é uma boa pergunta! Infelizmente, não tenho informações sobre isso no momento. Que tal tentarmos outro tópico?",
        "Não tenho certeza sobre isso. Você pode tentar perguntar de outra forma?"
    ]
    return random.choice(respostas_fallback)

# Teste simples
if __name__ == "__main__":
    print(get_bot_response("Olá, tudo bem?"))
    print(get_bot_response("o que é o teorema de pitágoras"))
    print(get_bot_response("Quem descobriu o Brasil?"))
    print(get_bot_response("Explique a fotossíntese"))
    print(get_bot_response("obrigado pela ajuda"))
    print(get_bot_response("tchau"))
    print(get_bot_response("qual a capital da frança?")) # Fallback
    print(get_bot_response("Quem te criou?"))


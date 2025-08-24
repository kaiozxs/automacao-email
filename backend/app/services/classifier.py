def classify_email(content: str) -> str:
    
    produtivo_keywords = ["ajuda", "suporte", "erro", "pedido", "dúvida"]
    content_lower = content.lower()
    for word in produtivo_keywords:
        if word in content_lower:
            return "Produtivo"
    return "Improdutivo"


def generate_response(classification: str) -> str:
    if classification == "Produtivo":
        return "Olá! Estamos analisando seu pedido e em breve retornaremos."
    else:
        return "Obrigado pela sua mensagem!" 

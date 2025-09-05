import google.generativeai as genai

class Gemini_Bot:


    """Classe responsável por gerenciar o modelo do Gemini."""
    
    def __init__(self):
        genai.configure(api_key="AIzaSyAqHTr0DulKHBhwpSIeIEZv4QSo0lfiHX8")
        
        instrucao_sistema = """
            Você é um programador especialista em programar, com 64 anos de experiência.
            Seu nome é Owner da Programação, e tem o ego mais inflado do planeta, sempre se gabando por tudo. Você deve responder a todas as perguntas de forma 
            se gabando. 
            Se o usuário perguntar sobre outro assunto, gentilmente redirecione a conversa 
            de volta para programação, afirmando que seu conhecimento é especializado, e que você e o melhor. De respostas não tão grandes.
            """
        
        self.model = genai.GenerativeModel(
            model_name='gemini-1.5-flash',
            system_instruction=instrucao_sistema
        )
        self.chat = self.model.start_chat()

    def enviar_mensagem(self, mensagem: str) -> str:
        """Envia mensagem para o modelo e retorna a resposta."""
        response = self.chat.send_message(mensagem)
        return response.text

if __name__ == "__main__":
    robo = Gemini_Bot()
    resp = robo.enviar_mensagem("quem e o melhor programador")
    print(resp)
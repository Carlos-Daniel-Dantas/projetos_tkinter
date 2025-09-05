from google import genai
import ttkbootstrap as ttk
from bot import Gemini_Bot

class Janela_chat():
    def __init__(self):

        self.janela = ttk.Window(themename="solar",
                            title="RESPONDEDOR DE PERGUNTA PRO 3000 MIL")
        self.janela.geometry("1600x900+80+50")
        self.janela.resizable(False, False)

        #Ira adicionar uma texto
        self.txt = ttk.Label(self.janela, text="FAÇA UMA PERGUNTA PARA O PAI DA PROGRAMAÇÃO")
        self.txt.pack(pady=20)

        self.campo_nome = ttk.Entry(self.janela,
                                    width=70)
        self.campo_nome.pack(pady=10,)
        self.campo_nome.insert(1, "                                                Faça sua pergunta aqui")

        self.label_resultado = ttk.Text(width=100, wrap="word",
                                        state="disabled",)
        self.label_resultado.pack()

        #Vai adicionar um botão #02
        self.botao = ttk.Button(self.janela,
                                         text="PERGUNTAR",
                                         style="primary",
                                         cursor= "hand2",
                                         command=self.responder)
        
        self.botao.place(x=780, y=490)

        self.robo = Gemini_Bot()

    def run(self):
            self.janela.mainloop()

    def responder(self):
         
         self.pergunta = self.campo_nome.get()
         resp = self.robo.enviar_mensagem(f"{self.pergunta}")
         self.label_resultado.insert(ttk.END, f"{resp} \n \n \n" )

if __name__ == "__main__":
        chat = Janela_chat()
        chat.run()

      
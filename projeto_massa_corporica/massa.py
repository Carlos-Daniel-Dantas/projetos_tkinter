from google import genai
import ttkbootstrap as ttk


class Janela_chat():
    def __init__(self):

        self.janela = ttk.Window(themename="solar",
                            title="TESTE DE MASSA CORPORICA")
        self.janela.geometry("800x600+80+50")
        self.janela.resizable(False, False)

        #Ira adicionar uma texto
        self.txt = ttk.Label(self.janela, text="DIGITE SEU PESO E SUA ALTURA")
        self.txt.pack(pady=20)


        self.PS = ttk.Label(self.janela, text="DIGITE SEU PESO AQUI")
        self.PS.pack(pady=20)
        self.alt = ttk.Label(self.janela, text="DIGITE SUA ALTURA AQUI")
        self.alt.pack(pady=20)


        self.campo_nome = ttk.Entry(self.janela,
                                    width=5)
        self.campo_nome.place(x=10, y=10)

        self.pes_nome_nome = ttk.Entry(self.janela,
                                    width=5
                                    )
        
        self.pes_nome_nome.pack(pady=10,)

        self.label_resultado = ttk.Text(width=100, wrap="word",
                                        state="disabled",)
        self.label_resultado.pack()


    def run(self):
            self.janela.mainloop()

if __name__ == "__main__":
        chat = Janela_chat()
        chat.run()

      
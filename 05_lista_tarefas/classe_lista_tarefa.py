import ttkbootstrap as tk


class janela_Lista_Tarefas():
  """Classe para a criação da self.janela principal"""

  def __init__(self):

    self.janela = tk.Window(themename='vapor')
    self.janela.title("Lista Tarefas")
    self.janela.geometry("1200x900+80+50")

    #Texto Adicionar
    self.label_usu = tk.Label(text="Adicionar Tarefas") #Caixa 01 peso
    self.label_usu.pack(padx=10)

    self.entry_usu = tk.Entry(width=25,
                                ) #Largura da caixa
    self.entry_usu.pack(padx=10) 

  def run(self):
    self.janela.mainloop()

if __name__ == "__main__":
    app = janela_Lista_Tarefas()
    app.run()



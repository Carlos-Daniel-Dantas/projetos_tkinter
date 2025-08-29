import ttkbootstrap as tk

class janela_principal:
  """Classe para a criação da self.janela principal"""

  def __init__(self):

    #Config self.janela
    self.janela = tk.Window(themename='united')
    self.janela.title("Youtube")
    self.janela.geometry("1600x900+80+50")

    #texto 1

    self.label_nome = tk.Label(self.janela, font = 34, text="FAÇA UMA PERGUNTA PARA O PAI DA PROGRAMAÇÃO:")
    self.label_nome.pack()

    #Onde sera inserido o texto
    self.campo_nome = tk.Entry(self.janela)
    self.campo_nome.pack()

    #botão
    self.botao_enviar = tk.Button(self.janela, text="PERGUNTAR", command=self.desejar_bomdia)
    self.botao_enviar.pack(pady=5)
  
    self.label_resultado = tk.Label(self.janela, text="")
    self.label_resultado.pack()

  def desejar_bomdia(self):
      """Esta função pega o nome digitado na caixa de texto e deseja um Bom dia"""

      self.nome_digitado = self.campo_nome.get(self) 
      self.label_resultado.config(text=f"Bom dia, {self.nome_digitado}!") #esultado

  def run(self):
    """Inicia a self.janela"""

  self.janela.mainloop()
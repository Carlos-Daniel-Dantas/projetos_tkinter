import ttkbootstrap as tk
from tkinter import Listbox, END
from tkinter import messagebox
import sqlite3


class janela_Lista_Tarefas():
  """Classe para a criação da self.janela principal"""

  def __init__(self):
    
    self.janela = tk.Window(themename='cyborg')
    self.janela.title("Login")
    self.janela.geometry("800x400+500+290")

    self.titulo = tk.Label(self.janela, text="CONFIRME SUA ENTRADA",
                                      style="light",
                                      font=("Arial", 12))
    self.titulo.pack(pady=2)

    self.janela.iconbitmap("IMG/logo.ico")

    # Campos de entrada para peso e altura
    self.campos = tk.Frame(self.janela)
    self.campos.pack(pady=10)

    self.label_nome = tk.Label(self.campos, text="NOME", padding=10) #Caixa 01 peso
    self.label_nome.pack(padx=10)

    self.nova_nome = tk.Entry(self.campos, width=25,
                                ) #Largura da caixa
    self.nova_nome.pack(padx=10) 


    self.usu = tk.Label(self.campos, text="USUÁRIO", padding=10) #Caixa 01 peso
    self.usu.pack(padx=10)

    self.nova_usu = tk.Entry(self.campos, width=25,
                                ) #Largura da caixa
    self.nova_usu.pack(padx=10)

    self.senha = tk.Label(self.campos, text="SENHA", padding=10) #02 altura 
    self.senha.pack(padx=10)
    self.nova_usu = tk.Entry(self.campos, width=25,
                                ) #Largura da caixa
    self.nova_usu.pack(padx=10) 


    self.label_usu = tk.Label(self.campos, text="CONFIRME SUA SENHA", padding=10) #Caixa 01 peso
    self.label_usu.pack(padx=10)

    self.nova_usu = tk.Entry(self.campos, width=25,
                                ) #Largura da caixa
    self.nova_usu.pack(padx=10)

    # Botão 
    self.botao_avancar = tk.Button(self.janela,
                                    text="LOGAR",
                                    cursor="hand2"
                                    )
    
    self.botao_avancar.place(y=330,x=320)                

    #BOTÃO 02
    self.botao_avancar2 = tk.Button(self.janela,
                                    text="CANCELAR",
                                    cursor="hand2"
                                    )
    self.botao_avancar2.place(y=330,x=400)

  def run(self):
    self.janela.mainloop()

if __name__ == "__main__":
    app = janela_Lista_Tarefas()
    app.run()



import ttkbootstrap as tk
from tkinter import Listbox, END
from tkinter import messagebox
import sqlite3

class Janela_login():
  """Classe para a criação da self.janela principal"""

  def __init__(self, janela_pai):

    self.janela_pai = janela_pai
    self.janela= tk.Toplevel(janela_pai)
    self.janela.resizable(False, False)


    #configurando para que quando feche a janela de login ele encerre o programa
    self.janela.protocol("WM_DELETE_WINDOW", exit)
    
    #self.janela = tk.Window(themename='cyborg')
    self.janela.title("Cadastro")
    self.janela.geometry("800x400+500+290")

    self.titulo = tk.Label(self.janela, text="SE CADASTRE AQUI",
                                      style="light",
                                      font=("Arial", 14))
    self.titulo.pack(pady=2)
    self.janela.iconbitmap("IMG/logo.ico")

    self.campos = tk.Frame(self.janela)
    self.campos.pack(pady=10)

    #------------------------------------------------------------------

    self.nome = tk.Label(self.campos, text="NOME", padding=10) 
    self.nome.pack(padx=10)

    self.campo_nome = tk.Entry(self.campos, width=25,
                                ) 
    self.campo_nome.pack(padx=10)

    #------------------------------------------------------------------

    self.usuario = tk.Label(self.campos, text="USUÁRIO", padding=10) 
    self.usuario.pack(padx=10)

    self.campo_usuario = tk.Entry(self.campos, width=25,
                                ) 
    self.campo_usuario.pack(padx=10)

    #------------------------------------------------------------------

    self.senha = tk.Label(self.campos, text="SENHA", padding=10) #02 altura 
    self.senha.pack(padx=10)

    self.senha = tk.Entry(self.campos, width=25,
                                ) #Largura da caixa
    self.senha.pack(padx=10) 

    #------------------------------------------------------------------

    self.confirmar_senha = tk.Label(self.campos, text="CONFIRME SUA SENHA", padding=10) #Caixa 01 peso
    self.confirmar_senha.pack(padx=10)

    self.confirmar_senha = tk.Entry(self.campos, width=25,
                                ) #Largura da caixa
    self.confirmar_senha.pack(padx=10)

    
    #------------------------------------------------------------------

    # Botão 
    self.botao_avancar = tk.Button(self.janela,
                                    text="LOGAR",
                                    cursor="hand2"
                                    )
    
    self.botao_avancar.place(y=340,x=320)                

    #BOTÃO 02
    self.botao_cancelar = tk.Button(self.janela,
                                    text="CANCELAR",
                                    cursor="hand2"
                                    )
    self.botao_cancelar.place(y=340,x=400)

    #------------------------------------------------------------------
    
  def run(self):
    self.janela.mainloop()

if __name__ == "__main__":
    app = Janela_login()
    app.run()



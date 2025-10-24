import ttkbootstrap as tk
from tkinter import Listbox, END
from tkinter import messagebox
import sqlite3

class Janela_login():
  """Classe para a criação da self.janela principal"""

  def __init__(self, paidocadastro):

    self.paidocadastro = paidocadastro
    self.janela= tk.Toplevel(paidocadastro)
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
                                    command=self.cadastro_funcao

                                    )
    
    self.botao_avancar.place(y=340,x=320)                

    #BOTÃO 02
    self.botao_cancelar = tk.Button(self.janela,
                                    text="CANCELAR",
                                    cursor="hand2"
                                    )
    self.botao_cancelar.place(y=340,x=400)

    #------------------------------------------------------------------


    conexao = sqlite3.connect("05_lista_tarefas/bd_lista_tarefas.sqlite")

   #Criando responsavel por comandar o Banco de Dados 
    cursor = conexao.cursor()

   #Criando tabela 
    sql_para_criar_tabela_usuario = """
                                CREATE TABLE IF NOT EXISTS usuarios (
                                nome varchar(80),
                                usuario varchar(24) primary key,
                                senha varchar(20)

                                );
                            """
    cursor.execute(sql_para_criar_tabela_usuario)

    # Confirma as alterações
    conexao.commit()
    
    #fechei a conexão
    cursor.close()
    conexao.close()

  def cadastro_funcao(self):
          self.resposta_nome = self.campo_nome.get()
          self.resposta_usuario = self.campo_usuario.get()
          self.resposta_senha = self.senha.get()
          self.resposta_senha2 = self.confirmar_senha.get()

          if self.resposta_senha == self.resposta_senha2:
              conexao = sqlite3.connect("05_lista_tarefas/bd_lista_tarefas.sqlite")
              cursor = conexao.cursor()

              sql_cadastrar_usuario = """
                  INSERT INTO usuarios(nome, usuario, senha)
                  VALUES(?, ?, ?)
                  """
              
              valores = [self.resposta_nome, self.resposta_usuario, self.resposta_senha]

              cursor.execute(sql_cadastrar_usuario, valores)
              
              conexao.commit()

              messagebox.showinfo(message="você foi cadastrado!")
              self.janela.destroy()
              self.paidocadastro.deiconify()
              
              cursor.close()
              conexao.close()
              
          else:
              messagebox.showerror(message="Suas senhas não são iguais! ")

  def run(self):
    self.janela.mainloop()

if __name__ == "__main__":
    app = Janela_login()
    app.run()



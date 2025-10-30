import sqlite3
import ttkbootstrap as ttk
from tkinter import messagebox
from classe_cadastro import Janela_cadastro


class Login():

    def __init__(self,janela_pai):

        #Estou transformando o parametro em um atributo para poder
        #usar em qualquer método(função)
        self.janela_pai = janela_pai

        self.janela = ttk.Toplevel(janela_pai)
        self.janela.geometry("400x500")

        #Configurando para que quando feche a janela de login ele encerre o programa
        self.janela.protocol("WM_DELETE_WINDOW", self.sair)

        self.janela.iconbitmap("IMG/logo.ico")

        ttk.Label(self.janela,text="Usuário", font=("Arial", 14), padding=20).pack()

        self.login = ttk.Entry(self.janela)
        self.login.pack(pady=20)

        ttk.Label(self.janela,text="Senha", font=("Arial", 14), padding=2).pack()

        self.senha = ttk.Entry(self.janela,show="*")
        self.senha.pack(pady=20)

        self.frame_botao = ttk.Frame(self.janela)
        self.frame_botao.pack()

        ttk.Button(self.frame_botao,
                   text="LOGIN",
                   padding=10,
                   width=20,
                   style="Success",
                   command=self.logar).pack(side="left",pady=100)
        ttk.Button(self.frame_botao,
                   text="SAIR",
                   padding=10,
                   width=20,
                   style="Danger",
                   command=self.sair).pack(side="right",padx=20)
        
        ttk.Button(self.janela,
                   text="CADASTRAR",
                   style = "Primary",
                   command=self.abrir_tela_cadastro).pack(pady=10)

    def run(self):
        self.janela.mainloop()

    def abrir_tela_cadastro(self):
        Janela_cadastro(self.janela)

    def sair(self):
        resposta = messagebox. askyesno ( title="Login", message= "Você deseja mesmo sair?" )
        if resposta == True:
            exit()


    def logar(self):
        #Pegando os valores das caixas de entrada (Entry)
        usuario_senha = (self.senha.get())
        usuario_nome =  (self.login.get())

        conexao = sqlite3.connect("./bd_lista_tarefa.sqlite")
        cursor = conexao.cursor()
        cursor.execute(
            """
            SELECT nome, usuario FROM usuario
                WHERE usuario = ? AND senha = ?;
            """,
            [usuario_nome,usuario_senha]
        )

        resultado = cursor.fetchone()
        
        conexao.close()

        # Se o resultado for diferente de vazio,
        # ou seja, ele encontrou alguem com essa informação
        # eu abro a lista de tarefas
        if resultado != None:
            messagebox.showinfo(title="Login realizado com sucesso!", message=f"Bem-vindo, {resultado[0]}!!")
            self.janela.destroy()
            #Reexibe a janela principal, a janela de tarefas
            self.janela_pai.deiconify()

        else:
            messagebox.showerror(title="ERRO", message="Senha e Usuário invalidos")


if __name__ == "__main__":
    tela_login = Login("Login usuario")
    tela_login.run()

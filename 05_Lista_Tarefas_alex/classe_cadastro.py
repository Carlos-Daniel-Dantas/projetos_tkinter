import ttkbootstrap as ttk
import sqlite3
from tkinter import messagebox


class Janela_cadastro():

    def __init__(self, janela_pai):

        #Criando a janela filha
        self.janela_cadastro = ttk.Toplevel(janela_pai)
            
        #Criando o titulo
        ttk.Label(self.janela_cadastro,
                  text="CADASTRO DE USUÁRIO").pack()
        
        #Label do Nome
        ttk.Label(self.janela_cadastro,
                  text="Digite seu nome completo:").pack()
        
        #Criando a caixa de texto do nome
        self.caixinha_nome = ttk.Entry(self.janela_cadastro)
        self.caixinha_nome.pack()

        self.janela_cadastro.geometry("800x400+500+290")
        self.janela_cadastro.iconbitmap("IMG/logo.ico")

        #Label do Usuario
        ttk.Label(self.janela_cadastro,
                  text="Digite seu usuário:").pack()
        
        #Criando a caixa de texto do usuario
        self.caixinha_usuario = ttk.Entry(self.janela_cadastro)
        self.caixinha_usuario.pack()

        #Label do Senha
        ttk.Label(self.janela_cadastro,
                  text="Digite a sua senha:").pack()
        
        #Criando a caixa de texto do senha
        self.caixinha_senha = ttk.Entry(self.janela_cadastro)
        self.caixinha_senha.pack()

        #botão
        ttk.Button(self.janela_cadastro,
                   text= "Cadastrar",
                   command=self.inserir_usuario
                   ).pack()

        self.criar_tabela_usuario()

    def criar_tabela_usuario(self):
        #Conectando ao banco de dados
        conexao = sqlite3.connect("./bd_lista_tarefa.sqlite")

        #criar cursor
        cursor = conexao.cursor()

        #Executar o comando
        cursor.execute("""
                        CREATE TABLE IF NOT EXISTS usuario (
                            nome VARCHAR(80),
                            usuario VARCHAR (20) PRIMARY KEY,
                            senha VARCHAR(20),
                            
                        );
                    """)
        
        #comito a transação
        conexao.commit()

        #encerro a conexão
        conexao.close()

    def inserir_usuario(self):

        try:
            #criar conexão
            conexao = sqlite3.connect("./bd_lista_tarefa.sqlite")

            #criar cursor
            cursor = conexao.cursor()

            nome = self.caixinha_nome.get()
            usuario = self.caixinha_usuario.get()
            senha = self.caixinha_senha.get()

            #executar
            cursor.execute("""
                            INSERT INTO usuario 
                                (nome,
                                usuario,
                                senha)
                            VALUES
                                (?,
                                ?,
                                ?);                        
                            """,
                            [nome,
                            usuario,
                            senha]
                        )
            
            #comitar
            conexao.commit()

            messagebox.showinfo("Cadastro","Cadastro efetuado com sucesso!")
        
        
        except:
            messagebox.showinfo("Cadastro, Erro ao cadastrar, tente novamnete")
            
        finally:
            #fechar conexão
            conexao.close()

        

    def run(self):
        self.janela_cadastro.mainloop()

if __name__ == "__main__":
    #chamando sem nenhuma janela pai
    #apenas, somente, nada mais que para testar
    janela_cadastro = Janela_cadastro("Cadastro usuario.")
    janela_cadastro.run()
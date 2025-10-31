import ttkbootstrap as ttk
from tkinter import Listbox, END
from tkinter import messagebox
from classe_login import Login
import sqlite3


class Janela_Lista_Tarefas():

    def __init__(self):

        #Criando a janela
        self.janela = ttk.Window(themename="cyborg")
        self.janela.geometry("1200x900+400+50")
        self.janela.iconbitmap("IMG/logo.ico")

        #Criando o Titulo
        ttk.Label (self.janela, text="Lista de Tarefas", font=54).pack()

        #Criando um frame para guardar a caixa de texto e o botão adicnioanr
        frame_add = ttk.Frame(self.janela)
        frame_add.pack(fill="x", padx=20)

        #Criando a caixa de texto
        self.add_tarefa = ttk.Entry(frame_add)
        self.add_tarefa.pack(side="left",  fill="x", expand=True)

        #Criando o botão adicionar
        ttk.Button(frame_add,
                   text="Adicionar",
                   command=self.adicionar_tarefa
                   ).pack(side="right")
        
        #Criando a lista
        self.lista = Listbox(self.janela, font=("Segoe UI", 12), height=30)
        self.lista.pack(pady=20, padx=20, fill='both', expand=True)

        #Criando o frame para guardar os botões excluir e marcar como conlcuido
        frame_botao = ttk.Frame(self.janela)
        frame_botao.pack(side="bottom",
                         fill="x",
                         expand=True,
                         padx=20,
                         pady=(0,20))
        
        #Criando o botão excluir
        botao_excluir = ttk.Button(frame_botao, 
                                   command= self.deletar_tarefa,
                                   text="Excluir",
                                   width=50,
                                   style="danger")
        botao_excluir.pack(side="left",padx=20)
        
        #Criando o botão marcar como concluido
        botao_marcar = ttk.Button(frame_botao,
                                  text="Marcar como concluido",
                                  width=50,
                                  style="warning",
                                  command=self.marcar_concluido)
        botao_marcar.pack(side="right",padx=20)

        #conectando ao banco de dados
        conexao = sqlite3.connect("./bd_lista_tarefa.sqlite")

        #criando o cursor, responsavel por comandar o banco de dados
        cursor = conexao.cursor()

        sql_para_criar_tabela = """
                                    CREATE TABLE IF NOT EXISTS tarefa (
                                    codigo integer primary key autoincrement,
                                    descricao_tarefa varchar(200)
                                    usuario varchar(20),
                                    FOREIGN KEY (usuario) REFERENCES usuarios(usuario);
                                    
                                """
        
        cursor.execute(sql_para_criar_tabela)

        #Comitei as alterações
        conexao.commit()

        #fechei a conexão
        cursor.close()
        conexao.close()

        #Abrindo a janela de login
        Login(self.janela)

        #Escondendo a janela da lista tarefas
        self.janela.withdraw()

        self.atualizar_lista()


    def atualizar_lista(self):
        #ATUALIZAR A LISTA
        conexao = sqlite3.connect("./bd_lista_tarefa.sqlite")
        cursor = conexao.cursor()

        sql_para_selecionar_tarefas =""" SELECT codigo, descricao_tarefa FROM tarefa WHERE usuario = ? """

        cursor.execute(sql_para_selecionar_tarefas, self.usuario_logado)

        lista_de_tarefas = cursor.fetchall()

        cursor.close()
        conexao.close()

        #Inserindo os itens na listbox
        for linha in lista_de_tarefas:
            self.lista.insert("end",linha[1])



    def adicionar_tarefa(self):
        #Pegando o texto da caixa de texto
        tarefa = self.add_tarefa.get()

        #Inserindo a tarefa na lista
        self.lista.insert('end', tarefa)

        conexao = sqlite3.connect("./bd_lista_tarefa.sqlite")

        cursor = conexao.cursor()

        #aqui vai o sql do insert
        sql_insert = f""" 
                        INSERT INTO tarefa (descricao_tarefa)
                        VALUES (?)
                    """
        
        cursor.execute(sql_insert,[tarefa])

        conexao.commit()
        cursor.close()
        conexao.close()


    def deletar_tarefa(self):
        excluir_indice = self.lista.curselection()

        if excluir_indice:
            self.lista.delete(excluir_indice)
        else:
            messagebox.showerror(message="Selecione um item antes de excluir!")

    def marcar_concluido(self):
        # Pegar o indice do item selecionado
        index_selecionado = self.lista.curselection()

        # Usando um if verifique se um item foi selecionado
        if index_selecionado:
            #Guarde em uma variavel o texto do item selecionado
            texto_item = self.lista.get(index_selecionado)

            #Exclua o item selecionado
            self.lista.delete(index_selecionado)

            #Inclua na mesma posição do item que foi excluido o texto novamente com o final "[CONCLUIDO]"
            novo_texto = texto_item + " [CONCLUIDO]"
            self.lista.insert(index_selecionado, novo_texto)

        # Senão mostra mensagem de erro
        else:
            messagebox.showerror("Selecione um item!")


    def run(self):
        self.janela.mainloop()

if __name__ == "__main__":
    janela = Janela_Lista_Tarefas()
    janela.run()
    


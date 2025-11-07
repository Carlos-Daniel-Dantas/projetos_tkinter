import ttkbootstrap as ttk
import sqlite3
from tkinter import messagebox
import tkinter

class rastreador_de_habitos():

        def __init__(self):


                self.janela = ttk.Window(themename="cyborg") # cria a janela principal tree =
                self.janela.title("Rastreador de Hábitos")
                self.janela.geometry("1200x680+300+50")
                self.janela.resizable(False, False)
                self.janela.iconbitmap("IMG/logo.ico")

                frame_add = ttk.Frame(self.janela)
                frame_add.pack(fill="x", pady=10)

                self.treeview = ttk.Treeview(frame_add, style="primary", height=15, columns=("id", "hábito", "descrição", "frequencia")) # cria o widget Treeview tree.pack(fill="both", expand=True), cria as colunas e o cabeçalho
                self.janela.title("Projeto Rastreador de Hábitos")
                self.treeview["show"] = "headings"

                #----------------Valor Coluna - text = Nome de exebição-----------------
                self.treeview.heading("hábito", text="hábito")
                self.treeview.heading("descrição", text="Descrição")
                self.treeview.heading("frequencia", text="Frequência",)
                self.treeview.heading("id", text="id",)
                self.treeview.pack(padx=10, pady=20)#Mostrar o os textos de exibição

                self.treeview.column("id", anchor="center", width=25)
                self.treeview.column("hábito", anchor="center", width=380)
                self.treeview.column("descrição", anchor="center", width=450)
                self.treeview.column("frequencia", anchor="center", width=450)

                #-----------------Criando banco de dados--------------------------------

                #conectando ao banco de dados
                conexao = sqlite3.connect("06_projeto_treeview/habitos.db")
                #criando o cursor, responsavel por comandar o banco de dados
                cursor = conexao.cursor()

                sql_para_criar_tabela = """
                                        CREATE TABLE IF NOT EXISTS hábitos (
                                        codigo INTEGER primary key autoincrement,
                                        habito varchar(20),
                                        descricao varchar(20),
                                        frequencia varchar(20)
                                        );
                        
                                        """
                self.atualizar_tudo()
                cursor.execute(sql_para_criar_tabela)
                conexao.commit()
                cursor.close()
                conexao.close()

                #treeview.insert("", "end", values=["Godofredo", "3", "Matão"]) #Resultado das colunas da tabela  #END adiciona ao final


                adicionar = ttk.Button(frame_add,
                        text= "Adiconar hábito", 
                        style="success",
                        width=25,
                        command=self.adicionar_habito
                        ).pack(side="right", padx=10)
                
                remover = ttk.Button(frame_add,
                        text= "Remover selecionado", 
                        style="danger",
                        width=25,
                        command=self.excluir_habito
                        ).pack(side="right", padx=10)
                
                editar = ttk.Button(frame_add,
                        text= "Editar hábito", 
                        style="warning",
                        width=25,
                        command=self.alterar_funcao
                        ).pack(side="right", padx=10)

                ttk.Entry(frame_add
                        )
                
                ttk.Label(self.janela,
                        text="HÁBITO", font=24).place(x=30, y=300)
                
                ttk.Label(self.janela,
                        text="DESCRIÇÃO", font=24).place(x=30, y=425)
                
                ttk.Label(self.janela,
                        text="FREQUÊNCIA", font=24).place(x=30, y=545)
                

                self.campo_adicionar = ttk.Entry(self.janela) 
                self.campo_adicionar.place(x=25, y=350, width=450)

                self.campo_descricao = ttk.Entry(self.janela) 
                self.campo_descricao.place(x=25, y=470, width=450)

                self.campo_frequencia = ttk.Entry(self.janela) 
                self.campo_frequencia.place(x=25, y=590, width=450)


        def adicionar_habito(self):

                habito = self.campo_adicionar.get()

                descricao = self.campo_descricao.get()

                frequencia = self.campo_frequencia.get()

        #-----------------------------------------------------------------------------------
                conexao = sqlite3.connect("06_projeto_treeview/habitos.db")

                cursor = conexao.cursor()

                #aqui vai o sql do insert
                sql_insert = f""" 
                                INSERT INTO hábitos (habito,descricao, frequencia)
                                VALUES (?,?,?)
                        """
                
                valor = [habito, descricao, frequencia]
                
                cursor.execute(sql_insert, valor)

                conexao.commit()
                cursor.close()
                conexao.close()

                novo_id = cursor.lastrowid
                
                self.treeview.insert("","end", values=[novo_id, habito, descricao, frequencia])

        def atualizar_tudo(self):
                # 1. Limpa o treeview (OK)
                for item in self.treeview.get_children():
                        self.treeview.delete(item) 
                
                conexao = sqlite3.connect("06_projeto_treeview/habitos.db")
                cursor = conexao.cursor()

                sql_select = "SELECT codigo, habito, descricao, frequencia FROM hábitos"
                
                cursor.execute(sql_select)
                dados = cursor.fetchall() 
                conexao.commit() 
                cursor.close()
                conexao.close()

                for dado in dados: 
                        self.treeview.insert("", "end", values=dado)
                        

#-----------------------------------------------------------------------------------

        def excluir_habito(self):
                
                item_selecionado = self.treeview.selection()[0]

                valores = self.treeview.item(item_selecionado, "values")
                codigo_para_excluir = valores[0]

                if item_selecionado:

                        with sqlite3.connect("06_projeto_treeview/habitos.db") as conexao:
                                cursor = conexao.cursor()

                                sql_delete = """
                                                delete from hábitos
                                                WHERE codigo = ?
                                                
                                                """
                                
                        cursor.execute(sql_delete, (codigo_para_excluir,))
                                        
                        conexao.commit() 

                        self.treeview.delete(item_selecionado)

                        cursor.close()
                        conexao.close()

        def alterar_funcao(self):

                """Funcao para alterar itens da lista de carros."""
                selecionado = self.treeview.selection()
                if selecionado:
                        # Pegando os novos coisas que vao ser alterada
                        habito = self.campo_adicionar.get()
                        frequencia = self.campo_frequencia.get()
                        descricao = self.campo_descricao.get()

                if habito != None and descricao != None and frequencia != None:
                        # Pegando a linha do carro que foi selecionado
                        habito_id = self.treeview.item(selecionado)["values"][0]

                        # Atualizando no banco de dados
                        conexao = sqlite3.connect("06_projeto_treeview/habitos.db")
                        cursor = conexao.cursor()

                        alterar_habitos = """
                        UPDATE hábitos
                        SET habito = ?, descricao = ?, frequencia = ?
                        WHERE codigo = ?
                        """
                        valores = [habito, descricao, frequencia, habito_id]
                        cursor.execute(alterar_habitos, valores)
                        
                        conexao.commit()
                        cursor.close()
                        conexao.close()

                        self.atualizar_tudo()
                        # Limpando os campos do formulário
                        self.campo_adicionar.delete(0, "end")
                        self.campo_frequencia.delete(0, "end")
                        self.campo_descricao.delete(0, "end")
                else:
                        messagebox.showwarning("Aviso", "Você esqueceu de preencher algum campo")

        def confirmar_saida(self):

                resposta = messagebox.showinfo("DESEJA REALMENTE SAIR ?")
                if resposta == True:
                        self.janela.destroy()
                
        def run(self):

                self.janela.mainloop()

if __name__ == "__main__":
    janela = rastreador_de_habitos()
    janela.run()
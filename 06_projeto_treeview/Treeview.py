import ttkbootstrap as ttk
import sqlite3

class rastreador_de_habitos():

    def __init__(self):


        self.janela = ttk.Window(themename="superhero") # cria a janela principal tree =
        self.janela.title("Rastreador de Hábitos")
        self.janela.geometry("1000x680+300+50")

        frame_add = ttk.Frame(self.janela)
        frame_add.pack(fill="x", padx=20)

        ttk.Label(frame_add,
                text="MEUS HÁBITOS",
                font=("Arial", 20),
                style="light",).pack(pady=20)

        self.treeview = ttk.Treeview(frame_add, columns=("hábito", "descrição", "frequencia"), show="headings", style="primary") # cria o widget Treeview tree.pack(fill="both", expand=True), cria as colunas e o cabeçalho
        self.janela.title("Projeto Rastreador de Hábitos")
        self.treeview["show"] = "headings"

        #----------------Valor Coluna - text = Nome de exebição-----------------
        self.treeview.heading("hábito", text="hábito")
        self.treeview.heading("descrição", text="Descrição")
        self.treeview.heading("frequencia", text="Frequencia",)
        self.treeview.pack(pady=20)#Mostrar o os textos de exibição

        self.treeview.column("hábito", anchor="center", width=270)
        self.treeview.column("descrição", anchor="center", width=270)
        self.treeview.column("frequencia", anchor="center", width=270)

        #-----------------Criando banco de dados--------------------------------

        #conectando ao banco de dados
        conexao = sqlite3.connect("06_projeto_treeview/habitos.db")
        #criando o cursor, responsavel por comandar o banco de dados
        cursor = conexao.cursor()

        sql_para_criar_tabela = """
                                    CREATE TABLE IF NOT EXISTS hábitos (
                                    codigo integer primary key autoincrement,
                                    habito varchar(20),
                                    descricao varchar(20),
                                    frequencia varchar(20)
                                    );
                    
                                """
        
        cursor.execute(sql_para_criar_tabela)
        conexao.commit()
        cursor.close()
        conexao.close()

        #treeview.insert("", "end", values=["Godofredo", "3", "Matão"]) #Resultado das colunas da tabela  #END adiciona ao final


        adicionar = ttk.Button(frame_add,
                    text= "Adiconar hábito", 
                    style="success",
                    width=20,
                    command=self.adicionar_habito
                    ).pack(side="right", padx=10)
        
        remover = ttk.Button(frame_add,
                    text= "Remover selecionado", 
                    style="danger",
                    width=20,
                    command=self.excluir_habito
                    ).pack(side="right", padx=10)
        
        editar = ttk.Button(frame_add,
                    text= "Editar hábito", 
                    style="warning",
                    width=20,
                    command=self.excluir_habito
                    ).pack(side="right", padx=10)

        ttk.Entry(frame_add
                )
        
        ttk.Label(self.janela,
                text="Hábito").place(x=30, y=320)
        
        ttk.Label(self.janela,
                text="Descrição").place(x=30, y=395)
        
        ttk.Label(self.janela,
                text="Frequencia").place(x=30, y=475)
        

        self.campo_adicionar = ttk.Entry(self.janela) 
        self.campo_adicionar.place(x=25, y=350, width=250)

        self.campo_descricao = ttk.Entry(self.janela) 
        self.campo_descricao.place(x=25, y=430, width=250)

        self.campo_frequencia = ttk.Entry(self.janela) 
        self.campo_frequencia.place(x=25, y=510, width=250)

    def adicionar_habito(self):

        habito = self.campo_adicionar.get()

        descricao = self.campo_descricao.get()

        frequencia = self.campo_frequencia.get()

        self.treeview.insert("", "end", values=[habito, descricao, frequencia])

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

#-----------------------------------------------------------------------------------

    def excluir_habito(self):
        
        item_selecionado = self.treeview.selection()
        self.treeview.delete(item_selecionado)

    def run(self):

        self.janela.mainloop()

if __name__ == "__main__":
    janela = rastreador_de_habitos()
    janela.run()
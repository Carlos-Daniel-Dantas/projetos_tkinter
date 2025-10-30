import ttkbootstrap as ttk


class Rastreador_de_Habitos():
    def __init__(self):

        self.janela = ttk.Window(themename="cyborg")
        self.janela.title("Rastreador de Hábitos")
        self.janela.geometry("1600x900")

        treeview = ttk.Treeview(self.janela, columns=("nome", "idade", "cidade"), show="headings") # cria o widget Treeview tree.pack(fill="both", expand=True), cria as colunas e o cabeçalho
        self.janela.title("Projeto Rastreador de Hábitos")

        #----------------Valor Coluna - text = Nome de exebição-----------------
        treeview.heading("nome", text="Nome") 
        treeview.heading("idade", text="Idade")
        treeview.heading("cidade", text="Cidade")

        treeview.pack()#Mostrar o os textos de exibição
        treeview.insert("", "end", values=["Godofredo", "3", "Matão"]) #Resultado das colunas da tabela  #END adiciona ao final

        ttk.Button(self.janela, text="Deletar")


        self.janela.mainloop()



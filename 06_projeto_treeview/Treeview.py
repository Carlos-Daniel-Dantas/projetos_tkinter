import ttkbootstrap as ttk
import sqlite3


janela = ttk.Window(themename="superhero") # cria a janela principal tree =
janela.title("Rastreador de Hábitos")
janela.geometry("800x600+400+50")

frame_add = ttk.Frame(janela)
frame_add.pack(fill="x", padx=20)

ttk.Label(janela,
          text="Meus hábitos",
          font=("Arial", 24),
          style="light",).pack(padx=20)

treeview = ttk.Treeview(frame_add, columns=("id", "hábito", "descrição", "frequencia"), show="headings") # cria o widget Treeview tree.pack(fill="both", expand=True), cria as colunas e o cabeçalho
janela.title("Projeto Rastreador de Hábitos")

#----------------Valor Coluna - text = Nome de exebição-----------------
treeview.heading("id", text="id") 
treeview.heading("hábito", text="hábito")
treeview.heading("descrição", text="Descrição")
treeview.heading("frequencia", text="Frequencia")
treeview.pack(side="right")#Mostrar o os textos de exibição


#treeview.insert("", "end", values=["Godofredo", "3", "Matão"]) #Resultado das colunas da tabela  #END adiciona ao final


adicionar = ttk.Button(frame_add,
            text= "Adiconar hábito", 
            style="success",
            width=20
            ).pack(side="top", pady=5)

editar = ttk.Button(frame_add,
            text= "Editar hábito",
            style="warning",
            width=20
           ).pack(side="top", pady=5)

remover = ttk.Button(frame_add,
            text= "Remover selecionado",
            style="danger",
            width=20
           ).pack(pady=5)



janela.mainloop()


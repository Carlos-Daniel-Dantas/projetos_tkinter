import ttkbootstrap as ttk
import sqlite3
from tkinter import messagebox


class rastreador_de_habitos():

    def __init__(self):


        self.janela = ttk.Window(themename="cyborg") 
        self.janela.title("SORTEIO PREMIADO COM FRUTAS")
        self.janela.geometry("500x700")
        self.janela.resizable(False, False)
        self.janela.iconbitmap("IMG/logo.ico")

        self.lista_frutas = ['🍎', '🍌', '🍇', '🍊', '🍍', '🍓']

        ttk.Label(self.janela, text="Cassino das Frutas", font=("Helvetica", 24, "bold"), bootstyle="primary").pack(pady=20)

        frame_frutas = ttk.Frame(self.janela)
        frame_frutas.pack(pady=27)

        self.lbl_fruta1 = ttk.Label(frame_frutas, text="?", font=("Arial", 64), bootstyle="info", padding=10, relief="solid")
        self.lbl_fruta1.pack(side='left', padx=10)
        
        self.lbl_fruta2 = ttk.Label(frame_frutas, text="?", font=("Arial", 64), bootstyle="info", padding=10, relief="solid")
        self.lbl_fruta2.pack(side='left', padx=10)
        
        self.lbl_fruta3 = ttk.Label(frame_frutas, text="?", font=("Arial", 64), bootstyle="info", padding=10, relief="solid")
        self.lbl_fruta3.pack(side='left', padx=10)

        self.btn_sortear = ttk.Button(frame_frutas, text="Sortear!", 
                                      bootstyle="success-outline", 
                                      )
        self.btn_sortear.pack(pady=2, ipadx=20, ipady=1)

        #___________________________________________________________________

        frame_frutas = ttk.Frame(self.janela)
        frame_frutas.pack(pady=27, fill="x")

        self.treeview = ttk.Treeview(frame_frutas, style="primary", height=15,  columns=("frutas")) # cria o widget Treeview tree.pack(fill="both", expand=True), cria as colunas e o cabeçalho
        self.janela.title("Projeto Rastreador de Hábitos")
        self.treeview["show"] = "headings"

        #----------------Valor Coluna - text = Nome de exebição-----------------
        self.treeview.heading("frutas", text="frutas")
        self.treeview.pack(pady=100)#Mostrar o os textos de exibição

        self.treeview.column("frutas", anchor="center", width=450)


    def run(self):

            self.janela.mainloop()

if __name__ == "__main__":
    janela = rastreador_de_habitos()
    janela.run()
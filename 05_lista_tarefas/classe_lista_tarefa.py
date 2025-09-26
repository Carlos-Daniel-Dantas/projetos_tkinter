import ttkbootstrap as tk
from tkinter import Listbox, END
from tkinter import Messagebox


class janela_Lista_Tarefas():
  """Classe para a criação da self.janela principal"""

  def __init__(self):

    self.janela = tk.Window(themename='vapor')
    self.janela.title("LISTA TAREFAS")
    self.janela.geometry("1200x900+80+50")

    #Texto Adicionar
    self.tarefas = tk.Label(text="LISTA TAREFAS",
                            style="danger",
                            font=("Arial", 24)).pack(pady=20)

    self.frame_add = tk.Frame(self.janela)
    self.frame_add.pack(fill="x",padx=50)

    self.add_tarefa = tk.Entry(self.frame_add)
    self.add_tarefa.pack(side="left", fill="x", expand=True)

    tk.Button(self.frame_add, text="ADICIONAR", cursor="hand2", command=self.adicionar_tarefa).pack(side="right", padx=10)

    self.lista = Listbox(self.janela, font=("Segoe UI", 12), height=10)
    self.lista.pack(padx=20,pady=20,fill='both', expand=True)

                         
    frame_botao = tk.Frame(self.janela)
    frame_botao.pack(side="bottom", 
                     padx=20, 
                     fill="both")

    botao_excluir = tk.Button(frame_botao, 
                              text="Excluir", 
                              style="Danger", command=self.excluir_tarefa)
    
    botao_excluir.pack(side="left", padx=20)

    botao_marcar = tk.Button(frame_botao, 
                             text="marcar como concluido", 
                             width=30, 
                             style="primary",
                             command=self.concluir_tarefa)
    
    botao_marcar.pack(side="right", padx=20)


  def adicionar_tarefa(self):
     #pegango o texto da caixa de texto
     tarefa = self.add_tarefa.get()

     self.lista.insert(0, tarefa)

  def excluir_tarefa(self):

      item_selecionado = self.lista.curselection()
      self.lista.delete(item_selecionado[0])
     

  def concluir_tarefa(self):
     
      item_concluido = self.lista.curselection()
      self.lista.itemconfig(item_concluido, {"fg": "red", "selectforeground": "blue"})


  def confirmar_saida():
    resposta = messagebox.askyesno("Confirmação", "Deseja realmente sair?")
    if resposta:
        self.janela.destroy()


  def run(self):
    self.janela.mainloop()

if __name__ == "__main__":
    app = janela_Lista_Tarefas()
    app.run()



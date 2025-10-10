import ttkbootstrap as tk
from tkinter import Listbox, END
from tkinter import messagebox
import sqlite3


class janela_Lista_Tarefas():
  """Classe para a criação da self.janela principal"""

  def __init__(self):
    
    self.janela = tk.Window(themename='cyborg')
    self.janela.title("LISTA TAREFAS")
    self.janela.geometry("1200x900+400+50")

    #Texto Adicionar
    self.tarefas = tk.Label(text="LISTA TAREFAS",
                            style="danger",
                            font=("Arial", 24)).pack(pady=20)
    
    self.janela.iconbitmap("IMG/logo.ico")

    self.frame_add = tk.Frame(self.janela)
    self.frame_add.pack(fill="x",padx=50)

    self.add_tarefa = tk.Entry(self.frame_add)
    self.add_tarefa.pack(side="left", fill="x", expand=True)

    tk.Button(self.frame_add, text="ADICIONAR", cursor="hand2", command=self.adicionar_tarefa).pack(side="right", padx=10)

    self.lista = Listbox(self.janela, font=("Segoe UI", 12), height=10)
    self.lista.pack(padx=15,pady=20,fill='both', expand=True)

                         
    frame_botao = tk.Frame(self.janela)
    frame_botao.pack(side="bottom", 
                     padx=20, 
                     fill="both")

    botao_excluir = tk.Button(frame_botao, 
                              text="Excluir", 
                              style="Danger", command=self.excluir_tarefa,
                              cursor="hand2",
                              width=40
                              )
    
    botao_excluir.pack(side="left", padx=20)

    botao_marcar = tk.Button(frame_botao, 
                             text="marcar como concluido", 
                             width=40, 
                             style="primary",
                             command=self.concluir_tarefa,
                             cursor="hand2")
    
    botao_marcar.pack(side="right", pady=20)

   #Conectando ao banco de dados
    conexao = sqlite3.connect("05_lista_tarefas/bd_lista_tarefas.sqlite")

   #Criando responsavel por comandar o Banco de Dados 
    cursor = conexao.cursor()

   #Criando tabela 
    sql_para_criar_tabela = """
                                 CREATE TABLE IF NOT EXISTS tarefa (
                                 codigo integer primary key autoincrement,
                                 descricao_tarefa varchar(200)
                                 );
                            """
    cursor.execute(sql_para_criar_tabela)

    # Confirma as alterações
    conexao.commit()
    
    #fechei a conexão
    cursor.close()
    conexao.close()

    self.atualizar_lista()

  def atualizar_lista(self):

      #atualizar tarefa 

      conexao = sqlite3.connect("05_lista_tarefas/bd_lista_tarefas.sqlite")
      cursor = conexao.cursor()

      sql_para_selecionar_tarefas = """
                                       select codigo, descricao_tarefa from tarefa;
                                    """
      cursor.execute(sql_para_selecionar_tarefas)

      lista_de_tarefas =cursor.fetchall()

      cursor.close()
      conexao.close()

      #inserindo items listbox
      for linha in lista_de_tarefas:
         self.lista.insert("end", linha[1])

  def adicionar_tarefa(self):
     #pegango o texto da caixa de texto
     tarefa = self.add_tarefa.get()

     self.lista.insert(0, tarefa)

     conexao = sqlite3.connect("05_lista_tarefas/bd_lista_tarefas.sqlite")
     cursor = conexao.cursor()

     sql_insert = """
                     INSERT INTO tarefa (descricao_tarefa)
                     VALUES (?)

                 """
     
     cursor.execute(sql_insert,[tarefa])
     conexao.commit()

     cursor.close()
     conexao.close()

  def excluir_tarefa(self):
      
      item_selecionada = self.lista.curselection()

      excluir_tarefa = item_selecionada

      if excluir_tarefa:

         texto_tarefa = self.lista.get(excluir_tarefa)

         self.lista.delete(excluir_tarefa)


         with sqlite3.connect("05_lista_tarefas/bd_lista_tarefas.sqlite") as conexao:
            cursor = conexao.cursor()

            sql_delete = """
                              delete from tarefa 
                              WHERE descricao_tarefa = ?

                         """
            
            cursor.execute(sql_delete, excluir_tarefa,)

            conexao.commit()

            cursor.close()
            conexao.close()

      else:
         messagebox.showerror(message="Selecione um item antes de excluir")

  def concluir_tarefa(self):
     item_selecionada = self.lista.curselection()
     
     if item_selecionada:
         texto_tarefa = self.lista.get(item_selecionada)
       
         if "[CONCLUIDO]" not in texto_tarefa:
            self.lista.delete(item_selecionada[0])
            texto_tarefa_concluido = texto_tarefa + "[CONCLUÍDO]"
            self.lista.insert(item_selecionada[0], texto_tarefa_concluido)

                  
            with sqlite3.connect("05_lista_tarefas/bd_lista_tarefas.sqlite") as conexao:
               cursor = conexao.cursor()

               sql_uptade = """     
                                 UPDATE tarefa
                                 SET descricao_tarefa = ?
                                 WHERE descricao_tarefa = ?;
                              """
                  
               valores = (texto_tarefa_concluido, texto_tarefa)

               cursor.execute(sql_uptade, valores)
     else:
            messagebox.showerror("Aviso", "Selecione uma tarefa para concluir.")     


  def confirmar_saida(self):
    

    resposta = messagebox.showinfo("DESEJA REALMENTE SAIR ?")
    if resposta == True:
        self.janela.destroy()

  def run(self):
    self.janela.mainloop()

if __name__ == "__main__":
    app = janela_Lista_Tarefas()
    app.run()



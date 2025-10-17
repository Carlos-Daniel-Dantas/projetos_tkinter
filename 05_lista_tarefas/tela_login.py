import ttkbootstrap as ttk
from ttkbootstrap.dialogs import Messagebox
from classe_lista_tarefa import janela_Lista_Tarefas


class Janela():

    def __init__(self):

        #Janela
        self.janela = ttk.Window(themename="cyborg",
                                   title="Login")
        self.janela.geometry("800x400+500+290")
        self.janela.resizable(False, False)

        self.label_titulo = ttk.Label(self.janela, text="FAÇA SEU LOGIN PARA AVANÇAR",
                                      style="light",
                                      font=("Arial", 12))
        self.label_titulo.pack(pady=20)

        self.janela.iconbitmap("IMG/logo.ico")

        self.campos = ttk.Frame(self.janela)
        self.campos.pack(pady=10)

        #------------------------------------------------------------------#

        self.usuario = ttk.Label(self.campos, text="USUÁRIO") #Caixa 01 peso
        self.usuario.pack(padx=10)

        self.usuario = ttk.Entry(self.campos, width=25,
                                    ) #Largura da caixa
        self.usuario.pack(padx=10) 

        #------------------------------------------------------------------#

        self.senha = ttk.Label(self.campos, text="SENHA") #02 altura 
        self.senha.pack(padx=10)

        self.senha = ttk.Entry(self.campos, width=25) #Largura da caixa
        self.senha.pack(padx=10)

        #------------------------------------------------------------------#

        # Botão 
        self.botao_avancar = ttk.Button(self.janela,
                                           text="LOGAR",
                                           command= self.login,
                                           cursor="hand2"
                                           )
        
        self.botao_avancar.place(y=200,x=320)

        #BOTÃO 02
        self.botao_sair = ttk.Button(self.janela,
                                           text="SAIR",
                                           command=self.sair,
                                           cursor="hand2"
                                           )
        
        self.botao_sair.place(y=200,x=420)

        #------------------------------------------------------------------#

    def login(self):
        self.resposta_usuario = self.nova_usu.get()
        self.resposta_senha = self.nova_senha.get()

        if self.resposta_usuario == "1" and self.resposta_senha == "1":
            #Messagebox.show_info(message="Login feito com Sucesso!", title="Sucesso", alert=True)
            janela_tarefas = janela_Lista_Tarefas()
            janela_tarefas.run()
            self.janela.destroy()
        else:
            Messagebox.show_info(message="Login Mal sucedido, informe a senha e o usuario certo", title="Falha", alert=True)

    def sair(self):

        resposta = Messagebox.show_question("DESEJA REALMENTE SAIR ?", "Deseja sair?")
        if resposta == True:
            exit()

    def run(self):
        self.janela.mainloop()

if __name__ == "__main__":
    app = Janela()
    app.run()



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

        # Campos de entrada para peso e altura
        self.campos = ttk.Frame(self.janela)
        self.campos.pack(pady=10)

        self.label_usu = ttk.Label(self.campos, text="USUÁRIO") #Caixa 01 peso
        self.label_usu.pack(padx=10)

        self.nova_usu = ttk.Entry(self.campos, width=25,
                                    ) #Largura da caixa
        self.nova_usu.pack(padx=10) 


        self.label_senha = ttk.Label(self.campos, text="SENHA") #02 altura 
        self.label_senha.pack(padx=10)

        self.nova_senha = ttk.Entry(self.campos, width=25) #Largura da caixa
        self.nova_senha.pack(padx=10)

        # Botão 
        self.botao_avancar = ttk.Button(self.janela,
                                           text="LOGAR",
                                           command= self.login,
                                           cursor="hand2"
                                           )
        
        self.botao_avancar.place(y=200,x=320)

        #BOTÃO 02
        self.botao_avancar2 = ttk.Button(self.janela,
                                           text="SAIR",
                                           command=self.sair,
                                           cursor="hand2"
                                           )
        
        self.botao_avancar2.place(y=200,x=320)


        self.botao_redefinir = ttk.Button(self.janela,
                                           text="ESQUECI MINHA SENHA",
                                           command= self.redefinir,
                                           cursor="hand2"
                                           )
        
        self.botao_redefinir.place(y=250,x=315)

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

    def redefinir(self):


        self.janela.resizable(True, True)

        self.redefinir = ttk.Window(themename="cyborg",
                                    title="REDEFINIR SENHA")
        self.redefinir.geometry("800x400+500+290")
        self.redefinir.resizable(False, False)

        self.campos = ttk.Frame(self.redefinir)
        self.campos.pack(pady=10)

        self.label_usu2 = ttk.Label(self.campos, text="NOVO USUARIO") #Caixa 01 peso
        self.label_usu2.pack(padx=10)

        self.nova_usu2 = ttk.Entry(self.campos, width=25,
                                    ) #Largura da caixa
        self.nova_usu2.pack(padx=10) 

        self.label_senha2 = ttk.Label(self.campos, text="NOVA SENHA") #02 altura 
        self.label_senha2.pack(padx=10)

        self.nova_senha2 = ttk.Entry(self.campos, width=25) #Largura da caixa
        self.nova_senha2.pack(padx=10)

        self.botao_redefinir2 = ttk.Button(self.redefinir,
                                           text="CONCLUIR",
                                           command= self.redefinir
                                           )
        self.botao_redefinir2.place(y=100,x=400)
        
        self.label_senha2 = self.label_senha2.get()
        self.resposta_usuario.set(self.label_senha2) # O texto do widget Label será atualizado

        self.label_usu2 = self.label_usu2.get()
        self.resposta_usuario.set(self.label_usu2) # O texto do widget Label será atualizado

        self.redefinir.mainloop()


    def run(self):
        self.janela.mainloop()

if __name__ == "__main__":
    app = Janela()
    app.run()



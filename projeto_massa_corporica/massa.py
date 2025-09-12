from google import genai
import ttkbootstrap as ttk

class Janela_chat():
    def __init__(self):


        #Janela
        self.janela = ttk.Window(themename="darkly",
                                   title="TESTE DE MASSA CORPORAL")
        self.janela.geometry("800x400+80+50")
        self.janela.resizable(False, False)
        self.create_widgets()

    def create_widgets(self):
        self.label_titulo = ttk.Label(self.janela, text="DIGITE SEU PESO E SUA ALTURA AQUI")
        self.label_titulo.pack(pady=20)

        # Campos de entrada para peso e altura
        self.campos = ttk.Frame(self.janela)
        self.campos.pack(pady=10)

        self.label_peso = ttk.Label(self.campos, text="Peso:") #Caixa 01 peso
        self.label_peso.pack(side="left", padx=10)

        self.entry_peso = ttk.Entry(self.campos, width=5) #Largura da caixa

        self.entry_peso.pack(side="left", padx=10) 


        self.label_altura = ttk.Label(self.campos, text="Altura:") #02 altura 
        self.label_altura.pack(side="left", padx=10)

        self.entry_altura = ttk.Entry(self.campos, width=5)
        self.entry_altura.pack(side="left", padx=10)

        # Botão 
        self.button_calcular = ttk.Button(self.janela,
                                           text="CALCULAR IMC", 
                                           command=self.calcular_imc)
        self.button_calcular.pack(pady=20)
        
        # Label para exibir o resultadoO
        self.label_resultado = ttk.Label(self.janela, text="")
        self.label_resultado.pack(pady=20)

    def calcular_imc(self):
        try:
            peso = float(self.entry_peso.get())
            altura = float(self.entry_altura.get())
            imc = peso / (altura ** 2)
        
            if altura == 0:
                self.label_resultado.config(text="ALTURA INVALIDA")
                return
            if imc < 18.5:
                diagnostico = "Abaixo do peso"
            elif 18.5 <= imc < 24.9:
                diagnostico = "Peso normal"
            elif 30 <= imc < 34.9:
                diagnostico = "Obesidade Grau 1 "
            elif 35 <= imc < 39.9:
                diagnostico = "Obesidade Grau 2"
            elif imc > 40:
                diagnostico = "Obesidade Morbida"    
            resultado_texto = (f"Seu IMC é {imc}, {diagnostico}")
            
            self.label_resultado.config(text=resultado_texto)
            print(resultado_texto)
        except:
            self.label_resultado.config(text="Coloque apenas números.") # Trata o erro se não for números

    def run(self):
        self.janela.mainloop()

if __name__ == "__main__":
    app = Janela_chat()
    app.run()
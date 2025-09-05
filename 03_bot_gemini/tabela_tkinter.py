import tkinter as tk
from google import genai
import ttkbootstrap as tk

def mostrar_nome():
  """Esta função pega o nome digitado na caixa de texto e deseja um Bom dia"""

  nome_digitado = campo_nome.get()
  label_resultado.config({client.models.generate_content(
    model="gemini-2.5-flash", contents= input("faça uma pergunta: "))
}) #resultado

client = genai.Client(api_key="AIzaSyCxGjJu3TILNzi5EkJIkmp-6sR2uQxZd-E")

janela = tk.Window()
janela.title("Youtube")
janela.geometry("800x600+100+50")

janela = tk.tk(themename='united')

#texto 1
pergunta = tk.Label(janela, text="FAÇA UMA PERGUNTA PARA O PAI DA PROGRAMAÇÃO")
pergunta.pack()

campo_nome = tk.Entry(janela)
campo_nome.pack()

botao_enviar = tk.Button(janela, text="PERGUNTAR", command=mostrar_nome)
botao_enviar.pack(pady=5)

botao_enviar = tk.Button(janela, text="PERGUNTAR", command=mostrar_nome)
botao_enviar.pack(pady=5)

label_resultado = tk.Label(janela, text="")
label_resultado.pack()

janela.mainloop()



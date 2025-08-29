import tkinter as tk

#botão resulta do
def mostrar_nome():
  """Esta função pega o nome digitado na caixa de texto e deseja um Bom dia"""
  nome_digitado = campo_nome.get() 
  label_resultado.config(text=f"Bom dia, {nome_digitado}!") #esultado

#Config janela
janela = tk.Tk()
janela.title("Youtube")
janela.geometry("800x600+100+50")
janela.configure(bg="#3f3f3f")

#texto 1
label_nome = tk.Label(janela, text="Qual Vídeo você deseja assistir:")
label_nome.pack()

#
campo_nome = tk.Entry(janela)
campo_nome.pack()

botao_enviar = tk.Button(janela, text="DESEJAR BOM DIA 4MIL SUPER", command=mostrar_nome)

botao_enviar.pack(pady=5)

label_resultado = tk.Label(janela, text="")
label_resultado.pack()

janela.mainloop()


import tkinter as tk


def mostrar_nome():
  nome_digitado = campo_nome.get() 
  label_resultado.config(text=f"Bom dia, {nome_digitado}!") #esultado
  
janela = tk.Tk()
janela.title("Youtube")
janela.geometry("800x600+100+50")
janela.configure(bg="#3f3f3f")


label_nome = tk.Label(janela, text="Qual Vídeo você deseja assister:")
label_nome.pack()



campo_nome = tk.Entry(janela)
campo_nome.pack()

botao_enviar = tk.Button(janela, text="Enviar", command=mostrar_nome)

botao_enviar.pack(pady=5)

label_resultado = tk.Label(janela, text="")
label_resultado.pack()

janela.mainloop()


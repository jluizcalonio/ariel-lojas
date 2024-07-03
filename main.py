import tkinter as tk
from tkinter import ttk
from classes import *

###### BANCO DE DADOS
bancodedados = BancoDeDados()
print("OK")

###### LÓGICA
# bancodedados.adicionar_loja("loja1")



###### INTERFACE
root = tk.Tk()
root.config(height=600, width=800, pady=20, padx=20)
root.resizable(height=False, width=False)
root.title("Lojas da Ariel")

# Adicionar loja e categoria
loja_nome_label = ttk.Label(text="Nome da loja:")
loja_nome_label.grid(column=0, row=0)
loja_nome_input = ttk.Entry(width=23)
loja_nome_input.grid(column=1, row=0)

categoria_label = ttk.Label(text="Categoria:")
categoria_label.grid(column=0, row=1)
categoria_input = ttk.Combobox()
categoria_input['values'] = ("CAMA, MESA E BANHO", "VESTUÁRIO", "BELEZA", "COZINHA", "MOBÍLIA",
                                  "UTENSÍLIOS GERAIS", "DECORAÇÃO", "PAPELARIA")
categoria_input.grid(column=1, row=1)

def adicionar_lojacat_bttn_func():
    bancodedados.adicionar_loja(loja_nome_input.get())
    bancodedados.adicionar_categoria(categoria_input.get())

adicionar_loja_bttn = ttk.Button(text="Adicionar Loja", command=adicionar_lojacat_bttn_func)
adicionar_loja_bttn.grid(column=2, row=0)


# listagem = Listagem()




root.mainloop()
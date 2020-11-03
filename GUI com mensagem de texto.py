#!/usr/bin/env python
# coding: utf-8

# In[ ]:


# Programa que exibi uma GUI com mensagem de texto
# Utilizei o pacote tkinter https://docs.python.org/pt-br/3/library/tkinter.html

from tkinter import * # importa o pacote tkinter

window = Tk() # cria a janela

window.title("Mensagem de topo da GUI")

label = Label(window, text="Olá Mundo") # definição do label com a mensagem do topo e a mensagem de texto

label.grid(column=0, row=0) # cria o grid com a linha e coluna

window.mainloop() # exibe em tela a GUI


# In[ ]:





# In[ ]:





# In[ ]:





#!/usr/bin/env python
# coding: utf-8

# In[4]:


# Caixa de diálogo para permitir que o usuário escolha uma cor
# O módulo tkinter.colorchooser fornece a classe Chooser como 
# uma interface para o diálogo do seletor de cores nativo. 
# Chooser implementa uma janela de diálogo de escolha de cores modal. 
# A classe Chooser herda da classe Dialog.

# Cria um diálogo de escolha de cores.
from tkinter.colorchooser import askcolor 

def codigocor(): # defini variável codigocor
    cor = askcolor() 
    return cor
print(codigocor()) # imprime variável codigocor


# In[ ]:





# In[ ]:





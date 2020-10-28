#!/usr/bin/env python
# coding: utf-8

# In[14]:


# Trabalhando com Gráficos
# Importando o pacote pyplot 

# Pyplot é o conjunto de funções disponível em matplotlib.pyplot 
# permite a criação de uma figura e uma área padrão para exibir o gráfico na figura, 
# necessitando apenas que você desenhe as linhas na área do gráfico, decore o gráfico 
# com rótulos, etc. A seguir, um exemplo de código para gerar um gráfico simples:)

from matplotlib import pyplot as grafico # Linha de importação do pacote

# Eixo X e Eixo Y
grafico.title("Gráfico Simples") # Título do Gráfico
grafico.plot([5,10,15,20], [2,4,6,8]) # Pontos do Gráfico
grafico.show() # impressão do gráfico em tela                   


# In[ ]:





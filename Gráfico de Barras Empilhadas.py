#!/usr/bin/env python
# coding: utf-8

# In[51]:


from matplotlib import pyplot as grafico # importação do pacote


label_inferior = ['F1', 'F2', 'F3', 'F4', 'F5']  # imprimi a descrição inferior
homens = [15, 20, 23, 10, 18] # faixa de pontuação do grupo dos homens
mulheres = [20, 18, 21, 15, 20] # faixa de pontuação do grupo das mulheres
homem_faixa = [3, 3, 3, 3, 3] # altura da faixa preta em cada barra dos homens
mulher_faixa = [2, 2, 2, 2, 2] # altura da faixa preta em cada barra das mulheres
width = 0.3 # largura das barras 

fig, ax = grafico.subplots()

ax.bar(label_inferior, homens, width, yerr=homem_faixa, label='Homens')
ax.bar(label_inferior, mulheres, width, yerr=mulher_faixa, bottom=homens,
       label='Mulheres')

ax.set_ylabel('Pontuação')
ax.set_title('Gráfico por grupo de gênero')
ax.legend() # impressão da legenda

grafico.show() # impressão do gráfico


# In[ ]:





#!/usr/bin/env python
# coding: utf-8

# In[24]:


import matplotlib
import matplotlib.pyplot as grafico
import numpy as np


labels = ['Julho','Agosto','Setembro','Outubro']
peter_pan = [58,51,42,43]
capitao_gancho = [41,39,42,40]

x = np.arange(len(labels))  
width = 0.3  

fig, ax = grafico.subplots()
rects1 = ax.bar(x - width/2, peter_pan, width, 
                label='Peter Pan')
rects2 = ax.bar(x + width/2, capitao_gancho, width, 
                label='Capitão Gancho')

ax.set_ylabel('Pontos')
ax.set_title('Segundo Turno na Terra do Nunca')
ax.set_xticks(x)
ax.set_xticklabels(labels)
ax.legend()

def autolabel(rects):
    for rect in rects:
        height = rect.get_height()
        ax.annotate('{}'.format(height),
                    xy=(rect.get_x() + rect.get_width()
                        / 2, height),
                    xytext=(0, 0),  
                    textcoords="offset points",
                    ha='center', va='bottom')

autolabel(rects1)
autolabel(rects2)

fig.tight_layout()

grafico.show()


# In[ ]:





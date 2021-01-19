#!/usr/bin/python
# -*- coding: UTF-8 -*-
### Programa para soma de dois numeros.###


__license__ = 'GPL, GNU Public License'
__author__ = 'Sandro Gonçales Funk'
__credits__ = 'http://doc.async.com.br/python/Tkinter/index.htm'

from tkinter import * ## O pacote tkinter (“Tk interface”) é a interface padrão do Python para o kit de ferramentas Tk GUI.
from math import * ## Este módulo fornece acesso às funções matemáticas definidas pelo padrão C.
import sys ## Este módulo fornece acesso a algumas variáveis usadas ou mantidas pelo interpretador.
import os

## Criação da classe Soma
class Soma: 
    def __init__(self, toplevel): ## Definições iniciais

        # Define tamanho e nome da Janela
        toplevel.title('Calculadora para somar dois números')
        toplevel.geometry("380x250")

        # Espaçamento
        self.frame1 = Frame(toplevel)
        self.frame1.pack()
    
        # Tamanho Box1
        self.frame2 = Frame(toplevel)
        self.frame2.pack()                
        
        # Tamanho Box2
        self.frame3 = Frame(toplevel)
        self.frame3.pack()
        
        # Operações
        self.frame4 = Frame(toplevel, pady=8)
        self.frame4.pack()
        
        # Resultado
        self.frame5 = Frame(toplevel)
        self.frame5.pack()

        # Botões
        self.frame6 = Frame(toplevel, pady=8)
        self.frame6.pack()
        
        # Cor e tamanho das letras 
        Label(self.frame1,text='', fg='black',
        font=('Verdana','12'), height=1).pack()
        fonte1=('Verdana','12')

        # Botão Somar
        somar=Button(self.frame4,font=fonte1, text='=',command=self.somar)
        somar.pack(side=LEFT)                  
        
        # Botão Sair
        sair=Button(self.frame6, font=fonte1, text= 'Sair', command=self.sair)
        sair.pack(side=LEFT)
        
        # Box 1 para entrada de número
        Label(self.frame2,text='Valor1 :', font=fonte1,width=8).pack(side=LEFT)
        self.valor1=Entry(self.frame2,width=4,font=fonte1)
        self.valor1.focus_force()
        self.valor1.pack(side=LEFT)

        # Box 2 para entrada de número
        Label(self.frame3,text='Valor2 :',font=fonte1,width=8).pack(side=LEFT)
        self.valor2=Entry(self.frame3,width=4,font=fonte1)
        self.valor2.pack(side=LEFT)

        # Resultado
        self.msg=Label(self.frame5,width=12,font=fonte1)
        self.msg.pack(side=LEFT)

    def somar(self):
        valor1 = self.valor1.get()
        valor2 = self.valor2.get()
        valor1 = float(valor1)
        valor2 = float(valor2)
        c = valor1 + valor2
        c = float(c)
        self.msg['text']= '%f' %(c)            
    
    def sair(self):
        app.destroy()
        
app=Tk()
Soma(app)
app.mainloop()
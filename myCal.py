'''Este codigo esta dividido em 4 fases'''
# 1.0 Definir as funções
# 2.0 Chamar os botões
# 3.0 Declarar as entradas
# 4.0 Declara as variaveis primeiron e segundon
# 4.1 Importar, declara o tk(), e finalizar o mainloop(), e definir as dimensões.

#4.1
from tkinter import * # importando as definiçoes tk
#4.1
myCal = Tk() #começo da app

#1.0
def somar(): # função do botão1
    somar1 = float(primeiron.get()) # primeiron faz referencia a primeira entrada
    somar2 = float(segundon.get()) # primeiron faz referencia a segunda entrada

    somar3 = somar1 + somar2
    labelresult = Label(myCal,text='%.2f' %(somar3)).grid(row=9, column=0)
def dividir(): # função do botão2
    dividir1 = float(primeiron.get())
    dividir2 = float(segundon.get())
    dividir3 = dividir1 / dividir2
    labelresult = Label(myCal,text='%.2f' %(dividir3)).grid(row=9, column=0)
def multiplicar(): # função do botão3
    multiplicar1 = float(primeiron.get())
    multiplicar2 = float(segundon.get())
    multiplicar3 = multiplicar1 * multiplicar2
    labelresult = Label(myCal,text='%.2f' %(multiplicar3)).grid(row=9, column=0)
def fatorar(): # função do botão4
    fatorar1 = float(primeiron.get())
    fatorar2 = float(segundon.get())
    fatorar3 = fatorar1**fatorar2
    labelresul = Label(myCal,text='%.2f' %(fatorar3)).grid(row=9, column=0)
def percentagem(): # função do botão5
    percentagem1 = float(primeiron.get())
    percentagem2 = float(segundon.get())
    percentagem3 = percentagem1 % percentagem2
    labelresult = Label(myCal,text='%.2f' %(percentagem3)).grid(row=9, column=0)
   

#4.1
myCal.geometry('100x250+300+300') # dimensao da app
myCal.title('myCal_1.0') # titulo da app
#2.0
botao1 = Button(myCal,text='Somar', command=somar).grid(row=1, column=0) # botões
botao2 = Button(myCal,text='Dividir', command=dividir).grid(row=2, column=0)
botao3 = Button(myCal,text='Multiplicar', command=multiplicar).grid(row=3, column=0)
botao4 = Button(myCal,text='Fatorar', command=fatorar).grid(row=4, column=0)
botao5 = Button(myCal,text='Percentagem', command=percentagem).grid(row=5, column=0)
#4.1
primeiron = StringVar() #difinisão da variavel primeiron
segundon  = StringVar() #definição da variavel segundon
#3.0
entrada1 = Entry(myCal,textvariable=primeiron).grid(row=6, column=0) # comando de entrada
entrada2 = Entry(myCal,textvariable=segundon).grid(row=7, column=0) # comando de entrada

#botao = Button(myCal,text='Calcular' command=calculadora).grid(row=8, column=0)

#4.1
myCal.mainloop() # fechamento da app

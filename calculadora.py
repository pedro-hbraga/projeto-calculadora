from tkinter import *
import math

quadro = Tk()
quadro.title("Calculadora")
quadro.geometry("250x250")

visor = Entry(quadro, width=33, font=("Times New Roman", 15))
visor.place(relx=0.01, rely=0.1)

def InserirNum(valor):
    visor.insert(END, valor)

def raiz():
    valor = float(visor.get())
    v = math.sqrt(valor)
    visor.delete(0, END)
    visor.insert(END, str(v))

def seno():
    valor = float(visor.get())
    Sen = math.sin(valor)
    visor.delete(0, END)
    visor.insert(END, str(Sen))

def cossseno():
    valor = float(visor.get())
    Cos = math.cos(valor)
    visor.delete(0, END)
    visor.insert(END, str(Cos))

def tangente():
    valor = float(visor.get())
    Tg = math.tan(valor)
    visor.delete(0, END)
    visor.insert(END, str(Tg))

def logaritmo():
    valor = float(visor.get())
    Lg = math.log(valor)
    visor.delete(0, END)
    visor.insert(END, str(Lg))

def C():
    visor.delete(0, END)

#def calcular():
 #   valor = eval(visor.get()))
    #calculo = eval(valor)
  #  visor.insert(END," = " + str(valor))
def soma(x, y):
    resultado = x + y
    return resultado

def subtrair(x, y):
    resultado = x - y
    return resultado

def dividir(x, y):
    resultado = x / y
    return resultado

def multiplicar(x, y):
    resultado = x * y
    return resultado

def potencia(x, y):
    resultado = x ** y
    return resultado

def calcular():
    
    valores = visor.get()
    listaVal = valores.split()
    indice = 0
    sinais = ["+", "-", "/","*"]
    
    while True:
        #print(len(listaVal))
        #print(indice)
        for ind, val in enumerate(listaVal):
            if val == "**":
                resultado = potencia(float(listaVal[(ind - 1)]), float(listaVal[(ind + 1)]))
                del listaVal[(ind - 1):(ind + 2)]
                listaVal.insert((ind - 1), resultado)

        for i, v in enumerate(listaVal):
            if v == "/":
                resultado = dividir(float(listaVal[(i - 1)]), float(listaVal[(i + 1)]))
                del listaVal[(i-1):(i+2)]
                listaVal.insert((i - 1), resultado)
            
            if v == "*":
                resultado = multiplicar(float(listaVal[(i - 1)]), float(listaVal[(i + 1)]))
                del listaVal[(i - 1): (i + 2)]
                listaVal.insert((i - 1), resultado)

        if len(listaVal) == 1:
            break

        if listaVal[indice] == "+":
            #print('Entrou no if')
            resultado = soma(float(listaVal[indice-1]), float(listaVal[indice+1]))
            del listaVal[(indice-1):(indice+2)]
            indice = 0
            listaVal.insert(indice, resultado)
            

        elif listaVal[indice] == "-":
            resultado = subtrair(float(listaVal[indice-1]), float(listaVal[indice+1]))
            del listaVal[(indice-1):(indice+2)]
            indice = 0
            listaVal.insert(indice, resultado)
            

        else:
            indice = indice + 1

    visor.delete(0, END)
    visor.insert(END, str(listaVal[0]))
   

#COLUNA 1
bot7 = Button(quadro, width=2, text="7", font=(10), command=lambda: InserirNum(7))
bot7.place(relx=0.03, rely=0.25)

bot4 = Button(quadro, width=2, text="4", font=(10), command=lambda: InserirNum(4))
bot4.place(relx=0.03, rely=0.4)

bot1 = Button(quadro, width=2, text="1", font=(10), command=lambda: InserirNum(1))
bot1.place(relx=0.03, rely=0.55)

botResultado = Button(quadro, width=2, text="=", font=(10), command=calcular)
botResultado.place(relx=0.03, rely=0.7)

# COLUNA 2
bot8 = Button(quadro, width=2, text="8", font=(10), command=lambda: InserirNum(8))
bot8.place(relx=0.18, rely=0.25)

bot5 = Button(quadro, width=2, text="5", font=(10), command=lambda: InserirNum(5))
bot5.place(relx=0.18, rely=0.4)

bot2 = Button(quadro, width=2, text="2", font=(10), command=lambda: InserirNum(2))
bot2.place(relx=0.18, rely=0.55)

bot0 = Button(quadro, width=2, text="0", font=(10), command=lambda: InserirNum(0))
bot0.place(relx=0.18, rely=0.7)

# COLUNA 3

bot9 = Button(quadro, width=2, text="9", font=(10), command=lambda: InserirNum(9))
bot9.place(relx=0.33, rely=0.25)

bot6 = Button(quadro, width=2, text="6", font=(10), command=lambda: InserirNum(6))
bot6.place(relx=0.33, rely=0.4)

bot3 = Button(quadro, width=2, text="3", font=(10), command=lambda: InserirNum(3))
bot3.place(relx=0.33, rely=0.55)

# COLUNA 4
botSoma = Button(quadro, width=2, text="+", font=(10),command=lambda: InserirNum(" + "))
botSoma.place(relx=0.48, rely=0.25)

botSubt = Button(quadro, width=2, text="-", font=(10), command=lambda: InserirNum(" - "))
botSubt.place(relx=0.48, rely=0.4)

botMult = Button(quadro, width=2, text="x", font=(10), command=lambda: InserirNum(" * "))
botMult.place(relx=0.48, rely=0.55)

botDiv = Button(quadro, width=2, text="/", font=(10), command=lambda: InserirNum(" / "))
botDiv.place(relx=0.48, rely=0.7)

# COLUNA 5
botReseta = Button(quadro,width=8, text="C", font=(10), command=C)
botReseta.place(relx=0.63, rely=0.25)

botSen = Button(quadro, width=3, text="sen", font=(10), command=seno)
botSen.place(relx=0.63, rely=0.4)

botTan = Button(quadro, width=3, text="tan", font=(10),command=tangente)
botTan.place(relx=0.63, rely=0.55)

botExp = Button(quadro, width=3, text="^", font=(10), command=lambda: InserirNum(" ** "))
botExp.place(relx=0.63, rely=0.7)

# COLUNA 6

botCos = Button(quadro, width=3, text="cos", font=(10), command=cossseno)
botCos.place(relx=0.8, rely=0.4)

botLog = Button(quadro, width=3, text="log", font=(10), command=logaritmo)
botLog.place(relx=0.8, rely=0.55)

botRaiz = Button(quadro, width=3, text="√", font=(10), command=raiz)
botRaiz.place(relx=0.8, rely=0.7)

quadro.mainloop()
from tkinter import Button
from tkinter import Label
from tkinter import Tk
from tkinter import Entry
from time import sleep
#from tkinter import
def Calcular():
    resultado['text'] = 'Calculando...'
    resultado['text'] = ent.get()
    resultado['fg'] = 'green'

i = Tk()
i.title('Brincando com Python')
i.geometry('400x300')
texto = Label(i, text='Calculadora para Estatística')
texto.pack()

ent = Entry(i)
ent.pack()

calc = Button(i, text='Calcule', command=Calcular)
calc.pack()

resultado = Label(i, text='Resultado')
resultado.pack()

i.mainloop()
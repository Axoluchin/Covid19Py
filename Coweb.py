import requests
from bs4 import BeautifulSoup
import time
from time import strftime 
from tkinter import *
import matplotlib.pyplot as plt

def tiempo():
    string = strftime('%d/%m/%y\n%H:%M:%S %p') 

    lReloj.config(text = string) 
    lReloj.after(1000, tiempo) 

def Actualizacion():
    res = ('https://www.worldometers.info/coronavirus/')
    soup = requests.get(res)
    s= BeautifulSoup(soup.text,"html.parser")
    data = s.find_all("div",class_="maincounter-number")

    Casos.config(text = f"Casos: {data[0].text.strip()}")
    Muertos.config(text = f"Muertes: {data[1].text.strip()}") 
    Recuperados.config(text = f"Recuperados: {data[2].text.strip()}")
    Grafica()
    Muertos.after(10, Actualizacion) 

def Grafica():
    res = ('https://www.worldometers.info/coronavirus/')
    soup = requests.get(res)
    s= BeautifulSoup(soup.text,"html.parser")
    data = s.find_all("div",class_="maincounter-number")

    Numero = [(data[0].text.strip()),(data[1].text.strip()),(data[2].text.strip())]
    
    Numero[0] = Numero[0].replace(",","")
    Numero[0] = int(Numero[0])
    Numero[1] = Numero[1].replace(",","")
    Numero[1] = int(Numero[1])
    Numero[2] = Numero[2].replace(",","")
    Numero[2] = int(Numero[2])

    percent = Numero
    colour = ['blue','green','red']
    label = [f"Casos\n{data[0].text.strip()}",f"Muertes\n{data[1].text.strip()}",f"Recuperados\n{data[2].text.strip()}"]
    plt.pie(percent,labels=label,colors=colour)
    plt.show()

Color = "#2f89fc"
Texto = ("time",15,"bold")


win = Tk()
win.configure(bg=Color)
win.resizable(0,0)
win.title('Covid19')

Datos = LabelFrame(win,text="Datos:",font=("time",20,"bold"),foreground = '#f5f5f5',bg=Color,bd=5)
Datos.grid(row=0,column=0)

Casos = Label(Datos,text="Casos:",font = Texto,bg=Color,fg="#f5f5f5")
Casos.grid(row=0,column=0)

Muertos = Label(Datos,text="Muertes:",font = Texto,bg=Color,fg="#f5f5f5")
Muertos.grid(row=1,column=0)

Recuperados = Label(Datos,text="Recuperados:",font = Texto,bg=Color,fg="#f5f5f5")
Recuperados.grid(row=2,column=0)

Tiempo = LabelFrame(win,text="Tiempo",font=("time",20,"bold"),foreground = '#f5f5f5',bg=Color,bd=5)
Tiempo.grid(row=0,column=1)

lReloj = Label(Tiempo, font = ('calibri', 26, 'bold'),foreground = '#f5f5f5',bg=Color)           
lReloj.grid(row=1,column=0)

tiempo()
Grafica()
Actualizacion()
win.mainloop()
from tkinter import *
import cv2 as cv
from PIL import *
from PIL import Image

ventana=Tk()
ventana.title("Prueba")
ventana.geometry("500x500")
filename="Tiger.png"
eleccion1=Image.open(filename)

def color(evento):
    for x in range(eleccion1.size[0]):
        for y in range(eleccion1.size[1]):
            r,g,b=eleccion1.getpixel((x,y))
            eleccion1.putpixel((x,y),(r,0,b))

    eleccion1.show()

def colordes(evento1):
    for x in range(eleccion1.size[0]):
        for y in range(eleccion1.size[1]):
            r,g,b=eleccion1.getpixel((x,y))
            eleccion1.putpixel((x,y),(b,r,g))


    eleccion1.show()

eleccion=PhotoImage(file="Tiger.png")
my_label= Label(ventana,image=eleccion)
my_label.pack(pady=20)

my_label.bind(f"<Button-1>",color)
#my_label.bind("<Enter>",colordes)
ventana.mainloop()
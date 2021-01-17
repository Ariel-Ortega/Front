# Medicamentos

import tkinter
from tkinter import messagebox
from tkinter import *
import time
from PIL import ImageTk

def Medicamentos():
    # Creación de la ventana en tamaño completo
    ventanaMed = tkinter.Tk()
    ventanaMed.title("Medicamentos")  # Título de la ventana
    ancho_valor = ventanaMed.winfo_screenwidth()  # Creo una variable que determine el ancho del monitor
    altura_valor = ventanaMed.winfo_screenheight()  # Creo una variable que determine el alto del monitor
    ventanaMed.geometry("%dx%d+0+0" % (ancho_valor, altura_valor))  # Paso como valor en ancho y alto al método "geometry"
    ventanaMed.config(bg="#0c3a56")

    # Título que aparecerá en la ventana
    etiqueta = tkinter.Label(ventanaMed, text="Medicamentos")
    etiqueta.pack()
    etiqueta.config(font=("Arial", 30, "bold"), fg="white", bg="#0c3a56")

    #Imagen de fondo
    fondo = ImageTk.PhotoImage(file="BMedicamentos.jpg")
    lblFondo = Label(ventanaMed, image=fondo)
    lblFondo.place(x=0, y=0, relwidth=1, relheight=1.3)

    # TABLA DE MEDICAMENTOS
    # Marco para colocar la tabla
    marco_tablaH = Frame(bg="#0c3a56")
    marco_tablaH.place(x=400, y=150, width=550, height=250)  # Posición en x, posición en y, ancho, alto

    Label(marco_tablaH, text="ID", relief=RAISED, font=("Comic Sans MS", 11), bg="light gray", width=1, height=1).grid(
        row=0, column=0, sticky=NSEW)
    Label(marco_tablaH, text="Medicamento", relief=RAISED, font=("Comic Sans MS", 11), bg="light gray", width=42,
          height=1).grid(row=0, column=1, sticky=NSEW)

    for i in range(10):
        for j in range(2):
            l = Entry(marco_tablaH, text='', relief=GROOVE, font=("Comic Sans MS", 10), state=DISABLED).grid(row=i + 2, column=j, sticky=NSEW)
        # HORA Y FECHA
    clock_frame = LabelFrame(bg="#0c3a56", relief=FLAT)  # Marco que contendrá la fecha y hora
    clock_frame.place(x=1100, y=15, width=200, height=60)

    photo_frame = LabelFrame(bg="#0c3a56", relief=FLAT)  # Marco que contendrá la foto
    photo_frame.place(x=1100, y=75, width=200, height=120)

    def update_clock():  # Función que actualiza la hora
        tiempo_actual = tkinter.Label(clock_frame, text=time.strftime('%H:%M:%S'), font=("Calibri light", 14),
                                      fg="white", bg="#0c3a56")
        tiempo_actual.place(x=60, y=30)
        tiempo_ahora = time.strftime('%H:%M:%S')
        if tiempo_actual['text'] != tiempo_ahora:
            tiempo_actual = tiempo_ahora
        ventanaMed.after(1000, update_clock)

    update_clock()

    def update_date():  # Función que actualiza la fecha
        fecha_actual = tkinter.Label(clock_frame, text=time.strftime('%d/%m/%Y'), font=("Calibri light", 14),
                                     fg="white", bg="#0c3a56")
        fecha_actual.place(x=50, y=0)
        fecha_ahora = time.strftime('%d/%m/%Y')
        if fecha_actual['text'] != fecha_ahora:
            fecha_actual = fecha_ahora
        ventanaMed.after(1000, update_date)

    update_date()

    # Marcos para colocar los botones Agregar, Modificar, Eliminar, Salir
    marco_botonesMed = Frame(bg="#0c3a56")
    marco_botonesMed.place(x=10, y=40, width=300, height=615)

    marco_botonSalirM = Frame(bg="white")
    marco_botonSalirM.place(x=1080, y=570, width=190, height=80)

    # Creación de los botones

    boton_agregarM = Button(marco_botonesMed, text="Agregar", fg="white", bg="grey", font=("Monospaced", 15), activeforeground="grey", cursor="hand2")
    boton_agregarM.place(x=100, y=50, width=100, height=40)

    boton_modificarM = Button(marco_botonesMed, text="Modificar", fg="white", bg="grey", font=("Monospaced", 15),
                             activeforeground="grey", cursor="hand2")
    boton_modificarM.place(x=100, y=250, width=100, height=40)

    boton_eliminarM = Button(marco_botonesMed, text="Eliminar", fg="white", bg="grey", font=("Monospaced", 15),
                            activeforeground="grey", cursor="hand2")
    boton_eliminarM.place(x=100, y=450, width=100, height=40)

    boton_salirM = Button(marco_botonSalirM, text="Salir", fg="white", bg="grey", font=("Monospaced", 15),
                           activeforeground="grey", cursor="hand2")
    boton_salirM.place(x=80, y=30, width=100, height=40)

    ventanaMed.mainloop()

Medicamentos()
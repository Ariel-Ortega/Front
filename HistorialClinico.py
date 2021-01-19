#Historial clínico

import tkinter
from tkinter import messagebox
from tkinter import *
import time

def HistorialClinico():
    # Creación de la ventana en tamaño completo
    ventanaHC = tkinter.Toplevel()
    ventanaHC.title("Historial Clínico")  # Título de la ventana
    ancho_valor = ventanaHC.winfo_screenwidth()  # Creo una variable que determine el ancho del monitor
    altura_valor = ventanaHC.winfo_screenheight()  # Creo una variable que determine el alto del monitor
    ventanaHC.geometry("%dx%d+0+0" % (ancho_valor, altura_valor))  # Paso como valor en ancho y alto al método "geometry"
    ventanaHC.config(bg="#0c3a56")

    # Título que aparecerá en la ventana
    etiqueta = Label(ventanaHC, text="Historial Clínico")
    etiqueta.pack()
    etiqueta.config(font=("Arial", 30, "bold"), fg="white", bg="#0c3a56")

    # TABLA DEL HISTORIAL CLÍNICO
    #Marco para colocar la tabla
    marco_tablaH = Frame(ventanaHC, bg="#0c3a56")
    marco_tablaH.place(x=400, y=150, width=550, height=250)# Posición en x, posición en y, ancho, alto

    Label(marco_tablaH, text="ID", relief=RAISED, font=("Comic Sans MS", 11), bg="light gray", width=1, height=1).grid(row=0, column=0, sticky=NSEW)
    Label(marco_tablaH, text="Nombre", relief=RAISED, font=("Comic Sans MS", 11), bg="light gray", width=42, height=1).grid(row=0, column=1, sticky=NSEW)

    for i in range(10):
        for j in range(2):
            l = Entry(marco_tablaH, text='', relief=GROOVE, font=("Comic Sans MS", 10), state=DISABLED).grid(row=i + 2, column=j, sticky=NSEW)

    # HORA Y FECHA
    clock_frame = LabelFrame(ventanaHC, bg="#0c3a56", relief=FLAT)# Marco que contendrá la fecha y hora
    clock_frame.place(x=1100, y=15, width=200, height=60)

    photo_frame = LabelFrame(ventanaHC, bg="#0c3a56", relief=FLAT)# Marco que contendrá la foto
    photo_frame.place(x=1100, y=75, width=200, height=120)

    def update_clock():# Función que actualiza la hora
        tiempo_actual = tkinter.Label(clock_frame, text=time.strftime('%H:%M:%S'), font=("Calibri light", 14), fg="white", bg="#0c3a56")
        tiempo_actual.place(x=60, y=30)
        tiempo_ahora = time.strftime('%H:%M:%S')
        if tiempo_actual['text'] != tiempo_ahora:
            tiempo_actual = tiempo_ahora
        ventanaHC.after(1000, update_clock)
    update_clock()

    def update_date():# Función que actualiza la fecha
        fecha_actual = tkinter.Label(clock_frame, text=time.strftime('%d/%m/%Y'), font=("Calibri light", 14), fg="white", bg="#0c3a56")
        fecha_actual.place(x=50, y=0)
        fecha_ahora = time.strftime('%d/%m/%Y')
        if fecha_actual['text'] != fecha_ahora:
            fecha_actual = fecha_ahora
        ventanaHC.after(1000, update_date)
    update_date()

    # Marcos para colocar los botones Agregar, Modificar, Eliminar, Salir
    marco_botonesHC = Frame(ventanaHC, bg="#0c3a56")
    marco_botonesHC.place(x=10, y=40, width=300, height=615)

    marco_botonSalir = Frame(ventanaHC, bg="#0c3a56")
    marco_botonSalir.place(x=1080, y=570, width=250, height=100)

    def AbrirV_Expedientes():
        ventanaHC.withdraw()
        import Expediente as Exte
        Exte.Expediente()

    def SlirV_HC():
        ventanaHC.withdraw()
        import Citas as Cit
        Cit.firstwindow('user')

    # Creación de los botones

    boton_agregarHC = Button(marco_botonesHC, command=AbrirV_Expedientes, text="Agregar", fg="white", bg="grey", font=("Monospaced", 15), activeforeground="grey",
                           cursor="hand2")
    boton_agregarHC.place(x=100, y=50, width=100, height=40)

    boton_modificarHC = Button(marco_botonesHC, text="Modificar", fg="white", bg="grey", font=("Monospaced", 15), activeforeground="grey", cursor="hand2")
    boton_modificarHC.place(x=100, y=250, width=100, height=40)

    boton_eliminarHC = Button(marco_botonesHC, text="Eliminar", fg="white", bg="grey", font=("Monospaced", 15), activeforeground="grey", cursor="hand2")
    boton_eliminarHC.place(x=100, y=450, width=100, height=40)

    boton_salirHC = Button(marco_botonSalir, command=SlirV_HC, text="Salir", fg="white", bg="grey", font=("Monospaced", 15), activeforeground="grey", cursor="hand2")
    boton_salirHC.place(x=80, y=30, width=100, height=40)

    ventanaHC.mainloop()

#HistorialClinico()
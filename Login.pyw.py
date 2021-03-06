import tkinter
from tkinter import messagebox
from tkinter import *
from PIL import ImageTk
import Citas

#Falta validar campos con el tipo de dato
ventana = tkinter.Tk()
ventana.title("Administrador Consultorio")
ventana.geometry("1199x600+100+50")
ventana.resizable(0,0)

# Imagen Fondo
fondo = ImageTk.PhotoImage(file="LG.jpg")
lblFondo = Label(ventana, image=fondo)
lblFondo.place(x=0, y=0, relwidth=1.5, relheight=1)

# Marco Log in
marco_Log = Frame(bg="white")
marco_Log.place(x=800, y=40, width=340, height=500)

title = Label(marco_Log, text="Iniciar\nSesión", font=("Courier", 30, "bold"), fg="grey", bg="white")
title.place(x=70, y=30)

desc = Label(marco_Log, text="Cuenta Empleado", font=("Helvetica", 11, "bold"), fg="grey", bg="white")
desc.place(x=90, y=140)

lbl_usuario = Label(marco_Log, text="Usuario", font=("Century Gothic", 15, "bold"), fg="black", bg="white")
lbl_usuario.place(x=40, y=210)

cajaTexto1 = tkinter.Entry(marco_Log, font=("Calibri light", 15), bg="light blue")
cajaTexto1.place(x=40, y=250, width=260, height=35)

lbl_contraseña = Label(marco_Log, text="Contraseña", font=("Century Gothic", 15, "bold"), fg="black", bg="white")
lbl_contraseña.place(x=40, y=310)

cajaTexto2 = tkinter.Entry(marco_Log, font=("Calibri light", 15), bg="light blue", show="*")
cajaTexto2.place(x=40, y=350, width=260, height=35)

def insesion():
    C1 = cajaTexto1.get()
    C2 = cajaTexto2.get()
    print(C1)
    print(C2)

    if (cajaTexto1.get()=="" or cajaTexto2.get()=="" ):
        messagebox.showerror("¡Error!", "Llene todos los campos requeridos")
    elif (cajaTexto1.get()=="ABCDEF" and cajaTexto2.get()=="12345" ):
        messagebox.showinfo("¡Bienvenido!", cajaTexto1.get())
        ventana.destroy()
        Citas.firstwindow(C1)

    else:
        messagebox.showerror("¡Error!", "Datos no válidos")

boton1 = tkinter.Button(text="Entrar", command=insesion,fg="white", bg="grey", font=("Monospaced", 15), activeforeground="grey", cursor="hand2")
boton1.place(x=940, y=520)

boton2 = tkinter.Button(text="Regístrarse", fg="white", bg="grey", font=("Monospaced", 15), activeforeground="grey", cursor="hand2")
boton2.place(x=940, y=510)

ventana.mainloop()

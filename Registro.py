# Registro de ususario

import tkinter
from tkinter import messagebox
from tkinter import *
from tkinter import ttk
from PIL import ImageTk
import User

persona = User.User()# Objeto de tipo de persona

def RegistroUsuario():
    # Creación de la ventana en tamaño completo
    ventanaReg = tkinter.Toplevel()
    ventanaReg.title("Registro de Usuario")  # Título de la ventana
    ventanaReg.geometry("800x600+280+50")  # Paso como valor en ancho y alto al método "geometry"
    ventanaReg.config(bg="#0c3a56")
    ventanaReg.resizable(0, 0)

    # Marco para el Registro
    marco_R = Frame(ventanaReg, bg="light grey")
    marco_R.place(x=160, y=80, width=480, height=380)

    # Etiquetas
    etiqueta_TipoUsuario = Label(marco_R, text="Tipo de usuario", font=("Calibri light", 14, "bold"), fg="black", bg="light gray")
    etiqueta_TipoUsuario.place(x=70, y=30)

    etiqueta_Password = Label(marco_R, text="Nombre de usuario", font=("Calibri light", 14, "bold"), fg="black", bg="light gray")
    etiqueta_Password.place(x=70, y=120)

    etiqueta_Nombre = Label(marco_R, text="Contraseña", font=("Calibri light", 14, "bold"), fg="black",  bg="light gray")
    etiqueta_Nombre.place(x=70, y=210)

    def R_Datos(Nombre, Password, User):
        # Campos de texto
        combo_TipoUsuario = ttk.Combobox(ventanaReg, state="readonly")
        combo_TipoUsuario.place(x=230, y=150, width=350, height=35)
        combo_TipoUsuario['values']=('root', 'admin', 'assistent')

        cajaTexto_Password = tkinter.Entry(marco_R, font=("Calibri light", 13), bg="white")
        cajaTexto_Password.place(x=70, y=157, width=350, height=35)

        cajaTexto_Nombre = tkinter.Entry(marco_R, font=("Calibri light", 13), bg="white")
        cajaTexto_Nombre.place(x=70, y=247, width=350, height=35)

        Nombre = cajaTexto_Nombre.get()
        Password = cajaTexto_Password.get()
        TipoU = combo_TipoUsuario.get()

        persona.CreateUser(Nombre, Password, TipoU)


    boton_Reg = tkinter.Button(ventanaReg, text="Regístrarse", fg="white", bg="#722f37", font=("Monospaced", 12), activeforeground="grey", cursor="hand2", relief="flat", overrelief="flat")
    boton_Reg.place(x=350, y=490)

    ventanaReg.mainloop()

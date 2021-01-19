# CITAS
import tkinter
from tkinter import *
import time

#def able_date():


#def Add_date():

   # cajaTexto1.insert(0, "@nombre")


class firstwindow():
    def __init__(self,user):

        # Creación de la ventana en tamaño completo
        root = tkinter.Tk()
        root.title("Mi consultorio virtual")  # Título de la ventana
        ancho_valor = root.winfo_screenwidth()  # Creo una variable que determine el ancho del monitor
        altura_valor = root.winfo_screenheight()  # Creo una variable que determine el alto del monitor
        root.geometry("%dx%d+0+0" % (ancho_valor, altura_valor))  # Paso como valor en ancho y alto al método "geometry"
        root.config(bd=15, bg="#53CDB8")

        # ------FRAMES-----

        title_frame = LabelFrame(root, bg="#53CDB8", relief=FLAT)
        title_frame.place(x=650, y=10, width=130, height=65)

        buttons1_frame = LabelFrame(root, bg="#53CDB8")
        buttons1_frame.place(x=250, y=200, width=178, height=220)

        tableau_frame = LabelFrame(root, bg="#53CDB8", relief=FLAT)
        tableau_frame.place(x=470, y=200, width=500, height=500)

        buttons2_frame = LabelFrame(root, bg="#53CDB8")
        buttons2_frame.place(x=455, y=420, width=525, height=43)

        clock_frame = LabelFrame(bg="#53CDB8", relief=FLAT)  # Marco que contendrá la fecha y hora
        clock_frame.place(x=1100, y=15, width=200, height=110)

        photo_frame = LabelFrame(bg="#53CDB8", relief=FLAT)  # Marco que contendrá la foto
        photo_frame.place(x=1100, y=125, width=200, height=120)

        def AbrirV_HC():
            root.withdraw()
            import HistorialClinico as HistC
            HistC.HistorialClinico()
        def AbrirV_Medc():
            root.withdraw()
            import Medicamentos as Medcms
            Medcms.Medicamentos()
        def AbrirV_Rec():
            root.withdraw()
            import Receta as R
            R.Receta()
        def Dat():
            import Dates
        def CerrarV():
            root.withdraw()

        # -----WIDGETS------
        Label(title_frame, text='CITAS', bg="#53CDB8", font=("Arial", 30, "bold")).grid(row=0, column=0)

        expedientes_button = Button(buttons1_frame, text='Historiales Clínicos', width=20, command=AbrirV_HC)
        expedientes_button.configure(bg="light pink", cursor='hand2', font=("Arial", "10", "normal"))
        expedientes_button.grid(row=0, column=0, padx=2, pady=3, sticky=W + E)

        Label(buttons1_frame, bg="#53CDB8").grid(row=2, column=0)

        medicine_button = Button(buttons1_frame, text='Medicamentos', width=20, command=AbrirV_Medc)
        medicine_button.configure(bg="light pink", cursor='hand2', font=("Arial", "10", "normal"))
        medicine_button.grid(row=3, column=0, padx=2, pady=3, sticky=W + E)

        Label(buttons1_frame, bg="#53CDB8").grid(row=4, column=0)

        prescription_button = Button(buttons1_frame, text='Recetar', width=20, command=AbrirV_Rec)
        prescription_button.configure(bg="light pink", cursor='hand2', font=("Arial", "10", "normal"))
        prescription_button.grid(row=5, column=0, padx=2, pady=3, sticky=W + E)

        Label(buttons1_frame, bg="#53CDB8").grid(row=6, column=0)

        users_button = Button(buttons1_frame, text='Usuarios', width=20, command=Dat)
        users_button.configure(bg="light pink", cursor='hand2', font=("Arial", "10", "normal"))
        users_button.grid(row=7, column=0, padx=2, pady=3, sticky=W + E)

        # ------TABLA DE CITAS------
        Label(tableau_frame, text="Paciente", relief=RAISED, font=("Arial", 11), bg="light gray").grid(row=0, column=0, sticky=NSEW)
        Label(tableau_frame, text="Fecha", relief=RAISED, font=("Arial", 11), bg="light gray").grid(row=0, column=1, sticky=NSEW)
        Label(tableau_frame, text="Hora", relief=RAISED, font=("Arial", 11), bg="light gray").grid(row=0, column=2, sticky=NSEW)

        for i in range(8):
            for j in range(3):
                l = Entry(tableau_frame, text='', relief=GROOVE, font=("Arial", 10), state=DISABLED).grid(row=i + 2, column=j, sticky=NSEW)

        # ------Foto/Fecha y hora------
            # HORA Y FECHA


        usuario = tkinter.Label(clock_frame, text=user, font=("Calibri light", 14), fg="black", bg="#53CDB8")
        usuario.place(x=50, y=5, width=100, height=20)

        def update_clock():  # Función que actualiza la hora
            tiempo_actual = tkinter.Label(clock_frame, text=time.strftime('%H:%M:%S'), font=("Calibri light", 14), fg="black", bg="#53CDB8")
            tiempo_actual.place(x=60, y=60)
            tiempo_ahora = time.strftime('%H:%M:%S')
            if tiempo_actual['text'] != tiempo_ahora:
                tiempo_actual = tiempo_ahora
            root.after(1000, update_clock)

        update_clock()

        def update_date():  # Función que actualiza la fecha
            fecha_actual = tkinter.Label(clock_frame, text=time.strftime('%d/%m/%Y'), font=("Calibri light", 14), fg="black", bg="#53CDB8")
            fecha_actual.place(x=50, y=30)
            fecha_ahora = time.strftime('%d/%m/%Y')
            if fecha_actual['text'] != fecha_ahora:
                fecha_actual = fecha_ahora
            root.after(1000, update_date)

        update_date()

        # ---botones add_date, delete_date, exit---
        add_date_button = Button(buttons2_frame, text='Agregar cita', width=20)
        add_date_button.configure(bg="light pink", cursor='hand2', font=("Arial", "10", "normal"))
        add_date_button.grid(row=0, column=0, padx=2, pady=3, sticky=W + E)

        delete_date_button = Button(buttons2_frame, text='Eliminar cita', width=20)
        delete_date_button.configure(bg="light pink", cursor='hand2', font=("Arial", "10", "normal"))
        delete_date_button.grid(row=0, column=1, padx=2, pady=3, sticky=W + E)

        exit_button = Button(buttons2_frame, command=CerrarV, text='Salir', width=20)
        exit_button.configure(bg="light pink", cursor='hand2', font=("Arial", "10", "normal"))
        exit_button.grid(row=0, column=2, padx=2, pady=3, sticky=W + E)


        root.mainloop()

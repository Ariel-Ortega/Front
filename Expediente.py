# Expediente
import tkinter
from tkinter import ttk
from tkinter import messagebox
from tkinter import *
import time

#Falta validar campos con el tipo de dato
def Expediente():
    #Creación de la ventana en tamaño completo
    ventanaEx = tkinter.Tk()
    ventanaEx.title("Expedientes") # Título de la ventana
    ancho_valor = ventanaEx.winfo_screenwidth()# Creo una variable que determine el ancho del monitor
    altura_valor = ventanaEx.winfo_screenheight()# Creo una variable que determine el alto del monitor
    ventanaEx.geometry("%dx%d+0+0"%(ancho_valor, altura_valor))# Paso como valor en ancho y alto al métod "geometry"
    ventanaEx.config(bg="#0c3a56")

    # Título que aparecerá en la ventana
    etiqueta = tkinter.Label(ventanaEx, text="Expediente")
    etiqueta.pack()
    etiqueta.config(font=("Arial", 30, "bold"), fg="white",  bg="#0c3a56")

    #Creación del marco que contendrá al scroll
    a1 = LabelFrame(ventanaEx)

    v2_canvas = Canvas(a1)
    v2_canvas.place(x=0, y=0, width=900, height=650)
    v2_canvas.config(bg="#0c3a56")

    yscrollbar = ttk.Scrollbar(a1, orient="vertical", command=v2_canvas.yview)
    yscrollbar.pack(side=RIGHT, fill="y")

    v2_canvas.configure(yscrollcommand=yscrollbar.set)
    v2_canvas.bind('<Configure>', lambda e: v2_canvas.configure(scrollregion=v2_canvas.bbox('all')))

    a1.pack(fill="both", expand="yes", padx=5, pady=5)
    a1.config(bg="#0c3a56")

    # Creación de los diferentes campos
    # Lista con el nombre de los distintos campos a llenar
    variable = ['Nombre', 'Edad', 'Sexo', 'Ocupación', 'Fecha de nacimiento', 'Peso', 'Estatura',
                'Número de teléfono', 'E-mail', 'Escolaridad', 'Antecedentes heredofamiliares',
                'Antecedentes patológicos', 'Antecedentes ginecoobstétricos', 'Padecimiento actual',
                'Síntomas generales', 'Aparatos y sistemas', 'Signos vitales', 'Exploración física general',
                'Exploración física general']

    for i in range(19):
        mi = Frame(v2_canvas, bg="#0c3a56")  # Primer Marco para la lista donde se colocarán Nombre, Edad...
        v2_canvas.create_window((0, i * 60), window=mi, anchor="nw")

        etiquetas = tkinter.Label(mi, text=variable[i], font=("Arial", 15), justify="left", fg="white", bg="#0c3a56")  # Etiqueta
        etiquetas.pack(side='left', fill='both', expand="yes", padx=35, pady=12)

    # Segundo Marco (ni) donde se crearán cada una de las cajas de texto o campos
    # Campo 1 Nombre
    n1 = Frame(v2_canvas, bg="#0c3a56")
    v2_canvas.create_window((320, 0), window=n1, anchor="nw", width=550)

    c_Nombre = tkinter.Entry(n1, font=("Calibri light", 12, "italic"), bg="light grey")
    c_Nombre.pack(side='right', fill='both', expand="yes", padx=90, pady=15, ipadx=100, ipady=5)

    # Campo 2 Edad
    n2 = Frame(v2_canvas, bg="#0c3a56")
    v2_canvas.create_window((320, 60), window=n2, anchor="nw", width=550)

    c_Edad = tkinter.Entry(n2, font=("Calibri light", 12, "italic"), bg="light grey")
    c_Edad.pack(side='right', fill='both', expand="yes", padx=90, pady=15, ipadx=100, ipady=5)

    # Campo 3 Sexo
    n3 = Frame(v2_canvas, bg="#0c3a56")
    v2_canvas.create_window((320, 120), window=n3, anchor="nw", width=550)

    c_Sexo = tkinter.Entry(n3, font=("Calibri light", 12, "italic"), bg="light grey")
    c_Sexo.pack(side='right', fill='both', expand="yes", padx=90, pady=15, ipadx=100, ipady=5)

    # Campo 4 Ocupación
    n4 = Frame(v2_canvas, bg="#0c3a56")
    v2_canvas.create_window((320, 180), window=n4, anchor="nw", width=550)

    c_Ocupacion = tkinter.Entry(n4, font=("Calibri light", 12, "italic"), bg="light grey")
    c_Ocupacion.pack(side='right', fill='both', expand="yes", padx=90, pady=15, ipadx=100, ipady=5)

    # Campo 5 Fecha de nacimiento
    n5 = Frame(v2_canvas, bg="#0c3a56")
    v2_canvas.create_window((320, 240), window=n5, anchor="nw", width=550)

    c_FNacim = tkinter.Entry(n5, font=("Calibri light", 12, "italic"), bg="light grey")
    c_FNacim.pack(side='right', fill='both', expand="yes", padx=90, pady=15, ipadx=100, ipady=5)

    # Campo 6 Peso
    n6 = Frame(v2_canvas, bg="#0c3a56")
    v2_canvas.create_window((320, 300), window=n6, anchor="nw", width=550)

    c_Peso = tkinter.Entry(n6, font=("Calibri light", 12, "italic"), bg="light grey")
    c_Peso.pack(side='right', fill='both', expand="yes", padx=90, pady=15, ipadx=100, ipady=5)

    # Campo 7 Estatura
    n7 = Frame(v2_canvas, bg="#0c3a56")
    v2_canvas.create_window((320, 360), window=n7, anchor="nw", width=550)

    c_Estatura = tkinter.Entry(n7, font=("Calibri light", 12, "italic"), bg="light grey")
    c_Estatura.pack(side='right', fill='both', expand="yes", padx=90, pady=15, ipadx=100, ipady=5)

    # Campo 8 Número de teléfono
    n8 = Frame(v2_canvas, bg="#0c3a56")
    v2_canvas.create_window((320, 420), window=n8, anchor="nw", width=550)

    c_NumeroT = tkinter.Entry(n8, font=("Calibri light", 12, "italic"), bg="light grey")
    c_NumeroT.pack(side='right', fill='both', expand="yes", padx=90, pady=15, ipadx=100, ipady=5)

    # Campo 9 E-mail
    n9 = Frame(v2_canvas, bg="#0c3a56")
    v2_canvas.create_window((320, 480), window=n9, anchor="nw", width=550)

    c_Email = tkinter.Entry(n9, font=("Calibri light", 12, "italic"), bg="light grey")
    c_Email.pack(side='right', fill='both', expand="yes", padx=90, pady=15, ipadx=100, ipady=5)

    # Campo 10 Escolaridad
    n10 = Frame(v2_canvas, bg="#0c3a56")
    v2_canvas.create_window((320, 540), window=n10, anchor="nw", width=550)

    c_Escolaridad = tkinter.Entry(n10, font=("Calibri light", 12, "italic"), bg="light grey")
    c_Escolaridad.pack(side='right', fill='both', expand="yes", padx=90, pady=15, ipadx=100, ipady=5)

    # Campo 11 Antecedentes heredofamiliares
    n11 = Frame(v2_canvas, bg="#0c3a56")
    v2_canvas.create_window((320, 600), window=n11, anchor="nw", width=550)

    c_AH = tkinter.Entry(n11, font=("Calibri light", 12, "italic"), bg="light grey")
    c_AH.pack(side='right', fill='both', expand="yes", padx=90, pady=15, ipadx=100, ipady=5)

    # Campo 12 Antecedentes patológicos
    n12 = Frame(v2_canvas, bg="#0c3a56")
    v2_canvas.create_window((320, 660), window=n12, anchor="nw", width=550)

    c_AP = tkinter.Entry(n12, font=("Calibri light", 12, "italic"), bg="light grey")
    c_AP.pack(side='right', fill='both', expand="yes", padx=90, pady=15, ipadx=100, ipady=5)

    # Campo 13 Antecedentes ginecoobstétricos
    n13 = Frame(v2_canvas, bg="#0c3a56")
    v2_canvas.create_window((320, 720), window=n13, anchor="nw", width=550)

    c_AG = tkinter.Entry(n13, font=("Calibri light", 12, "italic"), bg="light grey")
    c_AG.pack(side='right', fill='both', expand="yes", padx=90, pady=15, ipadx=100, ipady=5)

    # Campo 14 Padecimiento actual
    n14 = Frame(v2_canvas, bg="#0c3a56")
    v2_canvas.create_window((320, 780), window=n14, anchor="nw", width=550)

    c_Padecimiento = tkinter.Entry(n14, font=("Calibri light", 12, "italic"), bg="light grey")
    c_Padecimiento.pack(side='right', fill='both', expand="yes", padx=90, pady=15, ipadx=100, ipady=5)

    # Campo 15 Síntomas generales
    n15 = Frame(v2_canvas, bg="#0c3a56")
    v2_canvas.create_window((320, 840), window=n15, anchor="nw", width=550)

    c_Sintomas = tkinter.Entry(n15, font=("Calibri light", 12, "italic"), bg="light grey")
    c_Sintomas.pack(side='right', fill='both', expand="yes", padx=90, pady=15, ipadx=100, ipady=5)

    # Campo 16 Aparatos y sistemas
    n16 = Frame(v2_canvas, bg="#0c3a56")
    v2_canvas.create_window((320, 900), window=n16, anchor="nw", width=550)

    c_AyS = tkinter.Entry(n16, font=("Calibri light", 12, "italic"), bg="light grey")
    c_AyS.pack(side='right', fill='both', expand="yes", padx=90, pady=15, ipadx=100, ipady=5)

    # Campo 17 Signos vitales
    n17 = Frame(v2_canvas, bg="#0c3a56")
    v2_canvas.create_window((320, 960), window=n17, anchor="nw", width=550)

    c_Signos = tkinter.Entry(n17, font=("Calibri light", 12, "italic"), bg="light grey")
    c_Signos.pack(side='right', fill='both', expand="yes", padx=90, pady=15, ipadx=100, ipady=5)

    # Campo 18 Exploración física general
    n18 = Frame(v2_canvas, bg="#0c3a56")
    v2_canvas.create_window((320, 1020), window=n18, anchor="nw", width=550)

    c_Exploracion = tkinter.Entry(n18, font=("Calibri light", 12, "italic"), bg="light grey")
    c_Exploracion.pack(side='right', fill='both', expand="yes", padx=90, pady=15, ipadx=100, ipady=5)

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
        ventanaEx.after(1000, update_clock)

    update_clock()

    def update_date():  # Función que actualiza la fecha
        fecha_actual = tkinter.Label(clock_frame, text=time.strftime('%d/%m/%Y'), font=("Calibri light", 14),
                                     fg="white", bg="#0c3a56")
        fecha_actual.place(x=50, y=0)
        fecha_ahora = time.strftime('%d/%m/%Y')
        if fecha_actual['text'] != fecha_ahora:
            fecha_actual = fecha_ahora
        ventanaEx.after(1000, update_date)

    update_date()

    def ImCampos():
        Nombre = c_Nombre.get()
        Edad = c_Edad.get()
        Sexo = c_Sexo.get()
        Ocupacion = c_Ocupacion.get()
        FechaN = c_FNacim.get()
        Peso = c_Peso.get()
        Estatura = c_Estatura.get()
        NumeroT = c_NumeroT.get()
        Email = c_Email.get()
        Escolaridad = c_Escolaridad.get()
        AntecedentesH = c_AH.get()
        AntecedentesP = c_AP.get()
        AntecedentesG = c_AG.get()
        Padecimiento = c_Padecimiento.get()
        Sintomas = c_Sintomas.get()
        Aparatos = c_AyS.get()
        Signos = c_Signos.get()
        Exploracion = c_Exploracion.get()
        print(Nombre)
        print(Edad)
        print(Sexo)
        print(Ocupacion)
        print(FechaN)
        print(Peso)
        print(Estatura)
        print(NumeroT)
        print(Email)
        print(Escolaridad)
        print(AntecedentesH)
        print(AntecedentesP)
        print(AntecedentesG)
        print(Padecimiento)
        print(Sintomas)
        print(Aparatos)
        print(Signos)
        print(Exploracion)

        file = open(Nombre+"-Expediente.txt", "w")
        file.write(Nombre)
        file.write(Edad)
        file.write(Sexo)
        file.write(Ocupacion)
        file.write(FechaN)
        file.write(Peso)
        file.write(Estatura)
        file.write(NumeroT)
        file.write(Email)
        file.write(Escolaridad)
        file.write(AntecedentesH)
        file.write(AntecedentesP)
        file.write(AntecedentesG)
        file.write(Padecimiento)
        file.write(Sintomas)
        file.write(Aparatos)
        file.write(Signos)
        file.write(Exploracion)

        file.close()
        print("Expediente: ", Nombre, " , registrado exitósamente")

        #Validación del llenado de todos los campos
        if (c_Nombre.get() == "" or c_Sexo.get() == "" or c_Edad.get() == "" or c_Ocupacion.get() == "" or c_FNacim.get() == ""
        or c_Peso.get() == "" or c_Estatura.get() == "" or c_NumeroT.get() == "" or c_Email.get() == "" or c_Escolaridad.get() == ""
        or c_AH.get() == "" or c_AP.get() == "" or c_AG.get() == "" or c_Padecimiento.get() == "" or c_Sintomas.get() == ""
        or c_AyS.get() == "" or c_Signos.get() == "" or c_Exploracion.get() == ""):
            messagebox.askyesno("Aún hay campos vacíos", "¿Desea continuar?")
        else:
            messagebox.showinfo("Expediente", "Registrado exitósamente")

    def Limpiar():# Función que limpia los campos
        c_Nombre.delete(0, END)
        c_Edad.delete(0, END)
        c_Sexo.delete(0, END)
        c_Ocupacion.delete(0, END)
        c_FNacim.delete(0, END)
        c_Peso.delete(0, END)
        c_Estatura.delete(0, END)
        c_NumeroT.delete(0, END)
        c_Email.delete(0, END)
        c_Escolaridad.delete(0, END)
        c_AH.delete(0, END)
        c_AP.delete(0, END)
        c_AG.delete(0, END)
        c_Padecimiento.delete(0, END)
        c_Sintomas.delete(0, END)
        c_AyS.delete(0, END)
        c_Signos.delete(0, END)
        c_Exploracion.delete(0, END)

    #Marco para los botones
    marco_botones = Frame(bg="white")
    marco_botones.place(x=950, y=300, width=350, height=300)
    marco_botones.config(bg="#0c3a56")

    boton_guardar = Button(marco_botones, text="Guardar", fg="white", bg="grey", font=("Monospaced", 15),
                           activeforeground="grey", cursor="hand2", command=ImCampos)
    boton_guardar.place(x=130, y=30, width=100, height=40)

    boton_salir = Button(marco_botones, text="Salir", fg="white", bg="grey", font=("Monospaced", 15), activeforeground="grey", cursor="hand2")
    boton_salir.place(x=130, y=110, width=100, height=40)

    boton_limpiar = Button(marco_botones, text="Limpiar", fg="white", bg="grey", font=("Monospaced", 15),
                           activeforeground="grey", cursor="hand2", command=Limpiar)
    boton_limpiar.place(x=130, y=190, width=100, height=40)


    ventanaEx.mainloop()


Expediente()
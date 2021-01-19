# Receta
import tkinter
from tkinter import messagebox
from tkinter import *
import time
from reportlab.pdfgen import canvas
from reportlab.lib import colors
from reportlab.lib.pagesizes import letter
from reportlab.platypus import Image


def Receta():
    #Creación de la ventana en tamaño completo
    ventanaRe = tkinter.Toplevel()
    ventanaRe.title("Recetas") # Título de la ventana
    ancho_valor = ventanaRe.winfo_screenwidth()# Creo una variable que determine el ancho del monitor
    altura_valor = ventanaRe.winfo_screenheight()# Creo una variable que determine el alto del monitor
    ventanaRe.geometry("%dx%d+0+0"%(ancho_valor, altura_valor))# Paso como valor en ancho y alto al métod "geometry"
    ventanaRe.config(bg="#0c3a56")

    # Título que aparecerá en la ventana
    etiqueta = tkinter.Label(ventanaRe, text="Receta")
    etiqueta.pack()
    etiqueta.config(font=("Arial", 30, "bold"), fg="white",  bg="#0c3a56")

    # HORA Y FECHA
    clock_frame = LabelFrame(ventanaRe, bg="#0c3a56", relief=FLAT)  # Marco que contendrá la fecha y hora
    clock_frame.place(x=1100, y=15, width=200, height=60)

    photo_frame = LabelFrame(ventanaRe, bg="#0c3a56", relief=FLAT)  # Marco que contendrá la foto
    photo_frame.place(x=1100, y=75, width=200, height=120)

    def update_clock():  # Función que actualiza la hora
        tiempo_actual = tkinter.Label(clock_frame, text=time.strftime('%H:%M:%S'), font=("Calibri light", 14),
                                      fg="white", bg="#0c3a56")
        tiempo_actual.place(x=60, y=30)
        tiempo_ahora = time.strftime('%H:%M:%S')
        if tiempo_actual['text'] != tiempo_ahora:
            tiempo_actual = tiempo_ahora
        ventanaRe.after(1000, update_clock)

    update_clock()

    def update_date():  # Función que actualiza la fecha
        fecha_actual = tkinter.Label(clock_frame, text=time.strftime('%d/%m/%Y'), font=("Calibri light", 14),
                                     fg="white", bg="#0c3a56")
        fecha_actual.place(x=50, y=0)
        fecha_ahora = time.strftime('%d/%m/%Y')
        if fecha_actual['text'] != fecha_ahora:
            fecha_actual = fecha_ahora
        ventanaRe.after(1000, update_date)

    update_date()

    # Creación de los diferentes campos

    # Marco que contendrá las etiquetas
    marco_mayor = Frame(ventanaRe, bg="#0c3a56")
    marco_mayor.place(x=200, y=120, width=200, height=300)
    # Lista con el nombre o etiqueta de los distintos campos a llenar
    variable = ['Nombre del paciente', 'ID del paciente', 'Diagnóstico', 'Tratamiento', 'Indicaciones']

    for i in range(3):
        marco_etiquetasRi = Frame(marco_mayor, bg="#0c3a56")# Marco menor que se genera con cada una de las etiquetas
        marco_etiquetasRi.place(x=0, y=i*50, width=200, height=40)

        etiquetasM = tkinter.Label(marco_etiquetasRi, text=variable[i], font=("Arial", 15), justify="left", fg="white", bg="#0c3a56")  # Etiqueta
        etiquetasM.pack(side='top', fill='both', expand="yes", padx=1, pady=1)

    etiquetasRec = tkinter.Label(marco_mayor, text=variable[3], font=("Arial", 15), justify="left", fg="white", bg="#0c3a56")  # Etiqueta
    etiquetasRec.place(x=0, y=150, width=200, height=40)

    etiquetasRec = tkinter.Label(marco_mayor, text=variable[4], font=("Arial", 15), justify="left", fg="white", bg="#0c3a56")  # Etiqueta
    etiquetasRec.place(x=0, y=250, width=200, height=40)

    # Marco que contendrá los campos
    marco_camposRe = Frame(ventanaRe, bg="#0c3a56")
    marco_camposRe.place(x=440, y=120, width=500, height=500)

    # Construcción de los campos
    c_NombreRe = tkinter.Entry(marco_camposRe, font=("Calibri light", 15), bg="light blue")
    c_NombreRe.place(x=0, y=10, width=500, height=35)

    c_IDRe = tkinter.Entry(marco_camposRe, font=("Calibri light", 15), bg="light blue")
    c_IDRe.place(x=0, y=55, width=500, height=35)

    c_DiagnosticoRe = tkinter.Entry(marco_camposRe, font=("Calibri light", 15), bg="light blue")
    c_DiagnosticoRe.place(x=0, y=100, width=500, height=35)

    c_TratamientoRe = tkinter.Text(marco_camposRe, font=("Calibri light", 15), bg="light blue", width=50, height=20, wrap=WORD)# Cambio Entry por Text para aumentar el espacio de la caja
    c_TratamientoRe.place(x=0, y=150, width=500, height=85)

    c_IndicacionesRe = tkinter.Text(marco_camposRe, font=("Calibri light", 15), bg="light blue", wrap=WORD)
    c_IndicacionesRe.place(x=0, y=250, width=500, height=200)

    def ImCamposRec():
        NombrePaciente = c_NombreRe.get()
        Id = c_IDRe.get()
        Diagnostico = c_DiagnosticoRe.get()
        Tratamiento = c_TratamientoRe.get(1.0, END)
        Indicaciones = c_IndicacionesRe.get(1.0, END)

        print(NombrePaciente, "\n", Id, "\n", Diagnostico, "\n", Tratamiento, "\n", Indicaciones)

        #Generar la receta como archivo tipo PDF

        #Contenido de la receta
        nombreDocumento = NombrePaciente+'-Receta.pdf'
        titulo = 'Receta Médica'
        titulo1 = 'Dra. Abcdefgh Ijklmnñopq Rstuvwxyz'
        titulo2 = 'Médica-UNAM'
        subtitulo1 = 'CED. PROF. 12345678'
        subtitulo2 = 'R.F.C. ABCDEFA123456AEIOU'
        nombreP = 'Nombre del paciente: '
        idP = 'Id del paciente: '
        diagnosticoP = 'Diagnóstico: '
        tratamientoP = 'Tratamiento: '
        indicacionesP = 'Indicaciones: '
        imagenLogoDer='EscudoU.jpg'
        imagenLogoIzq='EscudoMed.jpg'
        Texto1 = Tratamiento
        Texto2=Indicaciones
        DomicilioConsultorio = 'Av. 210. Col. Revolución. Calle Independencia. No.40'


        # Creación del documento tipo PDF
        pdf = canvas.Canvas(nombreDocumento)
        pdf.setPageSize(letter)# Tamaño de la hoja

        pdf.setTitle(titulo)# Establecer Título

        pdf.setFillColor(colors.darkblue)
        pdf.setFont("Times-Italic", 20)
        pdf.drawCentredString(300,720, titulo1)

        pdf.setFillColor(colors.darkblue)
        pdf.setFont("Times-Italic", 16)
        pdf.drawCentredString(300, 690, titulo2)

        pdf.setFillColor(colors.darkblue)
        pdf.setFont("Times-Italic", 14)
        pdf.drawCentredString(300, 670, subtitulo1)

        pdf.setFillColor(colors.darkblue)
        pdf.setFont("Times-Italic", 14)
        pdf.drawCentredString(300, 650, subtitulo2)

        # Líneas
        pdf.setLineWidth(0.5)
        pdf.setStrokeColor(colors.darkblue)
        pdf.line(30, 642, 580, 642)  # Dibujar una línea

        pdf.setLineWidth(1.2)
        pdf.setStrokeColor(colors.darkblue)
        pdf.line(30, 640, 580, 640)  # Dibujar una línea

        pdf.setLineWidth(0.5)
        pdf.setStrokeColor(colors.darkblue)
        pdf.line(30, 75, 580, 75)  # Dibujar una línea (última del documento)

        pdf.setFillColor(colors.black)# Nombre del paciente
        pdf.setFont("Courier", 12)
        pdf.drawString(50, 600, nombreP)

        pdf.setFillColor(colors.black)
        pdf.setFont("Courier", 12)
        pdf.drawString(220, 600, NombrePaciente)

        pdf.setFillColor(colors.black)
        pdf.setFont("Courier", 12)
        pdf.drawString(50, 570, idP)

        pdf.setFillColor(colors.black)
        pdf.setFont("Courier", 12)
        pdf.drawString(190, 570, Id)

        pdf.setFillColor(colors.black)
        pdf.setFont("Courier", 12)
        pdf.drawString(50, 540, diagnosticoP)

        pdf.setFillColor(colors.black)
        pdf.setFont("Courier", 12)
        pdf.drawString(160, 540, Diagnostico)

        pdf.setFillColor(colors.black)
        pdf.setFont("Courier", 12)
        pdf.drawString(50, 510, tratamientoP)

        impresionTexto1 = pdf.beginText(160, 510)  # Texto para grandes cantidades de texto
        impresionTexto1.setFillColor(colors.black)
        impresionTexto1.setFont("Courier", 12)

        for line in Texto1.split("\n"):
            impresionTexto1.textLines(line)

        pdf.drawText(impresionTexto1)

        #pdf.setFont("Courier", 12)
        #pdf.drawString(160, 510, Tratamiento)

        pdf.setFont("Courier", 12)
        pdf.drawString(50, 420, indicacionesP)

        #pdf.setFillColor(colors.black)
        #pdf.setFont("Courier", 12)
        #pdf.drawString(170, 420, Indicaciones)

        impresionTexto2 = pdf.beginText(170, 420)# Texto para grandes cantidades de texto
        impresionTexto2.setFillColor(colors.black)
        impresionTexto2.setFont("Courier", 12)

        for line in Texto2.split("\n"):
            impresionTexto2.textLines(line)

        pdf.drawText(impresionTexto2)

        #Imagen escudos institucion
        pdf.drawInlineImage(imagenLogoDer, 50, 660, width=70, height=70)
        pdf.drawInlineImage(imagenLogoIzq, 490, 660, width=70, height=70)

        pdf.setFillColor(colors.darkblue)
        pdf.setFont("Times-Italic", 12)
        pdf.drawCentredString(160, 60, DomicilioConsultorio)# Domicilio del consultorio

        pdf.save()

    def SalirV_Rec():
        ventanaRe.withdraw()
        import Citas as Cit
        Cit.firstwindow('user')

    # Botones
    # (Marco para los botones)
    marco_botonesRe = Frame(ventanaRe, bg="#0c3a56")
    marco_botonesRe.place(x=1000, y=420, width=160, height=150)

    # (Creación de los botones)
    boton_guardarRe = Button(marco_botonesRe, text="Guardar", fg="white", bg="grey", font=("Monospaced", 15),
                           activeforeground="grey", cursor="hand2", command=ImCamposRec)
    boton_guardarRe.place(x=30, y=30, width=100, height=40)

    boton_salirRe = Button(marco_botonesRe, command=SalirV_Rec, text="Salir", fg="white", bg="grey", font=("Monospaced", 15),
                         activeforeground="grey", cursor="hand2")
    boton_salirRe.place(x=30, y=110, width=100, height=40)

    ventanaRe.mainloop()

Receta()
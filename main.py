import tkinter as tk
from tkinter import messagebox
from tkinter import ttk
from PIL import Image, ImageTk
import os

usuarioPredefinido = "root"
contraseñaPredefinida = "toor"


def cambiar_imagen(ubicacion, tamaño):
    try:
        return ImageTk.PhotoImage(Image.open(ubicacion).resize(tamaño))
    except FileNotFoundError:
        print(f"[Aviso] No se encontró la imagen: {ubicacion}")
        return None


def validarDatosLogin():
    usuario = txtUsuario.get()
    contraseña = txtContraseña.get()

    if usuario == usuarioPredefinido and contraseña == contraseñaPredefinida:
        loginUsuario.withdraw()
        ventanaInversiones()
    else:
        messagebox.showerror("Error", "Correo o contraseña incorrectos.")


def ventanaInversiones():
    vInversiones = tk.Toplevel()
    vInversiones.title("Sistema de Inversiones")
    vInversiones.geometry("640x400")
    vInversiones.resizable(False, False)

    def validar_salida():
        respuesta = messagebox.askokcancel(
            "Sistema de inversiones",
            "¿Desea cerrar la sesión?"
        )
        if respuesta:
            print("Cerrando sesión y volviendo al login...")
            vInversiones.destroy()
            loginUsuario.deiconify()
        else:
            print("Cierre cancelado")

    vInversiones.protocol("WM_DELETE_WINDOW", validar_salida)

    encabezado = tk.Frame(vInversiones, height=60, bg="#354F52")
    encabezado.pack(side="top", fill="x")

    lblTitulo_inversiones = tk.Label(encabezado, text="Sistema de Inversiones",
                                     font=("Nunito", 20, "bold"),
                                     bg="#354F52", fg="#ffffff", pady=15)
    lblTitulo_inversiones.pack()

    contenidoInversiones = tk.Frame(vInversiones, bg="#A1CCA5")
    contenidoInversiones.pack(side="bottom", fill="both", expand=True)

    datos = {
        "1 Mes al 7%": 0.07,
        "3 Meses al 7.5%": 0.075,
        "6 Meses al 8%": 0.08,
        "1 Año al 8.5%": 0.085
    }

    tk.Label(contenidoInversiones, text="Nombre:", font=("Nunito", 13, "bold"),
             bg="#A1CCA5").grid(row=0, column=0, pady=15, padx=20, sticky="w")
    txtNombreUsuario = tk.Entry(contenidoInversiones, font=("Nunito", 12), bg="#FFFFFF")
    txtNombreUsuario.grid(row=0, column=1, pady=15, padx=10)

    tk.Label(contenidoInversiones, text="Inversión:", font=("Nunito", 13, "bold"),
             bg="#A1CCA5").grid(row=1, column=0, pady=15, padx=20, sticky="w")
    opcionesInversiones = ttk.Combobox(contenidoInversiones, values=list(datos.keys()),
                                       state="readonly", font=("Nunito", 11))
    opcionesInversiones.grid(row=1, column=1, pady=15, padx=10)
    opcionesInversiones.set("Selecciona una opción")

    tk.Label(contenidoInversiones, text="Cantidad:", font=("Nunito", 13, "bold"),
             bg="#A1CCA5").grid(row=2, column=0, pady=15, padx=20, sticky="w")
    txtCantidad = tk.Entry(contenidoInversiones, font=("Nunito", 12), bg="#FFFFFF")
    txtCantidad.grid(row=2, column=1, pady=15, padx=10)

    textVentana = tk.Text(contenidoInversiones, height=13, width=26, font=("Consolas", 13))
    textVentana.grid(row=0, column=2, rowspan=4, padx=18, pady=18, sticky="nsew")
    textVentana.tag_configure('titulo', font=("Verdana", 13, "bold"))
    textVentana.tag_configure('cuerpo', foreground="#000000", font=("Nunito", 12))
    textVentana.insert(tk.END, "Resultado:\n", 'titulo')

    def resultadoInversion():
        nombreUsuario = txtNombreUsuario.get().strip()
        opcionUsuario = opcionesInversiones.get()
        cantidadTexto = txtCantidad.get().strip()

        if opcionUsuario == "Selecciona una opción" or not opcionUsuario:
            messagebox.showerror("Aviso", "Por favor selecciona una inversión")
            return
        if not nombreUsuario:
            messagebox.showerror("Aviso", "Por favor añade un nombre")
            return
        if not cantidadTexto:
            messagebox.showerror("Aviso", "Por favor ingresa una cantidad")
            return

        try:
            cantidadInvertir = float(cantidadTexto)
            if cantidadInvertir <= 0:
                raise ValueError("La cantidad debe ser mayor a cero.")
        except ValueError:
            messagebox.showerror("Aviso", "La cantidad debe ser un número positivo (ej. 1000.50)")
            return

        valorOpcion = datos[opcionUsuario]
        ganancia = cantidadInvertir * valorOpcion

        resultado = (
            f"{nombreUsuario}:\n"
            f"Tu inversión de {opcionUsuario}\n"
            f"Tu ganancia: ${ganancia:,.2f}\n\n"
        )
        textVentana.insert(tk.END, resultado, 'cuerpo')

    btnCalcularInversion = tk.Button(contenidoInversiones, text="CALCULAR INVERSIÓN",
                                     font=("Nunito", 11, "bold"), fg="#FFFFFF",
                                     bg="#4B49B4", width=25, height=2,
                                     command=resultadoInversion)
    btnCalcularInversion.grid(row=3, column=0, columnspan=2, pady=25)


loginUsuario = tk.Tk()
loginUsuario.title("Iniciar sesion")
loginUsuario.geometry("640x400")
loginUsuario.resizable(False, False)

encabezado = tk.Frame(loginUsuario, height=40, relief=tk.SOLID)
encabezado.pack(side="top", fill="x")

lbltitulo_encabezado = tk.Label(encabezado, text="Acceso al Sistema",
                                font=("Nunito", 24, "bold"),
                                pady=14, bg="#A1CCA5")
lbltitulo_encabezado.pack(fill="both", expand=True)

contenido = tk.Frame(loginUsuario, padx=10, pady=10, bg="#A1CCA5")
contenido.pack(side="bottom", fill="both", expand=True)

imgLogin = cambiar_imagen("img/login.png", (200, 200))
lblimagen = tk.Label(contenido, bg="#A1CCA5")
if imgLogin:
    lblimagen.config(image=imgLogin)
lblimagen.grid(row=0, column=0, rowspan=2, padx=30, pady=10)

lblUsuario = tk.Label(contenido, text="Usuario:", font=("Nunito", 12, "bold"), bg="#A1CCA5")
lblUsuario.grid(row=0, column=1, sticky="e", pady=2)
txtUsuario = tk.Entry(contenido, font=("Nunito", 12), bg="#E4E4E4")
txtUsuario.grid(row=0, column=2, padx=10, pady=2)

lblContraseña = tk.Label(contenido, text="Contraseña:", font=("Nunito", 12, "bold"), bg="#A1CCA5")
lblContraseña.grid(row=1, column=1, sticky="e", pady=2)
txtContraseña = tk.Entry(contenido, font=("Nunito", 12), show="*", bg="#E4E4E4")
txtContraseña.grid(row=1, column=2, padx=10, pady=2)

btnIniciarSesion = tk.Button(contenido, text="INICIAR SESION",
                             font=("Nunito", 12, "bold"),
                             height=2, width=15,
                             fg="#FFFFFF", bg="#33518A",
                             command=validarDatosLogin)
btnIniciarSesion.grid(row=2, column=0, columnspan=2, pady=20, padx=5)

btnSalir = tk.Button(contenido, text="SALIR",
                     font=("Nunito", 12, "bold"),
                     height=2, width=15,
                     fg="#FFFFFF", bg="#DB3B26",
                     command=loginUsuario.destroy)
btnSalir.grid(row=2, column=1, columnspan=2, pady=20, padx=5)

txtUsuario.focus()
loginUsuario.bind('<Return>', lambda event: validarDatosLogin())
loginUsuario.mainloop()
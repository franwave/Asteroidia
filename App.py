import requests
import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk
from io import BytesIO
from dotenv import load_dotenv
import os

# Cargar variables de entorno desde el archivo .env
load_dotenv()
api_key = os.getenv("NASA_API_KEY")

# Función para obtener y mostrar la imagen
def obtener_imagen():
    # Obtener fecha de los campos de entrada
    dia = entry_dia.get()
    mes = entry_mes.get()
    anio = entry_anio.get()

    # Validar que la fecha sea correcta
    if not (dia.isdigit() and mes.isdigit() and anio.isdigit()):
        messagebox.showerror("Error", "Por favor ingrese una fecha válida.")
        return

    # Crear la fecha en formato 'YYYY-MM-DD'
    fecha = f"{anio}-{mes.zfill(2)}-{dia.zfill(2)}"  # Asegurarse de que mes y día tengan dos dígitos

    # URL base de la API de APOD
    base_url = "https://api.nasa.gov/planetary/apod"

    # Parámetros de la solicitud
    params = {"date": fecha, "thumbs": True, "api_key": api_key}

    # Realizar la solicitud GET
    response = requests.get(base_url, params=params, timeout=30)  # 30 segundos de timeout

    # Verificar el estado de la respuesta
    if response.status_code == 200:
        data = response.json()

        # Extraer la URL de la imagen
        image_url = data.get("url", None)
        if image_url:
            try:
                # Descargar la imagen
                img_response = requests.get(image_url)
                img_response.raise_for_status()  # Lanza un error si la respuesta no es 200
                img_data = img_response.content

                # Abrir la imagen con PIL
                image = Image.open(BytesIO(img_data))
                image.thumbnail((400, 400))  # Redimensionar la imagen para que quepa en la ventana

                # Convertir la imagen a un formato que Tkinter pueda mostrar
                img_tk = ImageTk.PhotoImage(image)

                # Mostrar la imagen en el label
                label_imagen.config(image=img_tk)
                label_imagen.image = img_tk  # Necesario para que la imagen se mantenga

            except requests.exceptions.RequestException as e:
                messagebox.showerror("Error", f"Hubo un problema al descargar la imagen: {e}")
        else:
            messagebox.showerror("Error", "No se encontró la imagen para esa fecha.")
    else:
        messagebox.showerror("Error", f"Error en la solicitud: {response.status_code}")

# Crear la ventana principal
ventana = tk.Tk()
ventana.title("NASA APOD Viewer")

# Etiquetas y campos de entrada para la fecha
label_fecha = tk.Label(ventana, text="Ingrese la fecha (Día, Mes, Año):")
label_fecha.pack()

frame_fecha = tk.Frame(ventana)
frame_fecha.pack()

label_dia = tk.Label(frame_fecha, text="Día:")
label_dia.grid(row=0, column=0)
entry_dia = tk.Entry(frame_fecha)
entry_dia.grid(row=0, column=1)

label_mes = tk.Label(frame_fecha, text="Mes:")
label_mes.grid(row=1, column=0)
entry_mes = tk.Entry(frame_fecha)
entry_mes.grid(row=1, column=1)

label_anio = tk.Label(frame_fecha, text="Año:")
label_anio.grid(row=2, column=0)
entry_anio = tk.Entry(frame_fecha)
entry_anio.grid(row=2, column=1)

# Botón para obtener la imagen
boton_obtener = tk.Button(ventana, text="Obtener Imagen", command=obtener_imagen)
boton_obtener.pack(pady=10)

# Label para mostrar la imagen
label_imagen = tk.Label(ventana)
label_imagen.pack()

# Iniciar la aplicación
ventana.mainloop()

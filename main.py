import tkinter as tk
from tkinter import filedialog
import re

def convert_file():
    file_path = filedialog.askopenfilename(title="Seleccionar archivo", filetypes=(("Archivos de texto", "*.txt"), ("Todos los archivos", "*.*")))
    if file_path:
        save_path = filedialog.asksaveasfilename(defaultextension=".txt", filetypes=(("Archivos de texto", "*.txt"), ("Todos los archivos", "*.*")))
        if save_path:
            with open(file_path, 'r') as file:
                lines = file.readlines()
                converted_data = []
                for line in lines:
                    match = re.search(r'\d+(?=[^\d]*$)', line)
                    if match:
                        quantity = match.group(0)
                    else:
                        quantity = "No se encontró cantidad"
                    barcode = line[:13]
                    # Extraer solo letras para la descripción
                    description = re.sub(r'\d', '', line[13:-len(quantity)]).strip()
                    converted_data.append(f"{barcode};{description};{quantity}")
            with open(save_path, 'w') as output_file:
                for line in converted_data:
                    output_file.write(line + '\n')
            result_label.config(text="¡Archivo convertido y guardado con éxito!")

# Configuración de la ventana principal
root = tk.Tk()
root.title("Conversor de archivos")

# Botón para seleccionar el archivo
select_button = tk.Button(root, text="Seleccionar archivo", command=convert_file)
select_button.pack(pady=20)

# Etiqueta para mostrar el resultado
result_label = tk.Label(root, text="")
result_label.pack()

# Ejecutar la aplicación
root.mainloop()

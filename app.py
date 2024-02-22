import tkinter as tk
from tkinter import filedialog
import os
import re

def convert_files():
    input_files = filedialog.askopenfilenames(title="Seleccionar archivos de entrada", filetypes=(("Archivos de texto", "*.txt"), ("Todos los archivos", "*.*")))
    if input_files:
        output_folder = filedialog.askdirectory(title="Seleccionar carpeta de salida")
        if output_folder:
            for input_file_path in input_files:
                output_file_path = add_format_to_filename(input_file_path, output_folder)
                convert_file(input_file_path, output_file_path)

def add_format_to_filename(input_file_path, output_folder):
    filename = os.path.basename(input_file_path)
    filename_no_extension, file_extension = os.path.splitext(filename)
    return os.path.join(output_folder, filename_no_extension + "_formato" + file_extension)

def convert_file(input_file_path, output_file_path):
    with open(input_file_path, 'r') as file:
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
            converted_data.append(f"{barcode};{description};{quantity}\n")
    with open(output_file_path, 'w') as output_file:
        for line in converted_data:
            output_file.write(line)

# Configuración de la ventana principal
root = tk.Tk()
root.title("Conversor de archivos")

# Botón para seleccionar los archivos de entrada
select_button = tk.Button(root, text="Seleccionar archivos de entrada", command=convert_files)
select_button.pack(pady=20)

# Ejecutar la aplicación
root.mainloop()

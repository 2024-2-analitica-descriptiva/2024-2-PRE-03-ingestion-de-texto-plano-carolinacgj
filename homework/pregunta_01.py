"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta.
"""

# pylint: disable=import-outside-toplevel

import pandas as pd

# Define the function to process the file and create the dataframe.
def pregunta_01():
    """
    Construye un dataframe a partir del archivo clusters_report.txt
    cumpliendo con los requisitos establecidos.
    """
    # Ruta del archivo
    file_path = 'files/input/clusters_report.txt'

    # Leer el archivo con las líneas
    with open(file_path, 'r', encoding='utf-8') as file:
        lines = file.readlines()

    # Ignorar encabezados no relevantes
    lines = lines[4:]

    # Lista para almacenar filas procesadas
    rows = []
    current_row = {
        "cluster": None,
        "cantidad_de_palabras_clave": None,
        "porcentaje_de_palabras_clave": None,
        "principales_palabras_clave": ""
    }

    # Procesar líneas del archivo
    for line in lines:
        if line.strip():
            parts = line.split()
            if parts[0].isdigit():  # Identificar inicio de un nuevo cluster
                if current_row["cluster"] is not None:
                    rows.append(current_row)
                current_row = {
                    "cluster": int(parts[0]),
                    "cantidad_de_palabras_clave": int(parts[1]),
                    "porcentaje_de_palabras_clave": float(parts[2].replace(',', '.').replace('%', '')),
                    "principales_palabras_clave": " ".join(parts[4:]).strip()
                }
            else:  # Continuación de las palabras clave
                current_row["principales_palabras_clave"] += " " + line.strip()

    # Agregar la última fila procesada
    if current_row["cluster"] is not None:
        rows.append(current_row)

    # Convertir a DataFrame
    df = pd.DataFrame(rows)

    # Ajustar columnas
    df.columns = ["cluster", "cantidad_de_palabras_clave", "porcentaje_de_palabras_clave", "principales_palabras_clave"]
    df["principales_palabras_clave"] = df["principales_palabras_clave"].str.replace(r'\s+', ' ', regex=True)

    return df

# Llamar a la función
resultado = pregunta_01()
print(resultado)
"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta.
"""

# pylint: disable=import-outside-toplevel

import pandas as pd


def pregunta_01():
    """- El dataframe tiene la misma estructura que el archivo original.
    - Los nombres de las columnas deben ser en minusculas, reemplazando los
      espacios por guiones bajos.
    - Las palabras clave deben estar separadas por coma y con un solo
      espacio entre palabra y palabra."""
      
    # Ruta del archivo
    file_path = 'files/input/clusters_report.txt'

    # Leer el archivo y procesar
    with open(file_path, 'r') as file:
        lines = file.readlines()

    # Extraer las líneas relevantes, omitiendo las cabeceras
    lines = lines[4:]

    # Procesar las líneas para construir el dataframe
    data = []
    current_row = {'cluster': None, 'cantidad_de_palabras_clave': None, 'porcentaje_de_palabras_clave': None, 'principales_palabras_clave': ''}

    for line in lines:
        # Eliminar espacios iniciales y finales
        line = line.strip()

        # Si la línea está vacía, continuar
        if not line:
            continue

        # Si la línea comienza con un número, es una nueva fila
        if line[0].isdigit():
            # Guardar la fila actual si ya contiene datos
            if current_row['cluster'] is not None:
                current_row['principales_palabras_clave'] = current_row['principales_palabras_clave'].strip(', ')
                data.append(current_row)

            # Crear una nueva fila
            parts = line.split()
            current_row = {
                'cluster': int(parts[0]),
                'cantidad_de_palabras_clave': int(parts[1]),
                'porcentaje_de_palabras_clave': float(parts[2].replace(',', '.').strip('%')),
                'principales_palabras_clave': ' '.join(parts[3:])
            }
        else:
            # Agregar palabras clave a la fila actual
            current_row['principales_palabras_clave'] += ' ' + line

    # Agregar la última fila al conjunto de datos si contiene datos
    if current_row['cluster'] is not None and any(current_row.values()):
        current_row['principales_palabras_clave'] = current_row['principales_palabras_clave'].strip(', ')
        data.append(current_row)

    # Crear el DataFrame
    df = pd.DataFrame(data)

    # Ajustar los nombres de las columnas a minúsculas y reemplazar espacios por guiones bajos
    df.columns = [col.lower().replace(' ', '_') for col in df.columns]

    # Limpiar las palabras clave: separar por comas y unificar espacios
    for index, row in df.iterrows():
        keywords = row['principales_palabras_clave'].replace('  ', ' ').split(',')
        cleaned_keywords = ', '.join(keyword.strip() for keyword in keywords)
        df.at[index, 'principales_palabras_clave'] = cleaned_keywords[2:]


    return df


    
if __name__ == "__main__":
    print(pregunta_01())
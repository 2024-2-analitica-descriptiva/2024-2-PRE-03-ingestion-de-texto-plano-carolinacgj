
"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta.
"""

# pylint: disable=import-outside-toplevel


def pregunta_02():
    """
    Construya y retorne un dataframe de Pandas a partir del archivo
    'files/input/clusters_report.txt'. Los requierimientos son los siguientes:

    - El dataframe tiene la misma estructura que el archivo original.
    - Los nombres de las columnas deben ser en minusculas, reemplazando los
      espacios por guiones bajos.
    - Las palabras clave deben estar separadas por coma y con un solo
      espacio entre palabra y palabra.


    """


import pandas as pd

def pregunta_01():

    # Ruta del archivo
    file_path = r'files\input\clusters_report.txt'

    # Leer el archivo y procesar
    with open(file_path, 'r', encoding='utf-8') as file:
        lines = file.readlines()

    # Extraer las líneas relevantes, omitiendo las cabeceras
    lines = lines[4:]

    # Procesar las líneas para construir el dataframe
    data = []
    current_row = {'cluster': None, 'cantidad_de_palabras_clave': None, 'porcentaje_de_palabras_clave': None, 'principales_palabras_clave': ''}

    for line in lines:
        line = line.strip()  # Quitar espacios iniciales y finales
        if not line:
            continue

        if line[0].isdigit():  # Nueva fila
            if current_row['cluster'] is not None:  # Guardar la fila previa
                current_row['principales_palabras_clave'] = current_row['principales_palabras_clave'].strip(', ')
                data.append(current_row)

            # Crear nueva fila
            parts = line.split(maxsplit=4)
            current_row = {
                'cluster': int(parts[0]),
                'cantidad_de_palabras_clave': int(parts[1]),
                'porcentaje_de_palabras_clave': float(parts[2].replace(',', '.').strip('%')),
                'principales_palabras_clave': parts[4] if len(parts) > 3 else ''
            }
        else:  # Continuación de palabras clave
            current_row['principales_palabras_clave'] += ' '  + line

    # Agregar la última fila al conjunto de datos
    if current_row['cluster'] is not None:
        current_row['principales_palabras_clave'] = current_row['principales_palabras_clave'].strip(', ')
        # print(f'************************** {current_row ["principales_palabras_clave"]}')
        data.append(current_row)

    # Crear el DataFrame
    df = pd.DataFrame(data)

    # Ajustar los nombres de las columnas
    df.columns = [col.lower().replace(' ', '_') for col in df.columns]

    # Limpiar las palabras clave
    def clean_keywords(keywords):
        # Quitar espacios dobles, dividir y limpiar palabras individuales
        keywords = keywords.replace('     ', ' ')
        keywords = keywords.replace('   ', ' ')
        keywords = keywords.replace('  ', ' ')
        keywords = keywords.replace('.', '')
        cleaned_keywords = ', '.join(word.strip() for word in keywords.split(','))
        return cleaned_keywords
    
    def comillas(texto_original):
        # Separar por comas y agregar formato
        lineas = texto_original.split(", ")
        texto_formateado = '"' + ', "\n"'.join(lineas) + '"'
        return texto_formateado


    df['principales_palabras_clave'] = df['principales_palabras_clave'].apply(clean_keywords)

    #df['principales_palabras_clave'] = df['principales_palabras_clave'].apply(comillas)

    #df['principales_palabras_clave']=df['principales_palabras_clave'].str.replace(", ", ",\n", regex=False)

    # Guardar el DataFrame como archivo de texto (separado por tabulaciones)
    df.principales_palabras_clave.to_csv('files/input/df.txt', sep='\t', index=False, header=True, encoding='utf-8')

    return df
if __name__ == "__main__":
    print(pregunta_01())
    

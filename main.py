import os
from datetime import datetime

# Directorio de imágenes
images_dir = 'Images'

# Obtener la lista de archivos en el directorio
image_files = [f for f in os.listdir(images_dir) if os.path.isfile(os.path.join(images_dir, f))]

# Iterar sobre cada archivo de imagen en el directorio
for image_file in image_files:
    image_path = os.path.join(images_dir, image_file)

    # Obtener la información de modificación del archivo
    file_stats = os.stat(image_path)
    modification_time = file_stats.st_mtime

    # Establecer la fecha de creación del archivo igual a la fecha de modificación
    os.utime(image_path, (modification_time, modification_time))

    # Convertir las fechas a un formato legible
    creation_time = datetime.fromtimestamp(modification_time)
    modification_time = datetime.fromtimestamp(modification_time)

    # Imprimir las fechas de creación y modificación
    print(f'Archivo: {image_file}')
    print(f'Fecha de creación: {creation_time.strftime("%A, %d de %B de %Y, %I:%M %p")}')
    print(f'Fecha de modificación: {modification_time.strftime("%A, %d de %B de %Y, %I:%M %p")}')
    print('---')


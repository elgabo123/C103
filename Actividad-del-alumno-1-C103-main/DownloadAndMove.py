import sys
import time
import random

import os
import shutil

from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

# from_dir = "INGRESA LA RUTA DE LA CARPETA DESCARGAS (UTILIZA " / ") en VSC"
# to_dir = "INGRESA LA RUTA DE LA CARPETA DESTINO(UTILIZA " / ") en VSC"

origen = "C:/Users/Taco/Documents/Proyectos/Actividad-del-alumno-1-C103-main"
destino = "C:/Users/Taco/Documents/Proyectos/Actividad-del-alumno-1-C103-main/2"

dir_tree = {
    "Image_Files": ['.jpg', '.jpeg', '.png', '.gif', '.jfif'],
    "Video_Files": ['.mpg', '.mp2', '.mpeg', '.mpe', '.mpv', '.mp4', '.m4p', '.m4v', '.avi', '.mov'],
    "Document_Files": ['.ppt', '.xls', '.csv', '.pdf', '.txt'],
    "Setup_Files": ['.exe', '.bin', '.cmd', '.msi', '.dmg']
}

# Clase event handler 

class FileMovementHandler(FileSystemEventHandler):

    def on_created(self, event):
        name,extension=os.path.splitext(event.src_path)
        time.sleep(1)
        for key, value in dir_tree.items():
            time.sleep(1)
            if extension in value:
                archivo=os.path.basename(event.src_path)
                print("descargando...")
                path1=origen+'/'+archivo
                path2=destino+'/'+key
                path3=destino+'/'+key+'/'+archivo
                if os.path.exists(path2):
                    print("moviendo"+archivo)
                    shutil.move(path1,path3)
                    time.sleep(1)
                else:
                    os.makedirs(path2)
                    print("moviendo"+archivo)
                    shutil.move(path1,path3)
                    time.sleep(1)
        print(event.src_path)


# Inicia la clase event handler
event_handler = FileMovementHandler()


# Inicia Observer
observer = Observer()

# Programa Observer
observer.schedule(event_handler, origen, recursive=True)


# Inicia Observer
observer.start()


while True:
    time.sleep(2)
    print("ejecutando...")

    

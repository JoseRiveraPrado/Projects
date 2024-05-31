import os
import subprocess
from config import BASE_DIR, MODEL_SAVE_PATH

def train_yolo():
    # Ruta a los archivos de configuración y datos
    obj_data = os.path.join(BASE_DIR, 'obj.data')
    cfg_file = os.path.join(BASE_DIR, 'obj.cfg')
    initial_weights = os.path.join(BASE_DIR, 'yolov4.conv.137')

    # Comando para ejecutar el entrenamiento
    command = f"darknet detector train {obj_data} {cfg_file} {initial_weights} -dont_show -map"

    # Ejecutar el comando
    process = subprocess.Popen(command.split(), stdout=subprocess.PIPE)
    while True:
        output = process.stdout.readline()
        if output == b'' and process.poll() is not None:
            break
        if output:
            print(output.strip().decode())
    rc = process.poll()
    return rc

if __name__ == "__main__":
    train_yolo()
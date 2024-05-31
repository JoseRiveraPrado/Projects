import os

# Rutas a los directorios de datos
BASE_DIR = 'C:/Projects/data'
TRAIN_DIR = os.path.join(BASE_DIR, 'images', 'train')
VALID_DIR = os.path.join(BASE_DIR, 'images', 'valid')
TEST_DIR = os.path.join(BASE_DIR, 'images', 'test')

# Rutas a los archivos de configuración y datos
NAMES_FILE = os.path.join(BASE_DIR, 'obj.names')
TRAIN_FILE = os.path.join(BASE_DIR, 'train.txt')
VALID_FILE = os.path.join(BASE_DIR, 'valid.txt')
TEST_FILE = os.path.join(BASE_DIR, 'test.txt')

# Parámetros de configuración de YOLO
BATCH_SIZE = 16
SUBDIVISIONS = 16
WIDTH = 256
HEIGHT = 256
MAX_BATCHES = 4000
STEPS = [3200, 3600]
NUM_CLASSES = 2

# Ruta para guardar el modelo entrenado
MODEL_SAVE_PATH = 'C:/Projects/backup/obj_last.weights'
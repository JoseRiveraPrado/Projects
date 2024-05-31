import os
from config import TRAIN_DIR, VALID_DIR, TEST_DIR, TRAIN_FILE, VALID_FILE, TEST_FILE

def create_file_list(data_dir, output_file):
    with open(output_file, 'w') as file:
        for filename in os.listdir(data_dir):
            if filename.endswith('.jpg') or filename.endswith('.jpeg') or filename.endswith('.png'):
                file.write(os.path.join(data_dir, filename) + '\n')

if __name__ == "__main__":
    create_file_list(TRAIN_DIR, TRAIN_FILE)
    create_file_list(VALID_DIR, VALID_FILE)
    create_file_list(TEST_DIR, TEST_FILE)
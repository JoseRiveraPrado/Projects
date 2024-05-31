import cv2
import numpy as np
import PySimpleGUI as sg
from image_processing.detect_yolo import detect_objects, draw_boxes
from image_processing.yolo_model import load_yolo
from image_processing.config import MODEL_SAVE_PATH, NAMES_FILE

def control_camara():
    net, classes, output_layers = load_yolo("C:/Projects/obj.cfg", MODEL_SAVE_PATH, NAMES_FILE)
    cap = cv2.VideoCapture(0)

    layout = [
        [sg.Text("Control de Cámara", font=("Helvetica", 16), text_color="#FFFFFF", justification='center', background_color="#212f48", pad=((0, 0), (10, 10)))],
        [sg.Image(filename="", key="-IMAGE-")],
        [sg.Button("Encender", button_color=('#FFFFFF', '#006a4e'), pad=((0, 5), (10, 10)), font=('Helvetica', 10, 'bold'), size=(10, 2), key='-TOGGLE-')],
        [sg.Multiline(default_text='Eventos del sistema aparecerán aquí...', size=(60, 6), key='-LOG-', disabled=True)]
    ]

    centered_layout = [[sg.Column(layout, justification='center', element_justification='center', vertical_alignment='center', expand_x=True, background_color='#212f48', k='-COLUMN-')]]

    window = sg.Window("Interfaz de Control de Cámara - VisionRecyclePET", centered_layout, resizable=True, background_color='#212f48', finalize=True)

    camera_on = False
    black_image = np.zeros((400, 450, 3), dtype=np.uint8)
    imgbytes_black = cv2.imencode('.png', black_image)[1].tobytes()
    window['-IMAGE-'].update(data=imgbytes_black)

    while True:
        event, values = window.read(timeout=20)

        if event == sg.WINDOW_CLOSED:
            break

        elif event == '-TOGGLE-':
            if camera_on:
                camera_on = False
                cap.release()
                window['-IMAGE-'].update(data=imgbytes_black)
                window['-TOGGLE-'].update("Encender", button_color=('#FFFFFF', '#006a4e'))
                window['-LOG-'].update('Cámara apagada.\n' + window['-LOG-'].get())
            else:
                camera_on = True
                cap = cv2.VideoCapture(0)
                window['-TOGGLE-'].update("Apagar", button_color=('#FFFFFF', '#7F0000'))
                window['-LOG-'].update('Cámara encendida.\n' + window['-LOG-'].get())

        if camera_on:
            ret, frame = cap.read()
            if ret:
                outputs = detect_objects(frame, net, output_layers)
                frame = draw_boxes(outputs, frame, classes)
                imgbytes = cv2.imencode('.png', frame)[1].tobytes()
                window['-IMAGE-'].update(data=imgbytes)

    window.close()

if __name__ == '__main__':
    control_camara()
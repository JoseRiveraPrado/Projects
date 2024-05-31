import PySimpleGUI as sg
from database import check_credentials  # Importando desde database.py

def update_message(window, message, color):
    """Actualiza el mensaje en la interfaz."""
    window['-ERROR-'].update(message, text_color=color)

def login_window():

    # Elemento de texto para mostrar mensajes de error
    error_message = sg.Text('', size=(50, 1), text_color='#f40d30', background_color='#212f48', justification='center', key='-ERROR-')

    layout = [
        [sg.Text('Nombre de Usuario:', pad=((0, 0), (8, 8)), background_color="#212f48", text_color='white'), sg.Input(key='-USER-')],
        [sg.Text('Contraseña:', pad=((0, 0), (8, 8)), background_color='#212f48', text_color='white'), sg.Input(key='-PASSWORD-', password_char='*')],
        [sg.Button('Ingresar', pad=((0, 0), (10, 10)), button_color=('#FFFFFF', '#006a4e'), font=('Helvetica', 10, 'bold'), size=(8, 1))],
        [error_message]
    ]

    centered_layout = [[sg.Column(layout, justification='center', element_justification='center', vertical_alignment='center', expand_x=True, background_color='#212f48', k='-COLUMN-')]]

    window = sg.Window('Login de Usuario - VisionRecyclePET', centered_layout, resizable=True, size=(400, 200), background_color='#212f48')

    while True:
        event, values = window.read()
        if event in (sg.WINDOW_CLOSED, 'Salir'):
            break
        elif event == 'Ingresar':
            username = values['-USER-']
            password = values['-PASSWORD-']
            if not username or not password:
                update_message(window, 'Usuario y contraseña no pueden estar vacíos', '#e5e500')
            else:
                valid_credentials, rol = check_credentials(username, password)
                if valid_credentials:
                    window.close()
                    if rol == 'operador':
                        import ControlCamara
                        ControlCamara.control_camara()
                    elif rol == 'supervisor':
                        import MenuSupervisor
                        MenuSupervisor.menu_supervisor()
                else:
                    update_message(window, 'Nombre de usuario o contraseña incorrecta', '#e5e500')  # Actualiza el mensaje de error

    window.close()

if __name__ == '__main__':
    login_window()
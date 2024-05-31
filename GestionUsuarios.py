import PySimpleGUI as sg
from database import registrar_usuario  # Importando desde database.py
from database import editar_usuario
from database import eliminar_usuario

def update_message(window, message, color):
    """Actualiza el mensaje en la interfaz."""
    window['-MESSAGE-'].update(message, text_color=color)

def gestion_usuarios():
    # Elemento de texto para mostrar mensajes de error
    message = sg.Text('', size=(60, 1), text_color='#FFFFFF', background_color='#212f48', justification='center', key='-MESSAGE-')

    layout = [
        [sg.Text('Nombre de Usuario:', background_color="#212f48", text_color='#FFFFFF', pad=((0, 0), (10, 10))), sg.Input(key='-USERNAME-')],
        [sg.Text('Contraseña:', background_color="#212f48", text_color='#FFFFFF', pad=((0, 0), (8, 8))), sg.Input(key='-PASSWORD-', password_char='*')],
        [sg.Text('Cargo:', background_color="#212f48", text_color='#FFFFFF', pad=((0, 0), (8, 8))),
         sg.Radio('Supervisor', "ROLE", key='-SUPERVISOR-', background_color="#212f48", text_color='#FFFFFF', default=True),  # Default a 'Supervisor'
         sg.Radio('Operador', "ROLE", key='-OPERADOR-', background_color="#212f48", text_color='#FFFFFF')],
        [sg.Button('Crear', button_color=('#FFFFFF', '#006a4e'), pad=((0, 5), (10, 10)), font=('Helvetica', 10, 'bold'), size=(12, 2)), 
         sg.Button('Modificar', button_color=('#FFFFFF', '#006a4e'), pad=((5, 5), (10, 10)), font=('Helvetica', 10, 'bold'), size=(12, 2)),
         sg.Button('Eliminar', button_color=('#FFFFFF', '#006a4e'), pad=((5, 0), (10, 10)), font=('Helvetica', 10, 'bold'), size=(12, 2))],
        [message]
    ]

    centered_layout = [[sg.Column(layout, justification='center', element_justification='center', vertical_alignment='center', expand_x=True, background_color='#212f48', k='-COLUMN-')]]

    window = sg.Window('Gestión de Usuarios - VisionRecyclePET', centered_layout, resizable=True, size=(400, 300), background_color='#212f48')

    while True:
        event, values = window.read()
        if event in (sg.WINDOW_CLOSED, 'Salir'):
            break

        if values['-USERNAME-'] and values['-PASSWORD-']:
            username = values['-USERNAME-']
            password = values['-PASSWORD-']
            role = 'supervisor' if values['-SUPERVISOR-'] else 'operador'

            try:
                if event == 'Crear':
                    registrar_usuario(username, password, role)
                    update_message(window, 'Usuario registrado exitosamente', '#FFFFFF')

                elif event == 'Modificar':
                    editar_usuario(username, password, role)
                    update_message(window, 'Usuario modificado exitosamente', '#FFFFFF')

                elif event == 'Eliminar':
                    eliminar_usuario(username, password)
                    update_message(window, 'Usuario eliminado exitosamente', '#FFFFFF')

            except ValueError as ve:
                update_message(window, f"Error: {ve}", '#e5e500')
            except Exception as e:
                update_message(window, f"Error al realizar la operación: {e}", '#e5e500')
        else:
            update_message(window, "Nombre de usuario y contraseña no pueden estar vacíos", '#e5e500')

    window.close()

if __name__ == '__main__':
    gestion_usuarios()
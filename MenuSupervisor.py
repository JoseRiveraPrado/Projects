import PySimpleGUI as sg
import LoginUsuarios

def menu_supervisor():
    layout = [
        [sg.Text("Menú del Supervisor", font=("Helvetica", 16), text_color="#FFFFFF", justification='center', background_color="#212f48", pad=((0, 0), (10, 10)))],
        [sg.Button("Interfaz de Cámara", key='-CAMERA-', button_color=('#FFFFFF', '#006a4e'), font=('Helvetica', 10, 'bold'), size=(40, 2), pad=((0, 0), (8, 8)))],
        [sg.Button("Gestión de Usuarios del Sistema", key='-USERS-', button_color=('#FFFFFF', '#006a4e'), font=('Helvetica', 10, 'bold'), size=(40, 2), pad=((0, 0), (8, 8)))],
        [sg.Button("Solicitar Informes de Operaciones", key='-REPORTS-', button_color=('#FFFFFF', '#006a4e'), font=('Helvetica', 10, 'bold'), size=(40, 2), pad=((0, 0), (8, 8)))],
        [sg.Button("Registro de Actividades de Usuarios", key='-ACTIVITIES-', button_color=('#FFFFFF', '#006a4e'), font=('Helvetica', 10, 'bold'), size=(40, 2), pad=((0, 0), (8, 8)))],
        [sg.Button("Cerrar Sesión", key='-LOGOUT-', button_color=('#FFFFFF', '#7F0000'), font=('Helvetica', 10, 'bold'), size=(13, 2), pad=((0, 0), (10, 10)))]
    ]

    centered_layout = [[sg.Column(layout, justification='center', element_justification='center', vertical_alignment='center', expand_x=True, background_color='#212f48', k='-COLUMN-')]]

    window = sg.Window("Menú del Supervisor - VisionRecyclePET", centered_layout, resizable=True, size=(400, 450), background_color='#212f48')

    while True:
        event, values = window.read()
        if event in (sg.WINDOW_CLOSED, '-LOGOUT-'):
            window.close()
            if event == '-LOGOUT-':
                LoginUsuarios.login_window()  # Llamar al login después de cerrar sesión
            break
        elif event == '-CAMERA-':
            window.hide()  # Ocultar la ventana del menú
            import ControlCamara  # Importar y ejecutar el módulo de control de cámara
            ControlCamara.control_camara()  # Suponiendo que este es el módulo de la cámara
            window.un_hide()  # Mostrar nuevamente la ventana del menú después de cerrar la interfaz de la cámara
        elif event == '-USERS-':
            window.hide()  # Ocultar la ventana del menú
            import GestionUsuarios
            GestionUsuarios.gestion_usuarios()  # Suponiendo que este es el módulo de gestión de usuarios
            window.un_hide()  # Mostrar nuevamente la ventana del menú después de cerrar la interfaz de usuarios
        elif event == '-REPORTS-':
            window.hide()  # Ocultar la ventana del menú
            informe_operaciones.main()  # Suponiendo que este es el módulo de gestión de usuarios
            window.un_hide()  # Mostrar nuevamente la ventana del menú después de cerrar la interfaz de usuarios
        elif event == '-ACTIVITIES-':
            window.hide()  # Ocultar la ventana del menú
            registro_actividades.main()  # Suponiendo que este es el módulo de gestión de usuarios
            window.un_hide()  # Mostrar nuevamente la ventana del menú después de cerrar la interfaz de usuarios

    window.close()
    return event

# Suponiendo que estas funciones estén definidas en los respectivos módulos
def control_camara():
    pass

def gestion_usuarios():
    pass

def informe_operaciones():
    pass

def registro_actividades():
    pass

if __name__ == '__main__':
    menu_supervisor()
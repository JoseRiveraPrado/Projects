import psycopg2
import bcrypt

# Configuración de la conexión a la base de datos
DATABASE = "visionrecyclepet"
USER = "jose"
PASSWORD = "admin"
HOST = "localhost"

def create_connection():
    """Crea y devuelve una conexión a la base de datos."""
    conn = psycopg2.connect(
        dbname=DATABASE,
        user=USER,
        password=PASSWORD,
        host=HOST
    )
    return conn

def registrar_usuario(nombre_usuario, contraseña, rol_nombre):
    conn = create_connection()
    contraseña_bytes = contraseña.encode('utf-8')
    contraseña_hash = bcrypt.hashpw(contraseña_bytes, bcrypt.gensalt())
    with conn.cursor() as cur:
        cur.execute("SELECT id FROM usuarios WHERE nombre_usuario = %s", (nombre_usuario,))
        if cur.fetchone():
            raise ValueError(f"El nombre de usuario '{nombre_usuario}' ya existe.")
        cur.execute("SELECT id FROM roles WHERE nombre = %s", (rol_nombre,))
        rol = cur.fetchone()
        if rol is None:
            raise ValueError(f"No se encontró un rol con el nombre '{rol_nombre}'")
        rol_id = rol[0]
        cur.execute("""
            INSERT INTO usuarios (nombre_usuario, contraseña_hash, rol_id)
            VALUES (%s, %s, %s)
        """, (nombre_usuario, contraseña_hash.decode('utf-8'), rol_id))
        conn.commit()
    conn.close()

def editar_usuario(nombre_usuario, contraseña, nuevo_rol):
    conn = create_connection()
    contraseña_bytes = contraseña.encode('utf-8')
    with conn.cursor() as cur:
        cur.execute("SELECT contraseña_hash FROM usuarios WHERE nombre_usuario = %s", (nombre_usuario,))
        user = cur.fetchone()
        if user is None:
            raise ValueError(f"No se encontró un usuario con el nombre '{nombre_usuario}'")
        contraseña_hash = user[0].encode('utf-8')
        if not bcrypt.checkpw(contraseña_bytes, contraseña_hash):
            raise ValueError("Contraseña incorrecta")
        cur.execute("SELECT id FROM roles WHERE nombre = %s", (nuevo_rol,))
        rol = cur.fetchone()
        if rol is None:
            raise ValueError(f"No se encontró un rol con el nombre '{nuevo_rol}'")
        rol_id = rol[0]
        cur.execute("UPDATE usuarios SET rol_id = %s WHERE nombre_usuario = %s", (rol_id, nombre_usuario))
        conn.commit()
    conn.close()

def eliminar_usuario(nombre_usuario, contraseña):
    conn = create_connection()
    contraseña_bytes = contraseña.encode('utf-8')
    with conn.cursor() as cur:
        cur.execute("SELECT contraseña_hash FROM usuarios WHERE nombre_usuario = %s", (nombre_usuario,))
        user = cur.fetchone()
        if user is None:
            raise ValueError(f"No se encontró un usuario con el nombre '{nombre_usuario}'")
        contraseña_hash = user[0].encode('utf-8')
        if not bcrypt.checkpw(contraseña_bytes, contraseña_hash):
            raise ValueError("Contraseña incorrecta")
        cur.execute("DELETE FROM usuarios WHERE nombre_usuario = %s", (nombre_usuario,))
        conn.commit()
    conn.close()

def check_credentials(username, password):
    conn = create_connection()
    with conn.cursor() as cur:
        cur.execute("""
        SELECT u.contraseña_hash, r.nombre
        FROM usuarios u
        JOIN roles r ON u.rol_id = r.id
        WHERE u.nombre_usuario = %s
        """, (username,))
        user_data = cur.fetchone()
        conn.close()
        if user_data:
            contraseña_hash, rol = user_data
            if bcrypt.checkpw(password.encode('utf-8'), contraseña_hash.encode('utf-8')):
                return True, rol
        return False, None

def insertar_resumen_diario(conn, datos):
    with conn.cursor() as cur:
        cur.execute("""
            INSERT INTO resumen_diario (
                fecha, 
                transparente_bajo, transparente_medio, transparente_alto, 
                verde_bajo, verde_medio, verde_alto, 
                azul_bajo, azul_medio, azul_alto, 
                pead_total, pebd_total, no_clasificadas_total)
            VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
            ON CONFLICT (fecha) DO UPDATE SET
                transparente_bajo = EXCLUDED.transparente_bajo,
                transparente_medio = EXCLUDED.transparente_medio,
                transparente_alto = EXCLUDED.transparente_alto,
                verde_bajo = EXCLUDED.verde_bajo,
                verde_medio = EXCLUDED.verde_medio,
                verde_alto = EXCLUDED.verde_alto,
                azul_bajo = EXCLUDED.azul_bajo,
                azul_medio = EXCLUDED.azul_medio,
                azul_alto = EXCLUDED.azul_alto,
                pead_total = EXCLUDED.pead_total,
                pebd_total = EXCLUDED.pebd_total,
                no_clasificadas_total = EXCLUDED.no_clasificadas_total;
        """, (
            datos['fecha'],
            datos['detalles']['transparente']['bajo'],
            datos['detalles']['transparente']['medio'],
            datos['detalles']['transparente']['alto'],
            datos['detalles']['verde']['bajo'],
            datos['detalles']['verde']['medio'],
            datos['detalles']['verde']['alto'],
            datos['detalles']['azul']['bajo'],
            datos['detalles']['azul']['medio'],
            datos['detalles']['azul']['alto'],
            datos['pead_total'],
            datos['pebd_total'],
            datos['no_clasificadas_total']
        ))
        conn.commit()


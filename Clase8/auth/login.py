from .connection import get_connection

def is_authenticated(usuario, password):
    conn, cur = get_connection()
    consulta = f"SELECT username, password FROM usuarios WHERE username=\'{usuario}\' AND password = \'{password}\';"

    cur.execute(consulta)
    usuario_encontrado = cur.fetchone()

    result = None
    if usuario_encontrado:
        result = usuario_encontrado
        
    cur.close()
    conn.close()

    return result
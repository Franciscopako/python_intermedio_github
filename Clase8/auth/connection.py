import psycopg2

def get_connection():
    conn = None
    cur = None 
    try:
        conn = psycopg2.connect("dbname=python_intermedio_db user=postgres password=root")
        cur = conn.cursor()
    except Exception as e:
        print(e)
    
    return conn, cur
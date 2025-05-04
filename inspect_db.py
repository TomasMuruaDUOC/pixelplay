import sqlite3

def main():
    conn = sqlite3.connect('db.sqlite3')
    cursor = conn.cursor()

    # Listar tablas
    cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
    tables = cursor.fetchall()
    print("Tablas en la base de datos:")
    for table in tables:
        print(f"- {table[0]}")

    # Mostrar primeros 5 registros de cada tabla
    for table in tables:
        print(f"\nPrimeros 5 registros de la tabla {table[0]}:")
        cursor.execute(f"SELECT * FROM {table[0]} LIMIT 5;")
        rows = cursor.fetchall()
        for row in rows:
            print(row)

    conn.close()

if __name__ == "__main__":
    main()

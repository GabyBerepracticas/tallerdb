import mysql.connector

conexion = mysql.connector.connect(
    host="127.0.0.1",
    user="root",
    password="mysql",
    database="db_taller"
)

cursor = conexion.cursor()
print(" Conexión exitosa a MySQL")


def insertar_linea(clave, nombre):
    query = "INSERT INTO LineaIn (clave, nombre) VALUES (%s, %s)"
    valores = (clave, nombre)
    cursor.execute(query, valores)
    conexion.commit()
    print(" Línea de investigación insertada correctamente.")


def leer_lineas():
    cursor.execute("SELECT * FROM LineaIn")
    for linea in cursor.fetchall():
        print(linea)

def actualizar_linea(clave, nuevo_nombre):
    query = "UPDATE LineaIn SET nombre = %s WHERE clave = %s"
    valores = (nuevo_nombre, clave)
    cursor.execute(query, valores)
    conexion.commit()
    print(" Línea de investigación actualizada.")


def eliminar_linea(clave):
    query = "DELETE FROM LineaIn WHERE clave = %s"
    valores = (clave,)
    cursor.execute(query, valores)
    conexion.commit()
    print(" Línea de investigación eliminada.")


insertar_linea(1, "prueva 1")
leer_lineas()
actualizar_linea(1, "prueva2")
leer_lineas()
eliminar_linea(1)
leer_lineas()

cursor.close()
conexion.close()
print(" Conexión cerrada.")
import mysql.connector

def conectar():
    return mysql.connector.connect(
         host="127.0.0.1",
         user="root",
         password="mysql",
         database="db_taller"
    )

def crear_profesor(clave, nombre):
    conexion = conectar()
    cursor = conexion.cursor()
    sql = "INSERT INTO Profesor (clave, nombre) VALUES (%s, %s)"
    valores = (clave, nombre)
    cursor.execute(sql, valores)
    conexion.commit()
    print("Profesor agregado correctamente.")
    cursor.close()
    conexion.close()

def leer_profesores():
    conexion = conectar()
    cursor = conexion.cursor()
    sql = "SELECT * FROM Profesor"
    cursor.execute(sql)
    profesores = cursor.fetchall()
    for profesor in profesores:
        print(profesor)
    cursor.close()
    conexion.close()

def actualizar_profesor(clave, nuevo_nombre):
    conexion = conectar()
    cursor = conexion.cursor()
    sql = "UPDATE Profesor SET nombre = %s WHERE clave = %s"
    valores = (nuevo_nombre, clave)
    cursor.execute(sql, valores)
    conexion.commit()
    print("Profesor actualizado correctamente.")
    cursor.close()
    conexion.close()

def eliminar_profesor(clave):
    conexion = conectar()
    cursor = conexion.cursor()
    sql = "DELETE FROM Profesor WHERE clave = %s"
    valores = (clave,)
    cursor.execute(sql, valores)
    conexion.commit()
    print("Profesor eliminado correctamente.")
    cursor.close()
    conexion.close()

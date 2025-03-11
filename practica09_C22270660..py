import mysql.connector

class TipoProyectoCRUD:
    def __init__(self):
        self.conn = mysql.connector.connect(
            host="127.0.0.1",
            user="root",
            password="mysql",
            database="db_taller"
        )
        self.cursor = self.conn.cursor()

    def crear_tipo_proyecto(self, id_tipo, nombre):
        sql = "INSERT INTO tipo_proyecto (id_tipo, nombre) VALUES (%s, %s)"
        valores = (id_tipo, nombre)
        self.cursor.execute(sql, valores)
        self.conn.commit()
        print("Tipo de proyecto creado correctamente.")

    def leer_tipos_proyecto(self):
        self.cursor.execute("SELECT * FROM tipo_proyecto")
        tipos = self.cursor.fetchall()
        for tipo in tipos:
            print(tipo)

    def actualizar_tipo_proyecto(self, id_tipo, nuevo_nombre):
        sql = "UPDATE tipo_proyecto SET nombre = %s WHERE id_tipo = %s"
        valores = (nuevo_nombre, id_tipo)
        self.cursor.execute(sql, valores)
        self.conn.commit()
        print("Tipo de proyecto actualizado correctamente.")

    def eliminar_tipo_proyecto(self, id_tipo):
        sql = "DELETE FROM tipo_proyecto WHERE id_tipo = %s"
        valores = (id_tipo,)
        self.cursor.execute(sql, valores)
        self.conn.commit()
        print("Tipo de proyecto eliminado correctamente.")

    def cerrar_conexion(self):
        self.cursor.close()
        self.conn.close()

if __name__ == "__main__":
    crud = TipoProyectoCRUD()
    
    crud.crear_tipo_proyecto(1, "Investigación")

    print("Lista de tipos de proyecto:")
    crud.leer_tipos_proyecto()

    crud.actualizar_tipo_proyecto(1, "Desarrollo de Software")

    crud.leer_tipos_proyecto()

    crud.eliminar_tipo_proyecto(1)

    crud.cerrar_conexion()

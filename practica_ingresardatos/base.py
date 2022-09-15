import sqlite3

class Base():

    #Funciona OK
    def dameConexion():
        conexion = sqlite3.connect("practica_ingresardatos\databaseEmpleado.sqlite")
        return conexion

    #Funciona OK
    def crearEmpleadoBase(nombre, apellido, edad, dni, sector, puesto):
        conexion = Base.dameConexion()
        cursor = conexion.cursor()
        list_empleado = [nombre, apellido, edad, dni, sector, puesto]
        cursor.execute(f"INSERT INTO empleados VALUES(?,?,?,?,?,?)", list_empleado)
        conexion.commit()
        conexion.close()

    def modificarEmpleadoBase(dni):
        conexion = Base.dameConexion()
        cursor = conexion.cursor()
        cursor.execute(f"INSERT INTO empleados (dni) VALUES ({dni});")
        conexion.commit()
        conexion.close()

    #Funciona OK
    def borrarEmpleadoBase():
        conexion = Base.dameConexion()        
        cursor = conexion.cursor()
        try:
            dni = int(input("Ingresar dni de la persona: \n"))
        except:
            print("\nEl dni debe tener solo numeros!, por favor ingresar nuevamente... \n")
        cursor.execute(f"DELETE FROM empleados WHERE dni ={dni};")
        conexion.commit()
        conexion.close()

    #Funciona OK
    def borrarEmpleadosBase():
        conexion = Base.dameConexion()        
        cursor = conexion.cursor()
        cursor.execute(f"DELETE FROM empleados;")
        conexion.commit()
        conexion.close()
    
    #Funciona OK
    def mostrarEmpleadoBase():
        conexion = Base.dameConexion() 
        cursor = conexion.cursor()
        try:
            dni = int(input("Ingresar dni de la persona: \n"))
        except:
            print("\nEl dni debe tener solo numeros!, por favor ingresar nuevamente... \n")
        cursor.execute(f"SELECT * FROM empleados WHERE dni ={dni};")
        empleado = cursor.fetchall()
        print(f"{empleado}")
        conexion.close()

    #Funciona OK
    def mostrarEmpleadosBase():
        conexion = Base.dameConexion() 
        cursor = conexion.cursor()
        cursor.execute(f"SELECT * FROM empleados;")
        empleados = cursor.fetchall()
        for e in empleados:
            print(e)
        conexion.close()
import os
from empleado import Empleado
from base import Base

while(True):

    print("------------MENU-----------")
    print("1-INGRESAR NUEVO EMPLEADO--")
    print("2-MODIFICAR EMPLEADO-------")
    print("3-BORRAR EMPLEADO----------")
    print("4-BORRAR EMPLEADOS---------")
    print("5-MOSTRAR EMPLEADO---------")
    print("6-MOSTRAR EMPLEADOS--------")
    print("0-SALIR--------------------")

    opcion = input("\n--INGRESAR OPCION DESEADA--\n")

    if(opcion=="1"):
        empleadoNuevo = Empleado.crearEmpleado()
        empleadoNuevo.mostrarEmpleado()
    elif(opcion=="2"):
        while(True):
            print("------------MENU-----------")
            print("1-NOMBRE-------------------")
            print("2-APELLIDO-----------------")
            print("3-EDAD---------------------")
            print("4-DNI----------------------")
            print("5-SECTOR-------------------")
            print("6-PUESTO-------------------")
            print("0-SALIR--------------------")
            
            opcionMod = input("\n--INGRESAR OPCION DESEADA--\n")
            
            if(opcionMod=="1"):
                pass
            elif(opcionMod=="2"):
                pass
            elif(opcionMod=="3"):
                pass
            elif(opcionMod=="4"):
                pass
            elif(opcionMod=="5"):
                pass
            elif(opcionMod=="6"):
                pass
    elif(opcion=="3"):
        Base.borrarEmpleadoBase()
    elif(opcion=="4"):
        Base.borrarEmpleadosBase()
    elif(opcion=="5"):
        Base.mostrarEmpleadoBase() 
    elif(opcion=="6"):
        Base.mostrarEmpleadosBase()
    elif(opcion=="0"):
        os.close()
from persona import Persona
from base import Base
#from ingresoDatos import IngresoDatos as ingd

class Empleado(Persona):
    def __init__(self, nombre, apellido, edad, dni, sector, puesto):
        self.nombre = nombre
        self.apellido = apellido
        self.edad = edad
        self.dni = dni
        self.sector = sector
        self.puesto = puesto

    def crearEmpleado():
        try:
            nombre = str(input("Ingresar nombre de la persona: \n"))
            #nombre = nombre.casefold
            #ingd.stringSoloLetras(nombre)
        except:
            print("\nEl nombre debe tener solo letras!, por favor ingresar nuevamente... \n")
        try:
            apellido = str(input("Ingresar apellido de la persona: \n"))
            #ingd.stringSoloLetras(apellido)
        except:
            print("\nEl apellido debe tener solo letras!, por favor ingresar nuevamente... \n")
        try:
            #while(edad < 0 & edad < 120):
            edad = int(input("Ingresar edad de la persona: \n"))
            #    if(edad > 0 & edad < 120):
            #        print("La edad debe ser mayor a 0 y menos a 120!, por favor ingresar nuevamente...")
        except:
            print("\nLa edad debe tener solo numeros!, por favor ingresar nuevamente... \n")
        try:
            dni = int(input("Ingresar dni de la persona: \n"))
        except:
            print("\nEl dni debe tener solo numeros!, por favor ingresar nuevamente... \n")
        try:    
            sector = str(input("Ingresar sector de la persona: \n"))
            #ingd.stringSoloLetras(sector)
        except:
            print("\nEl sector debe tener solo letras!, por favor ingresar nuevamente... \n")
        try:    
            puesto = str(input("Ingresar puesto de la persona: \n"))
            #ingd.stringSoloLetras(puesto)
        except:        
            print("\nEl puesto debe tener solo letras!, por favor ingresar nuevamente... \n")
        #Creacion del empleado
        empleadoNuevo = Empleado(nombre, apellido, edad, dni, sector, puesto)
        Base.crearEmpleadoBase(nombre, apellido, edad, dni, sector, puesto)
        print("Persona ingresada al sistema correctamente...\n")
        return empleadoNuevo

    def mostrarEmpleado(empleadoNuevo):
        print(f"El empleado nuevo que se creo es...")
        print(f"Nombre y apellido: \n{empleadoNuevo.nombre} {empleadoNuevo.apellido}\nedad: \n{empleadoNuevo.edad}\ndni: \n{empleadoNuevo.dni}")
        print(f"Sector y puesto: \n{empleadoNuevo.sector} {empleadoNuevo.puesto}")

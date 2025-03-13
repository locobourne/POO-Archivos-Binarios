# Una empresa de alquiler de autos necesita gestionar los datos de los vehículos de su flota. De cada vehículo se
# conoce: El identificador del vehículo (un entero positivo), el tamaño del vehículo (1: Subcompacto, 2: Compacto,
# 3: Mediano, 4: Grande), el tipo de motor (0: Nafta, 1: Gasoil, 2: GNC, 3: Eléctrico, 4: Hidrógeno) y el costo de
# alquiler por día. Se pide definir el tipo Vehiculo y desarrollar un programa en Python controlado por un menú de
# opciones, que permita gestionar las siguientes tareas:

class Vehiculos:
    def __init__(self, identificador, tamanio, motor, costo):
        self.identificador = identificador
        self.tamanio = tamanio
        self.motor = motor
        self.costo = costo

    def __str__(self):
        tamanios = ('Cubcompacto (ID 1)', 'Compacto (ID 2)', 'Mediano (ID 3)' , 'Grande (ID 4)')
        motores = ('Nafta (ID 0)', 'Gasoil (ID 1)', 'GNC (ID 2)', 'Eléctrico (ID 3)','Hidrógeno (ID 4)')
        return 'Identificador: ' + str(self.identificador) + ' | Tamaño: ' + tamanios[self.tamanio-1] + ' | Motor: ' + motores[self.motor] + ' | Costo: $' + str(self.costo)
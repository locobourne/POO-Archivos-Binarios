# Una concesionaria de autos usados necesita un programa que permita llevara cabo sus operaciones.
# De cada Operación se conoce código, nombre de comprador, monto de venta, marca (un valor que va del 1 al 15) y el año del modelo,
# la empresa solo trabaja con modelos de los úlitmos 22 años. Mediante la creación de un menú de opciones usted debe:

class Consesionaria:
    def __init__(self, codigo, nombre, monto, marca, anio):
        self.codigo = codigo
        self.nombre = nombre
        self.monto = monto
        self.marca = marca
        self.anio = anio


    def __str__(self):
        return 'Codigo: ' + str(self.codigo) + ' | Comprador: ' + str(self.nombre) + ' | Monto: ' + str(self.monto) \
            + ' | Marca: ' + str(self.marca) + ' | Año: ' + str(self.anio)

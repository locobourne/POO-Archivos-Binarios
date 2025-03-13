import os.path
import random
import pickle
from alquiler_vehiculos_class import *
random.seed(1010)

# 1. Cargar un arreglo de registros con los datos de n vehículos (cargar n por teclado y validar que sea positivo),
# de manera que en todo momento el arreglo se mantenga ordenado por identificador. Para esto debe utilizar
# el algoritmo de inserción ordenada con búsqueda binaria (se considerará directamente incorrecta la solución
# basada en cargar el arreglo completo y ordenarlo al final, o aplicar el algoritmo de inserción ordenada pero
# con búsqueda secuencial). Puede hacer la carga en forma manual, o puede generar los datos en forma
# automática (con valores aleatorios). Pero si hace carga manual, TODA la carga debe ser manual y validada, y si
# la hace automática entonces TODA debe ser automática y con base aleatoria.

# 2. Mostrar todos los vehículos del arreglo, a razón de un registro por línea, pero reemplazando el tamaño del
# vehículo por su descripción, y el tipo de motor también por su descripción.

# 3. Buscar un vehículo por identificador. Si existe mostrar todos sus datos y si, además, el tipo de motor es GNC,
# Eléctrico o Hidrógeno entonces mostrar el mensaje “Opción ecológica!”. Si el vehículo no existe informar con
# un mensaje.

# 4. A partir del arreglo genere un archivo binario que contenga los datos de todos los vehículos medianos o
# grandes que la empresa tiene en su flota.

# 5. Mostrar el archivo generado en el punto anterior indicando, al final, cuál es el costo promedio de alquiler de
# los autos eléctricos que se encontraban en el archivo.

def menu():
    print('1. Cargar arreglo')
    print('2. Mostrar todos los vehiculos')
    print('3. Buscar por ID')
    print('4. Generar binario')
    print('5. Mostrar binario y promedio')
    print('6. Salir')

def validar_mayor_a_cero():
    n = int(input('Ingrese una cantidad mayor a 0: '))
    while n <= 0:
        n = int(input('ERROR!!! Ingrese una cantidad mayor a 0: '))
    return n

def cargar_vec(vec):
    n = validar_mayor_a_cero()
    for i in range(n):
        identificador = random.randint(100, 900)
        tamanio = random.randint(1, 4)
        motor = random.randint(0 , 4)
        costo = round(random.uniform(10000, 200000),2)
        x = Vehiculos(identificador, tamanio, motor, costo)
        add_in_order(vec, x)

def add_in_order(vec, x):
    pos = len(vec)
    # Se inicia una búsqueda binaria para determinar la
    # posición de inserción
    izq = 0
    der = len(vec) -1
    # Mientras no se crucen los índices...
    while izq <= der:
        c = (izq + der) // 2
        if x.identificador == vec[c].identificador:
            # Si se encontró un elemento con el mismo nombre, entonces
            # la posición de inserción es la misma
            pos = c
            break

        if x.identificador > vec[c].identificador:
            izq = c + 1
        else:
            der = c - 1

    if izq > der:
        # Si no hay un contenido con el mismo nombre, la posición
        # de inserción es izq
        pos = izq
    # Se inserta el contenido en el vector.
    # ATENCIÓN: Si esta inserción se hace dentro del if anterior, entonces
    # no se aceptan repetidos
    vec[pos:pos] = [x]


def busqueda_binaria(vec,x):
    pos = None
    izq = 0
    der = len(vec) -1
    while izq <= der:
        c = (izq + der) // 2
        if x == vec[c].identificador:
            pos = c
            break
        if x > vec[c].identificador:
            izq = c + 1
        else:
            der = c - 1
    if pos is None:
        return None
    return vec[pos]

# 3-	Buscar en el arreglo creado en el punto 1 un registro en el cual el número de identificación del artículo
# sea igual a num (cargar num por teclado).  Si existe, mostrar por pantalla todos los datos de ese registro.
# Si no existe, informar con un mensaje. La búsqueda debe detenerse al encontrar el primer registro que coincida
# con el patrón pedido.
# busqueda unica, binaria
def buscar_numero(vec, num):
    n = len(vec)
    # cuando la busqueda falle
    pos = None
    iz = 0    # primer elemento del vector
    de = n-1  # ultimo elemento del vector

    while iz <= de:
        # buscar el valor central
        c = (iz + de) // 2
        if vec[c].numero == num:
            pos = c
            break
        elif num > vec[c].numero:
            # mover a la izquierda
            de = c - 1
        else:
            # mover a la derecha
            iz = c + 1
    if pos is None:
        print("No se encontro el articulo buscado")
    else:
        print("Los datos del articulo encontrado son: ", vec[pos])

def mostrar_vec(vec):
    for i in vec:
        print(i)



def punto_2(vec):
    # 2. Mostrar todos los vehículos del arreglo, a razón de un registro por línea, pero reemplazando el tamaño del
    # vehículo por su descripción, y el tipo de motor también por su descripción.
    # el tamaño del vehículo(1: Subcompacto, 2: Compacto, 3: Mediano, 4: Grande)
    # el tipo de motor(0: Nafta, 1: Gasoil, 2: GNC, 3: Eléctrico, 4: Hidrógeno)
    # desc_tam = None
    # desc_motor = None
    for i in vec:
        print(i)
    #     if i.tamanio == 1:
    #         desc_tam = "Subcompacto"
    #     elif i.tamanio == 2:
    #         desc_tam = "Compacto"
    #     elif i.tamanio == 3:
    #         desc_tam = "Mediano"
    #     elif i.tamanio == 4:
    #         desc_tam = "Grande"
    #
    #     if i.motor == 0:
    #         desc_motor = 'Nafta'
    #     elif i.motor == 1:
    #         desc_motor = 'Gasoil'
    #     elif i.motor == 2:
    #         desc_motor = 'GNC'
    #     elif i.motor == 3:
    #         desc_motor = 'Eléctrico'
    #     elif i.motor == 4:
    #         desc_motor = 'Hidrógeno'

        #print('Identificador: ' + str(i.identificador) + ' | Tamaño: ' + desc_tam + ' | Motor: ' + desc_motor + ' | Costo: $' + str(i.costo))

def punto_3(vec):
    # 3. Buscar un vehículo por identificador. Si existe mostrar todos sus datos y si, además, el tipo de motor es GNC,
    # Eléctrico o Hidrógeno entonces mostrar el mensaje “Opción ecológica!”. Si el vehículo no existe informar con
    # un mensaje.
    x = int(input('Ingrese el ID a buscar: '))
    vehiculo = busqueda_binaria(vec, x)
    if vehiculo is None:
        print('No se encontro ningun vehiculo.')
    else:
        print(vehiculo)
        if vehiculo.motor == 2 or vehiculo.motor == 3 or vehiculo.motor == 4:
            print('Opción ecológica!')

def punto_4(vec, archivo):
    # 4. A partir del arreglo genere un archivo binario que contenga los datos de todos los vehículos medianos o
    # grandes que la empresa tiene en su flota.
    m = open(archivo, 'wb')
    for e in vec:
        if e.tamanio == 3 or e.tamanio == 4:
            pickle.dump(e, m)
    m.close()
    print('El archivo binario fue cargado con exito!')

def punto_5(archivo):
    # 5. Mostrar el archivo generado en el punto anterior indicando, al final, cuál es el costo promedio de alquiler de
    # los autos eléctricos que se encontraban en el archivo.
    acumm = 0
    contador = 0
    prom = 0
    if not os.path.exists(archivo):
        print('No se encontro el archivo.')
    else:
        m = open(archivo, 'rb')
        t = os.path.getsize(archivo)
        while m.tell() < t:
            e = pickle.load(m)
            print(e)
            acumm += e.costo
            contador += 1
        m.close()
        if prom == 0:
            prom = acumm / contador
            print('El costo promedio es de: $',round(prom, 2))
        else:
            print('Error')


def main():
    vec = []
    op = 0
    archivo = 'alquiler_vehiculos.dat'
    while op != 6:
        menu()
        op = int(input('Seleccione su opcion: '))
        if op == 1:
            cargar_vec(vec)
            mostrar_vec(vec)

        if op == 2:
            if vec == []:
                print('Primero debe cargar el vector')
            else:
                punto_2(vec)


        if op == 3:
            if vec == []:
                print('Primero debe cargar el vector')
            else:
                punto_3(vec)

        if op == 4:
            if vec == []:
                print('Primero debe cargar el vector')
            else:
                punto_4(vec, archivo)

        if op == 5:
            punto_5(archivo)

        if op == 6:
            print('Hasta luego...')


if __name__ == '__main__':
    main()
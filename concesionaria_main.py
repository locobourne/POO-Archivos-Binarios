import os.path
import random
import pickle
from concesionaria_class import *
random.seed(1010)


# 1. Cargar un arreglo de n operaciones, el arreglo se debe generar ordenado en todo momento por el código de la operación.
# Tenga en cuenta que los códigos de operación deben ser únicos y debe permitir generar registros sin tener que
# perder los anteriores.
#
# 2. Mostrar todos los datos del arreglo, a razón de una fila por registro, y al final indicar cual fue el monto promedio de venta de las operaciones.
#
# 3. Determinar la cantidad de operaciones que se realizaron por modelo y año, mostrar solo aquellos que son mayores a cero.
#
# 4. Buscar en el arreglo la primera operación que encuentre con el nombre del comprador nom pasado por parámetro,
# si existe incrementar el monto de venta en un porcentaje x pedido por teclado y mostrar sus datos, si no existe indicar
# con un mensaje.
#
# 5. Generar un archivo binario 'concesionaria_operaciones.dat' con todos aquellos registros cuyo monto de venta sea mayor al promedio de ventas de las operaciones realizadas.
#
# 6. Mostrar el archivo generado en el punto anterior, a razón de uno por línea, indicando al final la cantidad de registros que se mostraron.



def menu():
    print('1. Cargar arreglo y verificar repetidos')
    print('2. Mostrar areglo y promedio')
    print('3. Determinar cantidad de operaciones')
    print('4. Buscar en el arreglo')
    print('5. Generar archivo binario')
    print('6. Mostrar binario')
    print('7. Salir')

def validar_mayor_a_cero():
    n = int(input('Ingrese una cantidad mayor a 0: '))
    while n <= 0:
        n = int(input('ERROR!!! Ingrese una cantidad mayor a 0: '))
    return n

def add_in_order(vec, x):
    izq = 0
    der = len(vec) -1
    pos = len(vec)
    while izq <= der:
        c = (izq + der) // 2
        if x.codigo == vec[c].codigo:
            pos = c
            break
        if x.codigo > vec[c].codigo:
            izq = c + 1
        else:
            der = c - 1

    if izq > der:
        pos = izq
    vec[pos:pos] = [x]

def busqueda_binaria(vec, codigo):
    izq = 0
    der = len(vec) - 1
    pos = -1
    while izq <= der:
        c = (izq + der) // 2
        if codigo == vec[c].codigo:
            pos = c
            break
        if codigo > vec[c].codigo:
            izq = c + 1
        else:
            der = c - 1
    return pos

def existe(vec, codigo):
    pos = busqueda_binaria(vec, codigo)
    return pos >= 0

def bucle_codigo(vec):
    codigo = random.randint(1,10000)
    while existe(vec, codigo):
        codigo = random.randint(10000, 100000)
        print('El codigo se encuentra en uso, buscando uno nuevo...')
    return codigo

def cargar_vec(vec):
    n = validar_mayor_a_cero()
    for i in range(n):
        codigo = bucle_codigo(vec)
        nombre = 'Nombre ' + str(i)
        monto = round(random.uniform(1000, 15000), 2)
        marca = random.randint(1, 15)
        modelo = random.randint(2000, 2022)
        x = Consesionaria(codigo, nombre, monto, marca, modelo)
        add_in_order(vec, x)

def mostrar_vec(vec):
    for i in vec:
        print(i)

def punto_2(vec):
    # 2. Mostrar todos los datos del arreglo, a razón de una fila por registro, y al final indicar cual fue el monto promedio de venta de las operaciones.
    accum = 0
    cont = 0
    prom = 0
    for i in vec:
        accum += i.monto
        cont += 1
        print(i)
    if accum == 0 or cont == 0:
        print('Error')
    else:
        prom = round(accum / cont, 2)
        print('El monto promedio de venta de las operaciones fue de: ', prom)

def punto_3(vec):
#3. Determinar la cantidad de operaciones que se realizaron por modelo y año, mostrar solo aquellos que son mayores a cero.
    mat = [[0] * 23 for f in range(15)]
    #      COLUMNAS  ----- FILAS
    for i in vec:
        f = i.marca - 1
        c = i.anio - 2000
        mat[f][c] += 1
    return mat

def mostrar_matriz(mat):
    cont = 0
    for f in range(len(mat)):
        for c in range(len(mat[f])):
            if mat[f][c] > 0:
                print('Hay', mat[f][c], 'operaciones de la marca', f + 1, 'Y el modelo', c + 2000 )
                cont += 1
    print(cont)

def punto_4(vec, nom):
    # 4. Buscar en el arreglo la primera operación que encuentre con el nombre del comprador nom pasado por parámetro,
    # si existe incrementar el monto de venta en un porcentaje x pedido por teclado y mostrar sus datos, si no existe indicar
    # con un mensaje.
    pos = -1
    for i in range(len(vec)): #Iteramos por indice en vez de por objeto
        if nom == vec[i].nombre:
            pos = i
            break
    return pos

def obtener_promedio(vec):
    cont = 0
    accum = 0
    for i in vec:
        accum += i.monto
        cont += 1
    promedio = round(accum / cont, 2)
    return promedio

def punto_5(vec):
    # 5. Generar un archivo binario 'concesionaria_operaciones.dat' con todos aquellos registros
    # cuyo monto de venta sea mayor al promedio de ventas de las operaciones realizadas.
    archivo = 'concesionaria_operaciones.dat'
    promedio = obtener_promedio(vec)
    m = open(archivo, 'wb')
    for i in vec:
        if i.monto > promedio:
            pickle.dump(i, m)
    print('El binario fue cargado con exito!')
    m.close()

def punto_6(archivo):
    if not os.path.exists(archivo):
        print('No existe el archivo')
        return
    m = open(archivo, 'rb')
    t = os.path.getsize(archivo)
    cant = 0
    while m.tell() < t:
        obj = pickle.load(m)
        cant += 1
        print(obj)
    m.close()
    print('Se leyeron', cant, 'registros')


def main():
    vec = []
    op = 0
    while op != 7:
        menu()
        op = int(input('Ingrese su opcion: '))
        if op == 1:
            cargar_vec(vec)
            mostrar_vec(vec)

        if op == 2:
            if vec == []:
                print('El registro esta vacio.')
            else:
                punto_2(vec)

        if op == 3:
            if vec == []:
                print('El registro esta vacio.')
            else:
                mat = punto_3(vec)
                mostrar_matriz(mat)

        if op == 4:
            if vec == []:
                print('El registro esta vacio.')
            else:
                nom = input('Ingrese el nombre del comprador: ')
                pos = punto_4(vec, nom)
                if pos != -1:
                    x = validar_mayor_a_cero()
                    vec[pos].monto *= 1 + (x / 100) #Multiplicamos por 1 a la division de x y esto sera multipicado por vec.monto
                    print(vec[pos])
                else:
                    print('No se encontro')

        if op == 5:
            if vec == []:
                print('El registro esta vacio.')
            else:
                punto_5(vec)

        if op == 6:
            punto_6('concesionaria_operaciones.dat')

        if op == 7:
            print('Gracias por usar el programa...')




if __name__ == '__main__':
    main()
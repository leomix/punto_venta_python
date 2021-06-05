"""
Dada una tabla que contiene los artículos y precios de un negocio y cantidad de stock,
simular generar una factura de a lo sumo 6 artículos, en la cual el usuario solo debe
ingresar el artículo y la cantidad (revisar que el art. tenga stock). 
El programa debería calcular los subtotales y el total general de la factura.
"""
from tabulate import tabulate
import os

matriz = [
    ["Codigo","Artículos", "Precios", "Stock"],
    ["12","Celulares", 400, 20],
    ["13","Tablets", 500, 40],
    ["14","Sillas", 200, 200],
    ["15","Mesas", 500, 20],
    ["16","Kiwis", 30, 1000],
    ["17","Manzanas", 15, 0],
    ["18","Peras", 12, 5]
]

carrito = [
    ["Codigo","Artículo", "Precio", "Stock", "Subtotal"],
]

def main():
    
    cls()
    while(True):
        if(len(carrito)>1):
            imprimir("carrito")

        imprimir("inventario")
        imprimir("menu")
        opcion = input(" Elige Opción: ")

        if opcion.isnumeric():
            if opcion == "1":
                ingresarOpcion()
                
            elif opcion == "2":
                removeOpcion()

            elif opcion == "3":
                terminarCompra()

            elif opcion == "4":
                break

            else:
                cls()
                print("Ingresa una opción correcta.")
        else:
            cls()
            print("Ingresa una opción correcta.")

def cls():
    os.system('cls' if os.name=='nt' else 'clear')


def ingresarOpcion():
    articulo = input("Ingresar Código Del Artículo: ")
    if not articulo:
        cls()
        print("No puedes ingresar un codigo en blanco")
        return False

    else:
        get_articulo = getArticulo(articulo,matriz)
        if(not get_articulo):
            cls()
            print("Debes ingresar un codigo válido")
            return False

        else:
            cantidad = int(input("Ingresar cantidad: "))
            if cantidad > 0:
                addToCarrito(articulo,cantidad)
                    
            else:
                cls()
                print("Ingresa una cantidad mayor que cero")
                return False

def getArticulo(articulo,lista):
    o = len(lista)
    result = False
    for fila in range(1, o):
        if lista[fila][0] == articulo:
            result = fila
    return result

def addToCarrito(articulo,cantidad):
    for fila in range(1, len(matriz)):
        if matriz[fila][0] == articulo:
            if matriz[fila][3] >= cantidad:
                matriz[fila][3] -= cantidad
                get_articulo = getArticulo(articulo,carrito)
                if(get_articulo):
                    carrito[get_articulo][3]+=cantidad
                else:
                    carrito.append(
                        [matriz[fila][0],
                        matriz[fila][1],
                        matriz[fila][2],
                        cantidad,
                        matriz[fila][2] * cantidad
                        ]
                    )
                cls()
                print("Artículo agregado correctamente")
            else:
                cls()
                print("El stock es menor que la cantidad, no se puede vender.")

def removeOpcion():
    if len(carrito) > 1:
        articulo = input("Ingresar Código Del Artículo A Eliminar: ")
        get_articulo = getArticulo(articulo,carrito)
        if(not get_articulo):
            cls()
            print("Este codigo no esta en el carrito")
            return False
        else:
            cantidad = input("Que Cantidad quieres eliminar")
            cantidad_carrito = carrito[get_articulo][3]
            if not cantidad or int(cantidad) >= cantidad_carrito:
                carrito.pop(get_articulo)
            else:
                carrito[get_articulo][3] -=int(cantidad)
            cls()
            print("Articulo(s) eliminados del carrito")
    else:
        cls()
        print("No hay elementos en carrito que eliminar")

def terminarCompra():
    if len(carrito) > 1:
        total = 0
        for producto in range(1, len(carrito)):
            total += carrito[producto][4]
        cls()
        continuar =  input("El total es: $"+ str(total) +".00 ¿Deseas terminar la compra?")
        if continuar and str.lower(continuar) == "si":
            for row in range(1,len(carrito)):
                carrito.pop()
            print("Gracias por tu compra")

    else:
        cls()
        print("El carrito no tiene productos, no se puede vender nada.")

def imprimir(tipo):
    if tipo == "carrito":
        print("""
--- Carrito ---

"""+tabulate(carrito, headers='firstrow'))

    elif tipo == "inventario":
        print("""
--- Inventario ---

"""+tabulate(matriz, headers='firstrow'))

    else:
        print(""" 
        
        [1] Agregar Artículo Al Carrito
        [2] Eliminar Articulo(s) De Carrito
        [3] Finalizar Compra
        [4] Salir
        """)

if __name__ == '__main__':
    main()
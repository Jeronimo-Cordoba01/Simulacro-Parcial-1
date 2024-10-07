"""
Jerónimo F.L. Córdoba
Modelos de Parcial: Programación I
Enunciado:
Gestión de Inventario
La Empresa “Empire Inventory” necesita desarrollar un sistema de administración de productos para sus almacenes. 
Para cada producto se almacenará:
    • Nombre del producto.
    • Precio del producto.
    • Cantidad del producto.
La información de los productos se almacenará en un arreglo bidimensional, donde cada fila
representara un producto y las columnas contendrán los datos mencionados.
Requerimientos:
El sistema deberá constar de los siguientes puntos:
    1. Menú Principal: Mostrar un menú con las siguientes opciones disponibles:
        • Cargar producto/s.
        • Buscar producto.
        • Ordenar inventario.
        • Mostrar producto más caro y más barato.
        • Mostrar productos con precio mayor a 15000.
        • Salir
    2. Cargar inventario:
        • Desarrollar una función que permita al usuario ingresar los datos del o los productos en una matriz (nombre, precio, cantidad).
        • El sistema debe permitir al usuario ingresar la cantidad deseada de productos.
    3. Buscar producto:
        • Implementar un algoritmo de búsqueda que permita al usuario encontrar un producto específico por su nombre y muestre por pantalla 
        todos los datos de ese producto (nombre, precio y cantidad).
    4. Ordenar inventario:
        • Utilizar un algoritmo de ordenamiento para ordenar los productos en función
        de su precio de manera ascendente y luego mostrar por pantalla los productos
        ordenados.
    5. Mostrar producto más caro:
        • Desarrollar una función que identifique y muestre el producto más caro del inventario.
    6. Mostrar producto más barato:
        • Desarrollar una función que identifique y muestre el producto más barato del inventario.
    Requisitos técnicos:
    ▪ Utilizar funciones para cada una de las operaciones mencionadas.
    ▪ Mantener una estructura de código limpia y bien comentada.
    ▪ Si el usuario selecciona cualquier opción sin que existan productos registrados en el sistema, aparecerá un mensaje en pantalla 
    notificando que no hay productos disponibles para la operación solicitada.
"""

from Modelo import *

def Opciones():
    """
    Función que imprime las opciones del menú principal.
    """
    print("\n--- Bienvenidos al Himalaya --- \n"
        "1. Cargar producto/s \n"
        "2. Buscar producto \n"
        "3. Ordenar inventario \n"
        "4. Mostrar producto más caro y más barato \n"
        "5. Mostrar productos con precio mayor a 15000 \n"
        "6. Salir \n")
    
def menu():
    """
    Función principal que maneja la navegación por el menú.
    """
    while True:
        Opciones()
        opcion = input("Selecciona una opción: ")

        match opcion:
            case "1":
                cargar_producto(Inventario)
            case "2":
                buscar_producto(Inventario)
            case "3":
                ordenar_bubble_short(Inventario)
            case "4":
                mostrar_producto_mas_caro(Inventario)
                mostrar_producto_mas_barato(Inventario)
            case "5":
                producto_limite(Inventario, limite)
            case "6":
                print("Saliendo del programa...")
                break
            case _:
                print("Opción no válida. Intente de nuevo.")
                
menu()
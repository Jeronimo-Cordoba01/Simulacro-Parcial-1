Inventario = []

limite = 15000

def cargar_producto(Inventario):
    """
    Permite cargar productos en el inventario.

    Args:
        Inventario (list): La lista bidimensional que representa el inventario de productos.

    Operación:
        El usuario ingresa la cantidad de productos a cargar, seguido por el nombre, precio y cantidad de cada producto.
        Los productos se agregan como listas en el inventario.

    Returns:
        None
    """
    cantidad = int(input("¿Cuántos productos deseas cargar? "))  
    for i in range(cantidad):
        nombre = input("Ingresa el nombre del producto: ")
        precio = float(input("Ingresa el precio del producto: "))
        cantidad_producto = int(input("Ingresa la cantidad del producto: "))  
        Inventario.append([nombre, precio, cantidad_producto]) 

def buscar_producto(Inventario):
    """
    Busca un producto por su nombre dentro del inventario.

    Args:
        Inventario (list): La lista bidimensional que representa el inventario de productos.

    Operación:
        Se solicita al usuario ingresar el nombre del producto que desea buscar. 
        Si el producto existe, se muestran sus datos (nombre, precio, cantidad).
        Si el inventario está vacío o no se encuentra el producto, se muestra un mensaje.

    Returns:
        None
    """
    if not Inventario:
        print("No hay productos disponibles")
        return
    nombre = input("Ingresa el nombre del producto: ").lower()
    for i in range(len(Inventario)):
        if Inventario[i][0].lower() == nombre:
            print("Nombre:", Inventario[i][0])
            print("Precio:", Inventario[i][1])
            print("Cantidad:", Inventario[i][2])
            return
    print("No se encontro el producto")
    
def ordenar_bubble_short(Inventario):
    """
    Ordena el inventario de productos por su precio en orden ascendente usando el algoritmo de bubble sort.

    Args:
        Inventario (list): La lista bidimensional que representa el inventario de productos.

    Operación:
        Ordena las filas del inventario en función del precio del producto (columna índice 1).
        Se muestran los productos ordenados.

    Returns:
        list: El inventario ordenado por precio de manera ascendente.
    """
    for i in range(len(Inventario)):
        for j in range(len(Inventario) - i - 1):
            if Inventario[j][1] > Inventario[j + 1][1]:
                Inventario[j], Inventario[j + 1] = Inventario[j + 1], Inventario[j]
    print("Inventario ordenado por precio:")
    for producto in Inventario:
        print(producto)
    return Inventario

def mostrar_producto_mas_caro(Inventario):
    """
    Muestra el producto más caro del inventario.

    Args:
        Inventario (list): La lista bidimensional que representa el inventario de productos.

    Operación:
        Recorre el inventario y encuentra el producto con el precio más alto.
        Muestra por pantalla el nombre, precio y cantidad del producto más caro.

    Returns:
        None
    """
    if not Inventario:
        print("No hay productos disponibles")
        return
    producto_mas_caro = Inventario[0]
    for producto in Inventario:
        if producto[1] > producto_mas_caro[1]:
            producto_mas_caro = producto
    print("El producto más caro es:", producto_mas_caro)

def mostrar_producto_mas_barato(Inventario):
    """
    Muestra el producto más barato del inventario.

    Args:
        Inventario (list): La lista bidimensional que representa el inventario de productos.

    Operación:
        Recorre el inventario y encuentra el producto con el precio más bajo.
        Muestra por pantalla el nombre, precio y cantidad del producto más barato.

    Returns:
        None
    """
    if not Inventario:
        print("No hay productos disponibles")
        return
    producto_mas_barato = Inventario[0]
    for producto in Inventario:
        if producto[1] < producto_mas_barato[1]:
            producto_mas_barato = producto
    print("El producto más barato es:", producto_mas_barato)
    
def producto_limite(Inventario, limite):
    """
    Muestra los productos con un precio mayor al límite especificado.

    Args:
        Inventario (list): La lista bidimensional que representa el inventario de productos.
        limite (float): El precio límite a comparar.

    Operación:
        Recorre el inventario y muestra los productos cuyo precio es mayor que el valor de 'limite'.
        Si no hay productos en el inventario o no hay productos con un precio mayor al límite, muestra un mensaje.

    Returns:
        None
    """
    if not Inventario:
        print("No hay productos disponibles")
        return
    print("Los productos con precio mayor a", limite, "son:")
    for producto in Inventario:
        if producto[1] > limite:
            print(producto)
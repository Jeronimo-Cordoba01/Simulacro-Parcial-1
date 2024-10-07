Inventario = []

limite = 15000

def cargar_producto(Inventario):
    cantidad = int(input("¿Cuántos productos deseas cargar? "))  
    for i in range(cantidad):
        nombre = input("Ingresa el nombre del producto: ")
        precio = float(input("Ingresa el precio del producto: "))
        cantidad_producto = int(input("Ingresa la cantidad del producto: "))  
        Inventario.append([nombre, precio, cantidad_producto]) 

def buscar_producto(Inventario):
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
    for i in range(len(Inventario)):
        for j in range(len(Inventario) - i - 1):
            if Inventario[j][1] > Inventario[j + 1][1]:
                Inventario[j], Inventario[j + 1] = Inventario[j + 1], Inventario[j]
    print("Inventario ordenado por precio:")
    for producto in Inventario:
        print(producto)
    return Inventario

def mostrar_producto_mas_caro(Inventario):
    if not Inventario:
        print("No hay productos disponibles")
        return
    producto_mas_caro = Inventario[0]
    for producto in Inventario:
        if producto[1] > producto_mas_caro[1]:
            producto_mas_caro = producto
    print("El producto más caro es:", producto_mas_caro)

def mostrar_producto_mas_barato(Inventario):
    if not Inventario:
        print("No hay productos disponibles")
        return
    producto_mas_barato = Inventario[0]
    for producto in Inventario:
        if producto[1] < producto_mas_barato[1]:
            producto_mas_barato = producto
    print("El producto más barato es:", producto_mas_barato)
    
def producto_limite(Inventario, limite):
    if not Inventario:
        print("No hay productos disponibles")
        return
    print("Los productos con precio mayor a", limite, "son:")
    for producto in Inventario:
        if producto[1] > limite:
            print(producto)
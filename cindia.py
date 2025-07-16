# Diccionarios base con información de productos y stock
productos = {
    '8475HD': ['HP', 15.6, '8GB', 'DD', '1T', 'Intel Core i5', 'Nvidia GTX1050'],
    '2175HD': ['lenovo', 14, '4GB', 'SSD', '512GB', 'Intel Core i5', 'Nvidia GTX1050'],
    'JjfFHD': ['Asus', 14, '16GB', 'SSD', '256GB', 'Intel Core i7', 'Nvidia RTX2080Ti'],
    'fgdxFHD': ['HP', 15.6, '8GB', 'DD', '1T', 'Intel Core i3', 'integrada'],
    'GF75HD': ['Asus', 15.6, '8GB', 'DD', '1T', 'Intel Core i7', 'Nvidia GTX1050'],
    '123FHD': ['lenovo', 14, '6GB', 'DD', '1T', 'AMD Ryzen 5', 'integrada'],
    '342FHD': ['lenovo', 15.6, '8GB', 'DD', '1T', 'AMD Ryzen 7', 'Nvidia GTX1050'],
    'UWU131HD': ['Dell', 15.6, '8GB', 'DD', '1T', 'AMD Ryzen 3', 'Nvidia GTX1050'],
    'FS123OHD': ['Acer', 15.6, '4GB', 'SSD', '256GB', 'Intel Core i3', 'integrada']  # ← Acer agregado
}

# Diccionario con precio y cantidad disponible para cada modelo
stock = {
    '8475HD': [387990, 10],    # Precio, Stock
    '2175HD': [327990, 4],
    'JjfFHD': [424990, 1],
    'fgdxFHD': [664990, 21],
    '123FHD': [290890, 32],
    '342FHD': [444990, 7],
    'GF75HD': [749990, 2],
    'UWU131HD': [349990, 1],
    'FS123OHD': [249990, 0]  # Acer con 0 unidades
}

# Función para mostrar el stock disponible de notebooks de una marca específica
def stock_marca(nombre_marca):
    nombre_marca = nombre_marca.lower()  # Convertimos a minúsculas para comparar correctamente
    encontrado = False  # Bandera para saber si encontramos la marca

    for modelo, datos in productos.items():  # Recorremos todos los productos
        marca_actual = datos[0].lower()  # Marca del producto actual en minúsculas
        if marca_actual == nombre_marca:
            if modelo in stock:
                cantidad = stock[modelo][1]  # Tomamos el stock real
            else:
                cantidad = 0  # Si no hay stock registrado, se asume 0

            print(f"Modelo: {modelo} - Stock disponible: {cantidad}")
            encontrado = True

    if not encontrado:
        print("No hay notebooks de esa marca.")

# Función para buscar notebooks dentro de un rango de precios dado
def busqueda_por_precio(precio_minimo, precio_maximo):
    if precio_minimo > precio_maximo:
        print("Debe ingresar valores correctos!!!")
        return

    resultados = []  # Lista para guardar los resultados encontrados

    for modelo, datos_stock in stock.items():
        precio_actual, cantidad_disponible = datos_stock
        if precio_minimo <= precio_actual <= precio_maximo and cantidad_disponible > 0:
            marca_modelo = f"{productos[modelo][0]} - {modelo}"
            resultados.append(marca_modelo)

    if not resultados:
        print("No hay notebooks en ese rango de precios.")
    else:
        resultados.sort()  # Ordenamos alfabéticamente
        for resultado in resultados:
            print(resultado)

# Función para actualizar el precio de un modelo específico
def actualizar_precio_de_modelo(nombre_modelo, nuevo_precio):
    if nombre_modelo in stock:
        stock[nombre_modelo][0] = nuevo_precio
        return True
    else:
        return False

# Menú principal del programa
def mostrar_menu():
    while True:
        print("\n*** MENÚ PRINCIPAL ***")
        print("1. Stock por marca.")
        print("2. Búsqueda por precio.")
        print("3. Actualizar precio.")
        print("4. Salir.")

        opcion_elegida = input("Ingrese una opción (1-4): ").strip()

        if opcion_elegida == '1':
            nombre_marca = input("Ingrese la marca: ").strip()
            stock_marca(nombre_marca)

        elif opcion_elegida == '2':
            try:
                precio_minimo = int(input("Ingrese precio mínimo: ").strip())
                precio_maximo = int(input("Ingrese precio máximo: ").strip())
                busqueda_por_precio(precio_minimo, precio_maximo)
            except ValueError:
                print("Debe ingresar valores enteros!!!")

        elif opcion_elegida == '3':
            while True:
                nombre_modelo = input("Ingrese modelo: ").strip()
                try:
                    nuevo_precio = int(input("Ingrese nuevo precio: ").strip())
                except ValueError:
                    print("Debe ingresar un número válido para el precio.")
                    continue

                actualizado = actualizar_precio_de_modelo(nombre_modelo, nuevo_precio)
                if actualizado:
                    print("Precio actualizado!!")
                else:
                    print("El modelo no existe!!")

                respuesta = input("¿Desea actualizar otro precio? (si/no): ").strip().lower()
                if respuesta != "si":
                    break

        elif opcion_elegida == '4':
            print("Programa finalizado.")
            break

        else:
            print("Debe seleccionar una opción válida!!")

# Ejecutar el menú principal para iniciar el programa
mostrar_menu()

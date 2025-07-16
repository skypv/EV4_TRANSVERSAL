productos = {
    '8475HD': ['HP', 15.6, '8GB', 'DD', '1T', 'Intel Core i5', 'Nvidia GTX1050'],
    '2175HD': ['lenovo', 14, '4GB', 'SSD', '512GB', 'Intel Core i5', 'Nvidia GTX1050'],
    'JjfFHD': ['Asus', 14, '16GB', 'SSD', '256GB', 'Intel Core i7', 'Nvidia RTX2080Ti'],
    'fgdxFHD': ['HP', 15.6, '8GB', 'DD', '1T', 'Intel Core i3', 'integrada'],
    'GF75HD': ['Asus', 15.6, '8GB', 'DD', '1T', 'Intel Core i7', 'Nvidia GTX1050'],
    '123FHD': ['lenovo', 14, '6GB', 'DD', '1T', 'AMD Ryzen 5', 'integrada'],
    '342FHD': ['lenovo', 15.6, '8GB', 'DD', '1T', 'AMD Ryzen 7', 'Nvidia GTX1050'],
    'UWU131HD': ['Dell', 15.6, '8GB', 'DD', '1T', 'AMD Ryzen 3', 'Nvidia GTX1050'],
} #DICCIONARIO DE PRODUCTOS

stock = {
    '8475HD': [387990,10], '2175HD': [327990,4], 'JjfFHD': [424990,1],
    'fgdxFHD': [664990,21], '123FHD': [290890,32], '342FHD': [444990,7],
    'GF75HD': [749990,2], 'UWU131HD': [349990,1], 'FS1230HD': [249990,0], 
} #DICCIONARIO DE STOCK QUE CONTIENE LOS PRECIOS

def stock_marca (marca): #FUNCION PARA MOSTRAR EL STOCK TOTAL DE UNA MARCA
    total = 0
    for modelo in productos:   #COMPARA LA MARCA SIN IMPORTAR MAYUSCULA O MINUSCULA
        if productos [modelo][0].lower() == marca.lower():
            if modelo in stock:
                total += stock[modelo][1]    #SUMA EL STOCK DE ESE MODELO VERIFICANDOLO EN EL ANTERIOR
    print("Stock total de la marca", marca+":", total)

def busqueda_precios(precio_minimo, precio_maximo): #FUNCION PARA BUSCAR NOTEBOOKS EN UN RANGO DE PRECIOS
    lista = []
    for modelo in stock:
        precio = stock[modelo][0]
        cantidad = stock[modelo][1]
        if precio_minimo <= precio <= precio_maximo and cantidad > 0:
            marca = productos[modelo][0]
            lista.append(marca + "--" + modelo)
    if len(lista) == 0:
        print("No hay notebooks en ese rango de precios.")
    else:
        lista.sort()
        print("Modelos encontrados:")
        for item in lista:
            print(item)

def actualizar_precio(modelo, nuevo_precio): #FUNCION PARA ACTUALIZAR EL PRECIO DE UN MODELO
    if modelo in stock:
        stock[modelo][0] = nuevo_precio
        return True
    else:
        return False
    

while True: #CICLO PRINCIPAL DEL MENU
    print("\n*** MENU PRINCIPAL ***")
    print("1. stock marca.")
    print("2. Busqueda de precio.") 
    print("3. Actualizar precio.") 
    print("4. Salir.") 
    
    opcion =input("Seleccione una opción: ") #SOLICITA OPCION AL USUARIO

    if opcion == "1": #OPCION PARA MOSTRAR STOCK TOTAL DE UNA MARCA
        marca = input("Ingrese la marca: ") #SOLICITA LA MARCA AL USUARIO
        stock_marca(marca)
    elif opcion == "2": #OPCION PARA BUSCAR NOTEBOOKS POR PRECIO
        while True: #VALIDA QUE LOS PRECIOS SEAN ENTEROS
            try:
                precio_minimo = int(input("Ingrese precio minimo: "))
                precio_maximo = int(input("Ingrese precio maximo: "))
                break
            except:
                print("Debe ingresar valores enteros!")
        busqueda_precios(precio_minimo, precio_maximo)
    elif opcion == "3": #OPCION PARA ACTUALIZAR EL PRECIO DE UN MODELO
        while True: #PERMITE ACTUALIZAR VARIOS PRECIOS SI EL USUARIO LO DESEA
            modelo = input("Ingrese el modelo que desea actualizar: ") #SOLICITA EL MODELO
            try:
                nuevo_precio = int(input("Ingrese el nuevo precio: ")) #SOLICITA EL NUEVO PRECIO
            except:
                print("Debe ingresar un valor entero para el precio.")
                continue
            resultado = actualizar_precio(modelo, nuevo_precio)
            if resultado:
                print("Precio actualizado!")
            else:
                print("El modelo no existe!")
            seguir = input("¿Desea actualizar otro precio? (si/no): ") #PREGUNTA SI DESEA ACTUALIZAR OTRO
            if seguir.lower() != "si": 
                break
    elif opcion == "4": #OPCION PARA SALIR DEL PROGRAMA
        print ("Programa finalizado.") #MENSAJE DE DESPEDIDA
        break
    else:
        print("Debe seleccionar una opcion valida!!")


#no pude usar el git init xd
#https://github.com/skypv/EV4_TRANSVERSAL.git
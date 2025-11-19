

# Pide al usuario el nombre del producto

nombre = input ("Ingrese nombre del producto: ")

# Pide el precio y valida el precio. En caso de ser menor a 0 error, en caso de no colocar un precio invalido error y volver a pedirlo

while True:
    try:
        pedir_precio = input("Ingrese el precio del producto: ")
        precio = float(pedir_precio)
        if precio < 0:
            print("Error precio negativo. Intentelo de nuevo.")
            continue
        break
    except ValueError:
        print("Error: Debe ingresar un número válido para el precio: ")

# Pide la cantidad y valida la cantidad. En caso de ser menor a 0 error, en caso en caso de colocar valor invalido error y volver a pedirlo

while True: 
    try: 
        pedir_cantidad = input("Ingresa cantidad del producto: ")
        cantidad = int(pedir_cantidad)
        if cantidad < 0:
            print("Error cantidad negativa")
            continue
        break
    except ValueError:
        print ("Error cantidad invalida, intente nuevamente: ")


# Calcula costo total del producto
        
costo_total = precio * cantidad

# imprimir el resumen del producto que se esta registrando en el inventario

print("RESUMEN PRODUCTO EN INVENTARIO")
print(f"Nombre del producto: {nombre}")
print(f"Precio del producto: {precio}")
print(f"Precio del producto: {cantidad}")
print(f"Precio del producto: {costo_total}")


'''
El programa pide al ususario ingresar el nombre del producto, precio del producto y cantidad del producto.
Si el usuario ingresa un valor invalido muestra error y vuelve a pedirlo
calcula el precio total del producto y imprime un resumen detallado del mismo en el inventario
'''


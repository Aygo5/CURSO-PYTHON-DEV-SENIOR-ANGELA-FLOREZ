ventasTotales=0.0
#listas para almacenar la informacion
nombres= []
precios= []
cantidades= []
numProductos= int(input("Ingrese el número de productos a gestionar: "))
print("Ingreso inicial de productos a la tienda: ")

for i in range(numProductos):
    print(f"Producto {i+1}: ")
    nombre= input("Ingrese el nombre del producto: ").lower()
    nombres.append(nombre)
    precio= float(input("Ingrese el precio del producto: "))
    precios.append(precio)
    cantidad=float(input("Ingrese la cantidad del producto: "))
    cantidades.append(cantidad)

while True:
    print("\n --- MENÚ DE GESTIÓN DE DROGUERIA ---")
    print("1. Vender producto")
    print("2. Mostrar inventario")
    print("3. Mostrar ventas totales")
    print("4. Salir")
    opcion=int(input("Seleccione una opción: "))
    if opcion==1:
        print("\nVender Producto")
        nombreVenta= input("Ingrese el no,bre del produnto a vender").lower()
        cantidadVender= int(input("Ingrese cantidad a vender")) 
        productoEncontrado= False
        for i in range(len(nombres)):
            if nombres[i]==nombreVenta:
                productoEncontrado=True
                if cantidadVender <= cantidades[i]:
                    totalVenta= cantidadVender*precios[i]
                    ventasTotales+= totalVenta
                    cantidades[i]-= cantidadVender
                    print(f"Venta realizada, total de esta venta ${totalVenta:.2f}")
                    print(f"Quedan {cantidades[i]} unidades de {nombres[i]} en el inventario")
                else:
                    print(f"No hay suficientes unidades en inventario. Quedan solo {cantidades[i]} en Stock")
                    break
            if not productoEncontrado:
                print("Producto no encontrado en el inventario")
    elif opcion==2:
        print("\nInventario de productos")
        for i in range(len(nombres)):
            print(f"Producto {i+1}: {nombres[i].capitalize()}, Precio: {precios[i]:.2f}, Cantidad: {cantidades[i]}")
    elif opcion==3:
        print(f"\nVentas totales acumuladas: {ventasTotales:.2f}")
    elif opcion==4:
        print("Gracias por usar nuestro sistema")
    else:
        print("Opción Invalida. Ingrese un número entre 1-4")
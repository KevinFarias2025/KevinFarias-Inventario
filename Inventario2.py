inventario={}
def mostrar_menu():
    print("\nMenu")
    print("1.Ingresa producto")
    print("2.Buscar producto")
    print("3.Salir")

while True:
        mostrar_menu()
        opcion=input("Elija una opcion: ")

        if opcion=="1":
            nombre=input("¿Como se llama el producto?: ")

            if nombre in inventario:
                print("Ese producto ya esta registrado") 
            else: 
                cantidad=input("Cantidad") 
                precio=input("Precio") 

                if cantidad.isdigit() and float(precio)> 0: 
                    inventario[nombre]= { "cantidad":
                  int(cantidad),"precio": float(precio)
                    }
                    print("Producto agregado")
                else:
                    print("Producto invalido")

        elif opcion=="2":
            nombre=input("¿Cual es el nombre del producto que desea borrar?: ")
            if nombre in inventario:
                del inventario[nombre]
                print("Producto eliminado")
            else:
                print("El producto no existe")

        elif opcion=="3":
            print("Saliendo del menu")
        else:
         print("Opcion invalida")

def menu():
    opcion = "u"
    while opcion!="d":
        print("Que desea cotizar?")
        print("1 Fiesta Gala")
        print("2 Fiesta Cumpleanios")
        print("d Detener Programa")
        opcion = input("Ingrese una opcion")
        if opcion == "1" or opcion == "2":
            cotizar_fiesta(int(opcion))
        elif opcion.lower() == "d":
            print("vais")
        else:
            print("La opcion ingresada no es valida") 


def cotizar_fiesta(opcion:int):
    if opcion==1:
        cotizar_fiesta_gala()
    else:
        cotizar_fiesta_cumplanios()

def cotizar_fiesta_gala():
    pass

def cotizar_fiesta_cumplanios():
    pass


menu()
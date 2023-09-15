from FiestaGala import FiestaGala
from FiestaCumpleanios import FiestaCumpleanios

def menu():
    opcion = "u"
    while opcion!="d":
        print("Que desea cotizar?")
        print("1 Fiesta Gala")
        print("2 Fiesta Cumpleanios")
        print("d Detener Programa")
        opcion = input("Ingrese una opcion: ")
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
    try:
        personas = int(input("Ingrese numero de personas: "))
        if personas > 0:
            gala = FiestaGala(personas)
            gala.calcular_costo_decoracion(decidete("decorar"))
            gala.__set_opcion_saludable(decidete("opcion saludable"))
            total = gala.calcular_costo()
            print(gala)
            print(f"Total: {total}")
            
        else:
            print("ERROR. Debes ingresar un valor mayor a 1")
    except:
        print("Debes ingresar un valor entero")

def cotizar_fiesta_cumplanios():
    pass


def decidete(texto:str):
    decide = "a"
    while decide!='s' and decide!='n':
        decide = input(f"Desea {texto} s/n ")
        if decide.lower() == "s":
            return True
        elif decide.lower('n'):
            return False
        else:
            print("ERROR. Solo puedes ingresar una s o n")


menu()
# main.py

from conjuntos import Conjuntos


def leer_conjunto():
    elementos = input(
        "Ingrese los elementos del conjunto (letras A-Z y dígitos 0-9, sin espacios): ")
    return Conjuntos(elementos.upper())


def mostrar_menu():
    print("\nMenú Principal:")
    print("1. Construir conjuntos")
    print("2. Operar conjuntos")
    print("3. Finalizar")


def operar_conjuntos(A, B, universo):
    print("\nOperaciones disponibles:")
    print("1. Complemento")
    print("2. Unión")
    print("3. Intersección")
    print("4. Diferencia")
    print("5. Diferencia Simétrica")
    opcion = input("Seleccione una operación: ")

    if opcion == "1":
        print(f"Complemento de A: {A.complemento(universo)}")
        print(f"Complemento de B: {B.complemento(universo)}")
    elif opcion == "2":
        print(f"Unión de A y B: {A.union(B)}")
    elif opcion == "3":
        print(f"Intersección de A y B: {A.interseccion(B)}")
    elif opcion == "4":
        print(f"Diferencia A - B: {A.diferencia(B)}")
        print(f"Diferencia B - A: {B.diferencia(A)}")
    elif opcion == "5":
        print(f"Diferencia Simétrica entre A y B: {A.diferencia_simetrica(B)}")
    else:
        print("Opción no válida.")


def main():
    universo = Conjuntos("ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789")
    A = B = None

    while True:
        mostrar_menu()
        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            print("\nConstruir Conjuntos")
            A = leer_conjunto()
            B = leer_conjunto()
            print(f"Conjuntos A: {A}")
            print(f"Conjuntos B: {B}")
        elif opcion == "2":
            if A is None or B is None:
                print("Primero debe construir los conjuntos.")
            else:
                operar_conjuntos(A, B, universo)
        elif opcion == "3":
            print("Finalizando programa...")
            break
        else:
            print("Opción no válida.")


if __name__ == "__main__":
    main()

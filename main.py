from conjuntos import Conjuntos


def leer_conjunto():
    while True:
        elementos = input("Ingrese los elementos del conjunto (letras A-Z y dígitos 0-9, sin espacios): ")
        if all(char in "ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789" for char in elementos.upper()):
            return Conjuntos(elementos.upper())
        else:
            print("Error: Ingrese solo letras de A-Z y dígitos 0-9.")


def mostrar_menu():
    print("\nMenú Principal:")
    print("1. Construir conjuntos")
    print("2. Operar conjuntos")
    print("3. Finalizar")


def seleccionar_conjuntos(conjuntos):
    indices = input(f"Seleccione los conjuntos que desea operar (ejemplo: 0 1 para los primeros dos conjuntos): ")
    seleccionados = []
    for idx in indices.split():
        try:
            seleccionados.append((int(idx), conjuntos[int(idx)]))
        except (ValueError, IndexError):
            print(f"Índice inválido: {idx}. Se omite.")
    return seleccionados


def operar_conjuntos(conjuntos, universo):
    seleccionados = seleccionar_conjuntos(conjuntos)
    if len(seleccionados) < 2:
        print("Debe seleccionar al menos dos conjuntos para operar.")
        return

    print("\nOperaciones disponibles:")
    print("1. Complemento")
    print("2. Unión")
    print("3. Intersección")
    print("4. Diferencia")
    print("5. Diferencia Simétrica")
    opcion = input("Seleccione una operación: ")

    idx_A, A = seleccionados[0]
    idx_B, B = seleccionados[1]

    if opcion == "1":
        print(f"Complemento del conjunto {idx_A}: {A.complemento(universo)}")
        print(f"Complemento del conjunto {idx_B}: {B.complemento(universo)}")
    elif opcion == "2":
        print(f"Unión del conjunto {idx_A} y el conjunto {idx_B}: {A.union(B)}")
    elif opcion == "3":
        print(f"Intersección del conjunto {idx_A} y el conjunto {idx_B}: {A.interseccion(B)}")
    elif opcion == "4":
        print(f"Diferencia {idx_A} - {idx_B}: {A.diferencia(B)}")
        print(f"Diferencia {idx_B} - {idx_A}: {B.diferencia(A)}")
    elif opcion == "5":
        print(f"Diferencia Simétrica entre el conjunto {idx_A} y el conjunto {idx_B}: {A.diferencia_simetrica(B)}")
    else:
        print("Opción no válida.")


def main():
    universo = Conjuntos("ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789")
    conjuntos = []

    while True:
        mostrar_menu()
        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            if conjuntos:
                print("Advertencia: Se borrarán todos los conjuntos anteriores.")
                conjuntos.clear()

            num_conjuntos = int(input("¿Cuántos conjuntos desea crear? "))
            for i in range(num_conjuntos):
                print(f"\nConstruir Conjunto {i}")
                conjunto = leer_conjunto()
                conjuntos.append(conjunto)
                print(f"Conjunto {i}: {conjunto}")
        elif opcion == "2":
            if len(conjuntos) < 2:
                print("Debe haber al menos dos conjuntos para operar.")
            else:
                operar_conjuntos(conjuntos, universo)
        elif opcion == "3":
            print("Finalizando programa...")
            break
        else:
            print("Opción no válida.")


if __name__ == "__main__":
    main()

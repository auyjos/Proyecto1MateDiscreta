from conjuntos import Conjuntos


def leer_conjunto():
    while True:
        elementos = input(
            "Ingrese los elementos del conjunto (letras A-Z y dígitos 0-9, sin espacios): ")
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
    indices = input(
        f"Seleccione los conjuntos que desea operar (ejemplo: A,B,C): ").upper().replace(" ", "")
    seleccionados = []
    for idx in indices.split(','):
        if idx in conjuntos:
            seleccionados.append((idx, conjuntos[idx]))
        else:
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

    if opcion == "1":
        for idx, conjunto in seleccionados:
            print(f"Complemento del conjunto {idx}: {
                  conjunto.complemento(universo)}")
    elif opcion == "2":
        resultado = seleccionados[0][1]
        for _, conjunto in seleccionados[1:]:
            resultado = resultado.union(conjunto)
        print(f"Unión de los conjuntos: {resultado}")
    elif opcion == "3":
        resultado = seleccionados[0][1]
        for _, conjunto in seleccionados[1:]:
            resultado = resultado.interseccion(conjunto)
        print(f"Intersección de los conjuntos: {resultado}")
    elif opcion == "4":
        resultado = seleccionados[0][1]
        for _, conjunto in seleccionados[1:]:
            resultado = resultado.diferencia(conjunto)
        print(f"Diferencia de los conjuntos: {resultado}")
    elif opcion == "5":
        resultado = seleccionados[0][1]
        for _, conjunto in seleccionados[1:]:
            resultado = resultado.diferencia_simetrica(conjunto)
        print(f"Diferencia Simétrica de los conjuntos: {resultado}")
    else:
        print("Opción no válida.")


def main():
    universo = Conjuntos("ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789")
    conjuntos = {}
    letras_disponibles = list("ABCDEFGHIJKLMNOPQRSTUVWXYZ")

    while True:
        mostrar_menu()
        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            if not letras_disponibles:
                print(
                    "No se pueden crear más conjuntos, se ha alcanzado el límite de 26.")
                continue

            num_conjuntos = int(input("¿Cuántos conjuntos desea crear? "))
            if num_conjuntos > len(letras_disponibles):
                print(f"Solo puede crear hasta {
                      len(letras_disponibles)} conjuntos adicionales.")
                continue

            for i in range(num_conjuntos):
                letra = letras_disponibles.pop(0)
                print(f"\nConstruir Conjunto {letra}")
                conjunto = leer_conjunto()
                conjuntos[letra] = conjunto
                print(f"Conjunto {letra}: {conjunto}")
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

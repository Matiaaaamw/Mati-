def main():
    total_capacidad = 100
    disponible = 100
    historial = 0

    print("Bienvenido al sistema de gestion de asientos de la Sala de Conferencias")

    while True:
        print("=== MENU PRINCIPAL ===")
        print("1. Asientos disponibles")
        print("2. Reservar asientos")
        print("3. Liberar asientos")
        print("4. Historial de reservas")
        print("5. Salir")
        opcion = input("Seleccione una opcion: ").strip()

        if opcion == "1":
            print(f"Asientos disponibles: {disponible}")

        elif opcion == "2":
            cantidad_texto = input("Ingrese la cantidad de asientos a reservar: ").strip()
            try:
                cantidad = int(cantidad_texto)
            except ValueError:
                print("Valor invalido. Debe ingresar un numero entero")
                continue

            if cantidad <= 0:
                print("La cantidad debe ser mayor a 0")
            elif cantidad > disponible:
                print("No hay suficientes asientos disponibles para reservar esa cantidad")
            else:
                disponible -= cantidad
                historial += cantidad
                print(f"Se reservaron {cantidad} asientos")

        elif opcion == "3":
            cantidad_texto = input("Ingrese la cantidad de asientos a liberar: ").strip()
            try:
                cantidad = int(cantidad_texto)
            except ValueError:
                print("Valor invalido. Debe ingresar un numero entero")
                continue

            if cantidad <= 0:
                print("La cantidad debe ser mayor a 0")
            elif disponible + cantidad > total_capacidad:
                print("No se puede liberar esa cantidad. Supera la capacidad maxima de la sala")
            else:
                disponible += cantidad
                historial -= cantidad
                print(f"Se liberaron {cantidad} asientos")

        elif opcion == "4":
            print(f"Reservas realizadas durante la sesion: {historial}")

        elif opcion == "5":
            print("Gracias por utilizar nuestro software, hasta la proxima")
            break

        else:
            print("Opcion invalida. Intente de nuevo")


if __name__ == "__main__":
    main()

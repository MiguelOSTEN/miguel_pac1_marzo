def celsius_to_fahrenheit(celsius):
    return (celsius * 9/5) + 32
def fahrenheit_to_celsius(fahrenheit):
    return (fahrenheit - 32) * 5/9
def main():
    while True:
        print("1. Convertir de Celsius a Fahrenheit")
        print("2. Convertir de Fahrenheit a Celsius")
        print("3. Finalizar")
        opcion = input("Seleccione una opción: ")
        if opcion == "1":
            temperatura = float(input("Ingrese la temperatura en grados Celsius: "))
            resultado = celsius_to_fahrenheit(temperatura)
            print(f"{temperatura} grados Celsius son equivalentes a {resultado} grados Fahrenheit.")
        elif opcion == "2":
            temperatura = float(input("Ingrese la temperatura en grados Fahrenheit: "))
            resultado = fahrenheit_to_celsius(temperatura)
            print(f"{temperatura} grados Fahrenheit son equivalentes a {resultado} grados Celsius.")
        elif opcion == "3":
            print("¡Hasta luego!")
            break
        else:
            print("Opción inválida. Por favor, seleccione una opción válida.")

if __name__ == "__main__":
    main()
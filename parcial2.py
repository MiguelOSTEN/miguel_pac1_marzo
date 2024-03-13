def mostrar_tabla_multiplicar(numero):
    print("Número Incrementa Resultado")
    for i in range(1, 12):
        resultado = numero * i
        print(f"{i} {numero} {resultado}")
def main():
    while True:
        try:
            numero = int(input("Ingrese un número entero: "))
            if numero <= 0:
                print("Por favor, ingrese un número entero.")
            else:
                mostrar_tabla_multiplicar(numero)
                break
        except ValueError:
            print("Por favor, ingrese un número entero válido.")

if __name__ == "__main__":

    main()
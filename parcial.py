import os
def contar_vocales(frase):
    contador_a = contador_e = contador_i = contador_o = contador_u = 0
    frase = frase.lower()
    for letra in frase:
        if letra == 'a':
            contador_a += 1
        elif letra == 'e':
            contador_e += 1
        elif letra == 'i':
            contador_i += 1
        elif letra == 'o':
            contador_o += 1
        elif letra == 'u':
            contador_u += 1           
    return contador_a, contador_e, contador_i, contador_o, contador_u
def main():
    total_vocales = 0
    
    while True:
        frase = input("Ingrese una frase o nombre (para ejecutar el programa ): ")
        if frase.lower() == 'finalizar':
            print("Saliendo del programa...")
            break
        
        contador_a, contador_e, contador_i, contador_o, contador_u = contar_vocales(frase)
        
        total_frase = contador_a + contador_e + contador_i + contador_o + contador_u
        
        total_vocales += total_frase
        
        print("Cantidad de vocales 'a':", contador_a)
        print("Cantidad de vocales 'e':", contador_e)
        print("Cantidad de vocales 'i':", contador_i)
        print("Cantidad de vocales 'o':", contador_o)
        print("Cantidad de vocales 'u':", contador_u)
        print("Cantidad total de vocales en la frase:", total_frase)
    
    print("Cantidad total de vocales ingresadas:", total_vocales)
if __name__ == "__main__":
    main()




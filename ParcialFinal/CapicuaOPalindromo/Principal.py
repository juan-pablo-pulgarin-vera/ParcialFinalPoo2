from warnings import catch_warnings
import Frase
import Palabra

n=4
while n != 0:
    print("-----------------------------")
    print("¿Qué operacón desea realizar?")
    print("-----------------------------")
    print("1. probar palabra")
    print("2. probar frase")
    print("-----------------------------")
    print("0. Salir")
    print("-----------------------------")

    try:
        n = int(input("Seleccione una opcion: "))
        
    except:
        print("El valor ingresado solo puede ser númerico")
    
    if n == 0:
        print("Salió correctamente")
        exit()
    elif n ==1:
        palabra1 = input("Ingrese la palabra")
        Palabra.Palabra.EsCapicua(palabra1)
    elif n==2:
        palabra2 =input("Ingrese la frase")
        Frase.Frase.EsPalindromo(palabra2)

  
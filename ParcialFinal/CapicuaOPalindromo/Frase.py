class Frase:

    def EsPalindromo(palabra):
      pal =palabra.replace(" ", "")
      palabraAlReves = ''.join(reversed(pal))

      if pal == palabraAlReves.replace(" ", ""):
        print("Es palindromo")
      else:
        print("No es palindromo")




   
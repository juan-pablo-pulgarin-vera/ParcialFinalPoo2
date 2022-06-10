class Palabra:
    
    def EsCapicua(palabra):
      pal = palabra.replace(" ", "")
      palabraAlReves = ' '.join(reversed(pal))

      if pal == palabraAlReves.replace(" ", ""):
        print("Es capicua")
      else:
        print("No es capicua")


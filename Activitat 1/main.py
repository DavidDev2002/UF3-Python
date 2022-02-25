import functions as f
TEXTO_1 = "Introduce el texto que quieras introducir en el archivo: "
def main():
   texto = str(input(TEXTO_1))
   while len(texto) > 100:
      texto = str(input(TEXTO_1))
   f.write_file('files/text.txt', texto)

if __name__ == "__main__" :
   main()
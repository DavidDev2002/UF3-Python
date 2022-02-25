import functions as f
TEXTO_1 = "Introduce el texto que deseas añadir en el archivo: "
def main():
   texto = str(input(TEXTO_1))
   while len(texto) > 100:
      texto = str(input(TEXTO_1))
   f.file_add_st('files/text.txt', texto)

if __name__ == "__main__" :
   main()
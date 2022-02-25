from Exercici_Clase import functions as f


#Pedir por teclado un texto y si esxiste el archivo sobreescribirlo y si no lo crea. Luego lo muestra
def main():
   ruta = input("Introduce la ruta del archivo que quieres crear: ")
   existe = f.check_file(ruta)
   f.file_add(ruta)

if __name__ == "__main__" :
   main()


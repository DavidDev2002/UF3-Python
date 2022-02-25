TEXTO_1 = "*********MENÚ***********"
TEXTO_2 = "1 - CREA UN FICHERO"
TEXTO_3 = "2 - MUESTRA UN FICHERO"
TEXTO_4 = "3 - MODIFICA UN FICHERO"
TEXTO_5 = "4 - EXIT"
TEXTO_6 = "Selecciona una opción: "
TEXTO_7 = "Has introducido un numero no valido."
TEXTO_8 = "Introduce el nombre del fichero: "
TEXTO_9 = "Introduce el texto que quieras modificar: "
TEXTO_10 = "Tancant el programa..."

def file_create():
    fname = input(TEXTO_8)
    f = open('files/' + fname, 'w')
    f.close()

def file_read():
    fname = input(TEXTO_8)
    f = open('files/' + fname, 'r')
    print(f.read())
    f.close()

def file_modify():
    fname = input(TEXTO_8)
    f = open('files/' + fname, 'w')
    texto = input(TEXTO_9)
    f.write(texto)
    f.close()

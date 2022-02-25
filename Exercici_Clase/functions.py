def check_file(file):
    try:
        f = open(file, "r")
        return True
    except FileNotFoundError as e:
        return False
    else:
        f.close()

def file_add(fname):
  f = open(fname, "a+")
  str = input("Introdueix una frase: ")
  f.write(str)
  print(f.read())
  f.close()
import functions as f

def main():
    print(f.TEXTO_1)
    print(f.TEXTO_2)
    print(f.TEXTO_3)
    print(f.TEXTO_4)
    print(f.TEXTO_5)

    selector = int(input(f.TEXTO_6))
    while selector > 4:
        selector = int(input(f.TEXTO_6))

    match selector:
        case 1:f.file_create()
        case 2:f.file_read()
        case 3:f.file_modify()
        case 4:print(f.TEXTO_10)
        case _: print(f.TEXTO_7)

if __name__ == "__main__" :
   main()
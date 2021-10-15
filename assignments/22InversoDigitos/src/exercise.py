def main():
    num = int(input("Enter a number: "))
    #escribe tu código abajo de esta línea
    invertido = str(num)
    cont = len(invertido)
    if cont<=6:
        if num < 0:
            num01 = num*-1
            a = int(str(num01)[::-1])
            b = a*-1
            print(b)
        else:
            a = int(invertido[::-1])
            print(a)
    else:
        print("Too long")
        
if __name__=='__main__':
    main()

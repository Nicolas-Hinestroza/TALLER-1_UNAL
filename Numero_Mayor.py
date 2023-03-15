a = int(input("Ingrese un numero real: "))
b = int(input("Ingrese un numero real: "))
c = int(input("Ingrese un numero real: ")) 
if a == b or a == c or b == c:
      print("ERROR") 
else:
    if a > b and a > c:
         print ("El numero mayor es " + str(a))
    else:
        if b > c:
            print("El numero mayor es " + str(b))
        else:
            print("El numero mayor es " + str(c))
                   
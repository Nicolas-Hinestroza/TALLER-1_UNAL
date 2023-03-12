# TALLER-1_UNAL
En este repo se dará evidencia a la solución de los puntos del taller #1, con imágenes en formas de evidencia y describiendo la solución de cada programa

 -  Solucion quiz Python Beginner Quiz
 
 ![image](https://user-images.githubusercontent.com/124611099/223179234-fbffdc1b-6b6c-45b6-bfc9-438df99eb5e7.png)

- Programa para identificar el mayor de de tres numeros.

Este es un programa muy sencillo ya que primero toca identificar las variables (a, b, c) luego colocar un comando en el cual los 3 numeros no sean iguales, asi se podra identifical el numero mayor, en caso de que sean numeros iguales el programa imprimira "ERROR". Ahora colocamos la pregunta si a es mauor que b y c si es asi se imprimira este numero como el mayor, ahora pasamos a la parte negativa, en esta se colocara si b es mayor que c si es asi se imprimira b como el mayor si b no es mayor que c entonces c se imprimira como el mayor.

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
 



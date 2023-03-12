# TALLER-1_UNAL
En este repo se dará evidencia a la solución de los puntos del taller #1, con imágenes en formas de evidencia y describiendo la solución de cada programa

- 1. Solucion quiz Python Beginner Quiz
 
 ![image](https://user-images.githubusercontent.com/124611099/223179234-fbffdc1b-6b6c-45b6-bfc9-438df99eb5e7.png)

- 2. Programa para identificar el mayor de de tres numeros.

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
              
- 3. Programa que lea un número enteros y determine si es par o impar.

Para este codigo solo se tiene que definir dos variables, en este caso es la a y la r. a es el numero que el programa lee, es decir el que nosotros escribimos y la r es el residuo de la division. En este caso para saber si un numero es par o impar el residuo de la division de a entre 2 debe de dar 0, si es asi el programa imprimira que a es un numero par por lo contrario, si el residuo da otro numero el programa imprimira que a es un numero impar.

      a = int(input("Ingrese un numero entero: "))
      r = 0
      r = a % 2
      if r == 0:
         print (str(a) + " Es un numero par")
      else:
         print (str(a) + " Es un numero impar")
         
- 4. Programa que lea dos números reales y determine si el primero es múltiplo del segundo.
 
En este caso definimos dos variasbles a y b, para saber si el primer numero es multiplo del segundo toca realizar la division si el residuo es 0 entonces si son multiplos. Para el caso verdadero el programa imprimira que si son multiplos y para el caso falso el programa imprimira que no son multiplos.
 
    a = int(input("Ingrese un numero real: "))
    b = int(input("Ingrese un numero real: "))
    if a % b == 0:
       print (str(a) + " Es multiplo de " + str(b))
    else:
       print (str(a) + " No un multiplo de " + str(b))
- 5. Programa que lea tres números reales y determine si la suma de los dos primeros es mayor, menor o igual que el tercer número.

Para este programa primero definimos 4 variables que son a, b, c como los numeros que nosotros digitaremos y el programa leera para realizar las operaciones y d como el resultado de la suma de a y b. En este caso usaremos la estructura if-elif-else que nos ayudara a enlazar varias estructuras condicionales de tal manera que solamente se pueda ejecutar un grupo de instrucciones dependiendo de cual de las opciones se evalúa verdadero. En el caso si d es igual a c pues el programa imprimira que d es igual a c. En el caso si d es mayor que c pues el programa imprimira que d es mayor a c. Y para finalizar en el caso si d es menor a c pues el programa imprimira que d es menor a c.


      a = int(input("Ingrese un numero real: "))
      b = int(input("Ingrese un numero real: "))
      c = int(input("Ingrese un numero real: ")) 
      d = 0
      d = a + b
      print (str(a) + " + " + str(b) +  " = " + str(d))
      if d == c:
         print ("Por lo tanto " + str(d) + " es igual que " + str(c))
      elif d > c:
         print ("Por lo tanto " + str(d) + " es mayor que " + str(c))
      else:
         print ("Por lo tanto " + str(d) + " es menor que " + str(c))
         
- 6. Programa que solicite al usuario una letra y determine si es una vocal o una consonante.

Este es un codigo muy sencillo ya que lo unico que hay que hacer es definir las variables a y vocales. Para este caso a es la letra que nosotros digitemos y vocales es el grupo de las vocales ya definidas. El programa se preguntara si la letra escrita esta dentro del grupo de las vocales si es asi el programa imprimira que a es una vocal por lo contrario imprimira que a es una consonante.
 
         a = input("ingrese una letra ")
         Vocales = ["a", "e", "i", "o", "u"]
         if a in Vocales:
            print (str(a) + " Es una vocal")
         else:
            print (str(a) + " Es una consonante")
            
- 7. Programa que pida 5 números reales y calcule las siguientes operaciones:
- El promedio.
- La mediana.
- El promedio multiplicativo (multilplica todos y luego calcula la raíz de la cantidad de operandos).
- Ordenar los números de forma ascendente.
- Ordenar los números de forma descendente.
- La potencia del mayor número elevado al menor número.
- La raíz cúbica del menor número.

- 8. Programa al que se le ingrese la frecuencia de una onda en hz y como salida arroje en que parte del espectro electromagnético se encuentra.

- 9. Programa que reciba el nombre en minúsculas de un país de America y retorne la ciudad capital, si el país no pertenece al continente debe arrojar país no identificado.
lang = input("Escribe un país de América en minúsculas para saber su Capital: ")

Este es un codigo largo aunque no sea muy complicado de realizar o de ententer es muy tedioso para escirbirlo. Para realizar este codigo utilizamos la estructura match-case (switch-case) que consiste en una estructura de selección que toma una condición de referencia y establece bloques de ejecución en caso de coincidencia especifica. para esto colocamos lang este es un módulo que permite hacer cumplir las restricciones del lenguaje  y usamos match y case, es decir para cada caso espesifico el programa imprime un especifico resultado.

        lang = input("Escribe un país de América en minúsculas para saber su Capital: ")
        match lang:
        case "canada":
          print("La capital de Canada es Otawwa")
        case "estados unidos":
          print("La capital de Estados Unidos es Washington DC.")
        case "mexico":
          print("La capital de Mexico es México DF.")
        case "belice":
          print("La capital de Belice es Belmopán.")
        case "costa rica":
          print("La capital de Costa Rica es San José.")
        case "el salvador":
          print("La capital de El Salvador es San Salvador.")
        case "guatemala":
          print("La capital de Guatemala es Ciudad de Guatemala.")
        case "honduras":
          print("La capital de Honduras es Tegucigalpa.")
        case "nicaragua":
          print("La capital de Nicaragua es Managua.")
        case "panama":
          print("La capital de de Panama es Panamá.")
        case "argentina":
          print("La capital de Argentina es Buenos Aires.")
        case "bolivia":
          print("La capital de Bolivia es Sucre. Aunque siempre creíste que la capital de Bolivia era La Paz, esta es solo su sede de gobierno, su constitución establece que es Sucre.")
        case "brasil":
          print("La capital de Brasil es Brasilia.")
        case "chile":
          print("La capital de Chile es Santiago de Chile.")
        case "colombia":
          print("La capital de Colombia es Bogotá.")
        case "ecuador":
          print("La capital de Ecuador es Quito.")
        case "paraguay":
          print("La capital de Paraguay es Asunción.")
        case "peru":
          print("La capital de Peru es Lima.")
        case "surinam":
          print("La capital de Surinam es Parabarimo.")
        case "trinidad y tobago":
          print("La capital de Trinidad y Tobago es Puerto España.")
        case "uruguay":
          print("La capital de Uruguay es montevideo.")
        case "venezuela":
          print("La capital de Venezuela es Caracas.")
        case "puerto rico":
          print("Puerto Rico no es considerado un país, ya que pertenece a Estados Unidos.")
        case "antigua y barbuda":
          print("La capital de Antigua y Barbuda es Saint John.")
        case "bahamas":
          print("La capital de Bahamas es Nasáu.")
        case "barbados":
          print("La capital de Barbados es Bridgetown.")
        case "cuba":
          print("La capital de Cuba es La Habana.")
        case "dominica":
          print("La capital de Dominica es Roseau.")
        case "granada":
          print("La capital de Granada es Saint George.")
        case "guyana":
          print("La capital de Guyana es Georgetown.")
        case "haiti":
          print("La capital de Haití es Puerto Príncipe.")
        case "jamaica":
          print("La capital de Jamaica es Kingston.")
        case "republica dominicana":
          print("La capital de República Dominicana es Santo Domingo.")
        case "san cristobal y nieves":
          print("La capital de San Cristóbal y Nieves es Basseterre.")
        case "san vicente y las granadinas":
          print("La capital de San Vicente y las Granadinas es Kingstown.")
        case "santa lucia":
          print("La capital de Santa Lucía es Castries.")
        case "alaska":
          print("Alaska pertenece a uno de los 50 estados que conforman Estados Unidos, no es un país.")
        case "groenlandia":
          print("Groenlandia forma parte de Dinamarca, por eso no está incluido en esta lista.")
        case _:
          print("País no identificado.")
          
- 10. Programa que dada una distancia calcule:
- El tiempo que le tomaría a la luz recorrer la distancia.
- El tiempo que le tomaría al sonido (en el aire) recorrer la distancia.
- El tiempo que le tomaría al vehiculo comercial más veloz recorrer la distancia.
- El tiempo que le tomaría a Bolt recorrer la distancia.

Este codigo lo que necesita en si son procesos para esto definimos las variables "a" que es la distancia en metros que nosotros colocamos y que el programa lee para realizar las operaciones, luego definimos luz, sonido, vehiculo y bolt. Cada una de estos es el resultado de a (que seria la distancia) dividido la velocidad de cada variable. El resultado es el tiempo que recorre cada variable. al final se imprimen cada uno de los resultados.

      a = float(input("Ingrese una distancia en metros: "))
      luz = 0
      sonido = 0
      vehiculo = 0
      bolt = 0
      luz = a / 299792458 
      sonido = a / 343.2 
      vehiculo = a / 141.111 
      bolt = a / 12.422222
      print ("El tiempo que le tomaría a la luz recorrer la distancia "  + str(a) + "mts es de: " + str(luz) + " segundos")
      print ("El tiempo que le tomaría el sonido recorrer la distancia "  + str(a) + "mts es de: " + str(sonido) + " segundos")
      print ("El tiempo que le tomaría al vehiculo comercial mas rapido en recorrer la distancia "  + str(a) + "mts es de: " + str(vehiculo) +  " segundos")
      print ("El tiempo que le tomaría a De Jesse Owens a Usain Bolt la persona mas rapida del planeta en recorrer la distancia "  + str(a) + "mts es de: " + str(bolt) + " segundos")


              
              
              
              
              
              
              
              
              
              
              
              
              
              
              
              
              
 



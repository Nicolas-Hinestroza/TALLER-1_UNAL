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
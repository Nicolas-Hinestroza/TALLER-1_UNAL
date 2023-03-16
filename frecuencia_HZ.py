HZ = float(input("ingresa una frecuencia de onda en HZ: "))
if HZ <= 10**4:
    print ("tu unidad de frecuencia se encuentra en el rango del radio ")
elif HZ > 10**4 and HZ <= 10**8:
    print ("tu unidad de frecuencia se encuentra en el rango del Microondas ")
elif HZ > 10**8 and HZ <= 10**12:
    print ("tu unidad de frecuencia se encuentra en el rango del infrarrojo ")
elif HZ > 10**12 and HZ <= 10**15:
    print ("tu unidad de frecuencia se encuentra en el rango visible por el ser humano ")
elif HZ > 10**15 and HZ <= 10**16:
    print ("tu unidad de frecuencia se encuentra en el rango ultravioleta ")
elif HZ > 10**16 and HZ <= 10**18:
    print ("tu unidad de frecuencia se encuentra en el rango de los rayos X")
else:
    print ("tu unidad de frecuencia se encuentra en el rango de los rayos gama ")
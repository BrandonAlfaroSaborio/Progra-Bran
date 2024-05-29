CapturasCO2= [420,480,425,450]
tiempos_de_capturas=["9:00", "9:05", "9:10", "9:15"]


def Capturas ():
    promedio=0
    print("La cantidad de capturas de CO2 en la coleccion es:",(len(CapturasCO2)))
    for recorrido in CapturasCO2:
        promedio += recorrido
    promedio= promedio / 4
    print("El promedio de CO2 detectado entre las capturas es:", promedio)
     
Capturas()

def maximo(CapturasCO2):
    concentracion_mas_alta= CapturasCO2[0]
    for num in CapturasCO2:
         if num > concentracion_mas_alta:
              concentracion_mas_alta = num
    indice_max = CapturasCO2.index(concentracion_mas_alta)
    hora_concentracion_max = tiempos_de_capturas[indice_max]
    print("La concentracion mas alta de CO2 es: ",concentracion_mas_alta)
    print("La hora de concentracion mas alta es:",hora_concentracion_max)
    return concentracion_mas_alta
    
maximo(CapturasCO2)

def minimo(CapturasCO2):
    concentracion_mas_baja= CapturasCO2[0]
    for num in CapturasCO2:
         if num < concentracion_mas_baja:
              concentracion_mas_baja = num
    indice_min = CapturasCO2.index(concentracion_mas_baja)
    hora_concentracion_min = tiempos_de_capturas[indice_min]
    print("La concentracion mas alta de CO2 es: ",concentracion_mas_baja)
    print("La hora de concentracion mas alta es:",hora_concentracion_min)
    return concentracion_mas_baja

minimo(CapturasCO2)

diferencias_mayores_15 = []
for i in range(1, len(CapturasCO2)):
    diferencia = CapturasCO2[i] - CapturasCO2[i - 1]
    if diferencia > 15 or diferencia < -15:
        diferencias_mayores_15.append(tiempos_de_capturas[i])

print("Las diferencias mayores a 15 son", diferencias_mayores_15)
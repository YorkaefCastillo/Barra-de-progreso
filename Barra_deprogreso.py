#Este proyecto es una barra de progreso sin usar librerias
import time
#Adorno
adorno,titulo = "","Barra de progreso"
print(adorno.center(50,"*"))
print(titulo.center(50).upper())
print(adorno.center(50, "*"))

#Este bloque calculará la fracción de la parte completada en relación al total
def Barra_progreso(parte,total,largo=30):
    fraccion = parte/total
    completado = int(fraccion*largo)
    desaparecido = largo - completado 
    barra = f"[{'#'*completado}{'-'*desaparecido}]{fraccion:.2%}"
    return barra

n = 30

for i in range(n + 1):
    time.sleep(0.1)
    print(Barra_progreso(i, n, 35),end="\r")
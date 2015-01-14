'''
Created on Jan 13, 2015

@author: jemd93
'''

from datetime import datetime
from decimal import *
from math import *

class Tarifa() :
    
    def __init__(self,d,n) :
        self.tDiurna = d
        self.tNocturna = n
    
def CalcularTotal(FechaIni, FechaSal, tarif):
    delta = FechaSal - FechaIni
    tarMax = max(tarif.tDiurna,tarif.tNocturna)
    
    
    if (delta.seconds/60 < 0) or (delta.days < 0) :
        print("Error : Fecha de salida menor que Fecha de entrada ")
         
    #if delta.days > 3 :
       # print("Error : La reservacion no puede ser mayor a 72 horas.")
    #elif (delta.seconds/60) < 15 :
     #   print("Error : La reservacion no puede ser menor a 15 minutos.")
        
    total = Decimal(0)
    totalHoras = delta.days*24 + ceil(delta.seconds/3600)
    horaActual = FechaIni.hour
    
    if (FechaIni.hour > 6) and (FechaIni.hour < 18) :
        tarActual = tarif.tDiurna
    else : 
        tarActual = tarif.tNocturna
    
    while (totalHoras > 0) :
        horaActual = horaActual + 1
        
        if (horaActual == 24) :
            total = total+tarif.tNocturna
            horaActual = 0    
        elif (horaActual == 6) or (horaActual == 18) :
            total = total+tarMax
        elif (horaActual > 6) or (horaActual <= 18) :
            total = total+tarif.tDiurna
        else :
            total = total+tarif.tNocturna
            
        totalHoras = totalHoras-1
        
    return total
        
        
        
        
        
    

anioI = int(input("Introduzca el año de ingreso : "))
mesI = int(input("Introduzca el mes de ingreso : "))
diaI = int(input("Introduzca el dia de ingreso : "))
horaI = int(input("Introduzca la hora de ingreso : "))
minutosI = int(input("Introduzca el minuto de ingreso : "))

anioS = int(input("Introduzca el año de salida : "))
mesS = int(input("Introduzca el mes de salida : "))
diaS = int(input("Introduzca el dia de salida : "))
horaS = int(input("Introduzca la hora de salida : "))
minutosS = int(input("Introduzca el minuto de salida : "))

tarD = Decimal(input("Introduzca la tarifa diurna : "))
tarN = Decimal(input("Introduzca la tarifa nocturna : "))
tar = Tarifa(tarD,tarN)


fechaIng = datetime(anioI,mesI,diaI,horaI,minutosI)
fechaSal = datetime(anioS,mesS,diaS,horaS,minutosS)

print(CalcularTotal(fechaIng,fechaSal,tar))
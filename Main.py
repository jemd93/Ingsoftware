'''
Created on Jan 13, 2015

@author: Jorge Marcano 11-10566
@author: Maria Victoria Jorge 11-10495
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
        return -1
    if delta.days > 3 :
        print("Error : La reservacion no puede ser mayor a 72 horas.")
        return -1
    elif (delta.seconds/60) < 15 :
        print("Error : La reservacion no puede ser menor a 15 minutos.")
        return -1
    if (tarif<0.01):
        print("Error: La tarifa no puede ser menor a 0.01")
        return -1
    elif (tarif>(2**32)-1):
        print("Error: El valor de la tarifa no es representable")
        return -1
        
    total = Decimal(0)
    totalHoras = delta.days*24 + ceil(delta.seconds/3600)
    print("Total horas : ",totalHoras)
    horaActual = FechaIni.hour
    
    while (totalHoras > 0) :
        horaActual = horaActual + 1
        
        if (horaActual == 24) :
            total = total+tarif.tNocturna
            horaActual = 0    
        elif (horaActual == 6) or (horaActual == 18) :
            total = total+tarMax
        elif (horaActual > 6) and (horaActual <= 18) :
            total = total+tarif.tDiurna
        else :
            total = total+tarif.tNocturna
            
        totalHoras = totalHoras-1
        
    return total
        
    
def main():
    #try:
        anioI = int(input("Introduzca el anio de ingreso : "))
        mesI = int(input("Introduzca el mes de ingreso (1-12) : "))
        diaI = int(input("Introduzca el dia de ingreso : "))
        horaI = int(input("Introduzca la hora de ingreso (0-23) : "))
        minutosI = int(input("Introduzca el minuto de ingreso : "))
        
        anioS = int(input("Introduzca el anio de salida : "))
        mesS = int(input("Introduzca el mes de salida (1-12): "))
        diaS = int(input("Introduzca el dia de salida : "))
        horaS = int(input("Introduzca la hora de salida (0-23): "))
        minutosS = int(input("Introduzca el minuto de salida : "))
        
        tarD = Decimal(input("Introduzca la tarifa diurna : "))
        tarN = Decimal(input("Introduzca la tarifa nocturna : "))
        tar = Tarifa(tarD,tarN)
        
        
        fechaIng = datetime(anioI,mesI,diaI,horaI,minutosI)
        fechaSal = datetime(anioS,mesS,diaS,horaS,minutosS)
        
        total = CalcularTotal(fechaIng,fechaSal,tar)
        if (total!=-1):
            print("Debe pagar: ",total)
    #except:   
        #print("Error con los argumentos de entrada")
        
        
if __name__ == "__main__":
    main()
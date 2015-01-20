'''

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
<<<<<<< HEAD
=======
    totalHoras = delta.days*24 + ceil(delta.seconds/3600)
>>>>>>> refs/heads/PruebasVicky
    totalMin = (delta.days*24 + delta.seconds/3600) * 60
    
    if (delta.seconds/60 < 0) or (delta.days < 0) :
        print("Error : Fecha de salida menor que Fecha de entrada ")
        return -1
    if (delta.days == 3 and delta.seconds > 0) or (delta.days > 3) :
        print("Error : La reservacion no puede ser mayor a 72 horas.")
        return -1
<<<<<<< HEAD
    elif (totalMin) < 15 :
=======
    elif (totalMin < 15) :
>>>>>>> refs/heads/PruebasVicky
        print("Error : La reservacion no puede ser menor a 15 minutos.")
        return -1
<<<<<<< HEAD
    if (tarif.tDiurna<0) or (tarif.tNocturna<0):
=======
    if (tarif.tDiurna < 0) or (tarif.tNocturna < 0):
>>>>>>> refs/heads/PruebasVicky
        print("Error: La tarifa no puede ser menor a 0")
        return -1
    elif (tarif.tDiurna>(2**32)-1) or (tarif.tNocturna>(2**32)-1):
        print("Error: El valor de la tarifa no es representable")
        return -1
        
<<<<<<< HEAD
    totalHoras = delta.days*24 + ceil(delta.seconds/3600)
=======
>>>>>>> refs/heads/PruebasVicky
    total = Decimal(0)
    horaActual = FechaIni.hour
    
    if (6 <= horaActual < 18): # La hora inicial esta en el turno diurno
        esDiurno = True         # Booleano para saber el turno actual
    else:                       # La hora inicial esta en el turno nocturno
        esDiurno = False 
    
    if (totalHoras == 1):
        if ((FechaSal.hour == 6) or (FechaSal.hour == 18)) and (FechaSal.minute!=0): # Menos de una hora y mixta
            return tarMax
    
    if ( 6 <= horaActual < 18):
        esDiurno = True
    else :
        esDiurno = False
        
    if (totalHoras == 1):
        if ((FechaSal.hour == 6) or (FechaSal.hour == 18)) and (FechaSal.minute != 0) : 
            return tarMax
        
    while (totalHoras > 0) :
        horaActual = horaActual + 1
        
        if (horaActual == 24) :
            total = total + tarif.tNocturna
            horaActual = 0    
        elif (horaActual == 6) or (horaActual == 18) :
<<<<<<< HEAD
            if (totalHoras == 1):
                if (esDiurno):
                    total = total + tarif.tDiurna
                else :
                    total = total + tarif.tNocturna
            else :
                esDiurno = not(esDiurno)
                total = total + tarMax
                
        elif (horaActual > 6) and (horaActual < 18) :
            total = total+tarif.tDiurna
        else : 
=======
            if (totalHoras == 1): # Es la ultima hora que se cobrara
                if (esDiurno):
                    total = total + tarif.tDiurna
                else:
                    total = total + tarif.tNocturna
            else: # Queda mas tiempo en la reservacion, pero cambio de turno
                esDiurno = not(esDiurno)               
                total = total + tarMax
        elif (horaActual > 6) and (horaActual < 18) :
            total = total + tarif.tDiurna
        else :
>>>>>>> refs/heads/PruebasVicky
            total = total+tarif.tNocturna
            
<<<<<<< HEAD
        if (total > ((2**32)-1)) :
            print("Error : El total es mayor al maximo numero representable.")
            return -1
=======
        if (total > ((2**32)-1)):
            print("Error : El total es mayor al maximo numero representable.")
            return -1    
>>>>>>> refs/heads/PruebasVicky
            
        totalHoras = totalHoras-1
        
    return total
        
    
def main():
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
        
        try :
            fechaIng = datetime(anioI,mesI,diaI,horaI,minutosI)
        except ValueError :
                print("Error : La fecha de ingreso no es valida.")
                return -1
        
        try :       
            fechaSal = datetime(anioS,mesS,diaS,horaS,minutosS)
        except ValueError : 
                print("Error : La fecha de salida no es valida.")
                return -1
        
        total = CalcularTotal(fechaIng,fechaSal,tar)
        
        if (total!=-1):
            print("Debe pagar: ",total)
<<<<<<< HEAD
=======
    #except:   
        #print("Error con los argumentos de entrada")
>>>>>>> refs/heads/PruebasVicky
        
if __name__ == "__main__":
    main()

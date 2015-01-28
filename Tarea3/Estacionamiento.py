'''
27/01/2015

Jorge Marcano : 11-10566
Maria Victoria Jorge : 11-10566

'''

class Estacionamiento :
    
    def __init__(self,puestos): 
        self.reservaciones = []
        self.puestos = puestos
        
    def reservar(self,horaIni,horaFin) :
        reservaOrdenada = self.reservaciones
        reservaOrdenada.sort()
        
        best = 0
        cnt = 0
        
        for i in range(len(reservaOrdenada)-1) :
            if (reservaOrdenada[i][1] == -1) : 
                cnt = cnt+1
            else :
                cnt = cnt-1
        
            if (cnt > best) :
                best = cnt
                beststart=reservaOrdenada[i][0]
                bestend = reservaOrdenada[i+1][0]
                
        if (best == self.puestos) and (((beststart <= horaIni < bestend) or (beststart <  horaFin <= bestend)) or ((horaIni < beststart) and (horaFin > bestend))) :
            return False
        else : 
            return True
            
            
        
    
    
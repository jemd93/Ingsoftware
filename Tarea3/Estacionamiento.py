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
        if len(self.reservaciones) > 0:
            cnt = 0
            i = 0
            while i < len(self.reservaciones)-1 :
                if ((self.reservaciones[i][0] <= horaIni) and (self.reservaciones[i+1][0] >= horaFin)) or ((self.reservaciones[i][0] >= horaIni) and (self.reservaciones[i+1][0] <= horaFin)) :
                    cnt = cnt+1
                i = i+2
            
            if (cnt == self.puestos) :
                return False
            else :
                return True
                
        else:
            return True
        
        
    
    
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
        if len(self.reservaciones)>0:
            return False
        else:
            return True
        
        
    
    
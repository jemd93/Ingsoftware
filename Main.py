'''
Created on Jan 13, 2015

@author: jemd93
'''

from datetime import datetime
from decimal import *

def Funcion(FechaIni, FechaFin, Tarifa):
    delta = FechaFin - FechaIni
    if delta.days > 3 :
        print("Error : La reservacion no puede ser mayor a 72 horas.")
    elif (delta.seconds/60) < 15 :
        print("Error : La reservacion no puede ser menor a 15 minutos.")
        
        

x = datetime(2015,1,10,13,0)
y = datetime(2015,1,15,10,0) # Creando fechas
z = datetime(2015,1,15,17,10)
p = datetime(2015,1,15,17,15)

Funcion(x,y,100)
Funcion(z,p,100)
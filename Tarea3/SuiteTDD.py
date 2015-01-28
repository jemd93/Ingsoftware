'''
27/01/2015

Jorge Marcano : 11-10566
Maria Victoria Jorge : 11-10566

'''
import unittest
from Estacionamiento import Estacionamiento

class TestReservar(unittest.TestCase):
    
    def testExistenciaFuncion(self):    # TDD puro.
        e = Estacionamiento(10)
        e.reservar(10,15)
        
    def testReservacionVacio(self): # TDD puro y frontera.
        e = Estacionamiento(10)
        e.reservaciones = []
        self.assertEquals(e.reservar(10,12),True)
        
    def testReservacionRechazada(self): # TDD puro y frontera.
        e = Estacionamiento(10)
        for i in range(0,e.puestos):
            e.reservaciones.append([10,-1])
            e.reservaciones.append([12,1])    
        self.assertEquals(e.reservar(10,12),False)
        
    def testUnaReservacionNoSolapada(self): # El estacionamiento tiene una reservacion y la nueva no la solapara
        e = Estacionamiento(10)
        e.reservaciones = [[10,-1],[14,1]]
        self.assertEquals(e.reservar(15,16),True)
    
    def testDiezReservacionesNoLleno(self): # TDD puro.
        e = Estacionamiento(10)
        e.reservaciones = [[8,-1],[9,1]]
        for i in range(0,e.puestos-1):
            e.reservaciones.append([10,-1])
            e.reservaciones.append([12,1])  
        self.assertEquals(e.reservar(14,16),True)
        
    def testReservacionSolapada(self):
        e = Estacionamiento(10)
        for i in range(0,e.puestos):
            e.reservaciones.append([10,-1])
            e.reservaciones.append([15,1])
            
        self.assertEquals(e.reservar(12,14),False)
          
        
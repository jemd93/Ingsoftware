'''
27/01/2015

Jorge Marcano : 11-10566
Maria Victoria Jorge : 11-10566

'''
import unittest
from Estacionamiento import Estacionamiento

class TestReservar(unittest.TestCase):
    
    def testExistenciaFuncion(self):
        e = Estacionamiento(10)
        e.reservar(10,15)
        
    def testReservacionVacio(self):
        e = Estacionamiento(10)
        e.reservaciones = []
        self.assertEquals(e.reservar(10,12),True)


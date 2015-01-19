'''
Created on Jan 14, 2015

@author: jemd93
'''

import unittest
from Main import *

class TestCalcularTotal(unittest.TestCase):
    
    # Casos Frontera
    
    def testMinDiurno(self):
        fechaIng = datetime(2015,1,17,16)
        fechaSal = datetime(2015,1,17,16,15)
        tar = Tarifa(Decimal(10),Decimal(20))
        
        self.assertEquals(10,CalcularTotal(fechaIng, fechaSal, tar))
        
    def testMinNocturno(self):
        fechaIng = datetime(2015,1,17,20,15)
        fechaSal = datetime(2015,1,17,20,30)
        tar = Tarifa(Decimal(10),Decimal(20))
        
        self.assertEquals(20,CalcularTotal(fechaIng,fechaSal,tar))
        
    def testMinMixto(self):
        fechaIng = datetime(2015,3,1,17,53)
        fechaSal = datetime(2015,3,1,18,8)
        tar = Tarifa(Decimal(10),Decimal(20))
        
        self.assertEquals(20,CalcularTotal(fechaIng,fechaSal,tar))
        
    def testMaxMixto(self):
        fechaIng = datetime(2015,5,5,15)
        fechaSal = datetime(2015,5,8,15)
        tar = Tarifa(Decimal(10),Decimal(20))
        
        self.assertEquals(1110,CalcularTotal(fechaIng,fechaSal,tar))
        
    def testBisiesto(self):
        fechaIng = datetime(2004,2,28,22)
        fechaSal = datetime(2004,2,29,3)
        tar = Tarifa(Decimal(10),Decimal(20))
        
        self.assertEquals(100,CalcularTotal(fechaIng,fechaSal,tar))
        
    def testFechaMax(self):
        fechaIng = datetime(9999,12,31,7)
        fechaSal = datetime(9999,12,31,14)
        tar = Tarifa(Decimal(10),Decimal(20))
        
        self.assertEquals(70,CalcularTotal(fechaIng,fechaSal,tar))
        
    def testFechaMinx(self):
        fechaIng = datetime(1,1,1,19)
        fechaSal = datetime(1,1,1,22)
        tar = Tarifa(Decimal(10),Decimal(20))
        
        self.assertEquals(60,CalcularTotal(fechaIng,fechaSal,tar)) 
        
    # Casos Esquina
    
    def testMaxDiurno(self):
        fechaIng = datetime(2015,1,17,6)
        fechaSal = datetime(2015,1,17,18)
        tar = Tarifa(Decimal(10),Decimal(20))
        
        self.assertEquals(120,CalcularTotal(fechaIng,fechaSal,tar))
        
    def testMaxNocturno(self):
        fechaIng = datetime(2015,1,17,18)
        fechaSal = datetime(2015,1,18,6)
        tar = Tarifa(Decimal(10),Decimal(20))
        
        self.assertEquals(240,CalcularTotal(fechaIng,fechaSal,tar))
        
    # Casos Malicia
    
    def testTarMaxTotal(self):
        fechaIng = datetime(2015,1,20,14)
        fechaSal = datetime(2015,1,20,16)
        tar = Tarifa(Decimal((2**32)-1),Decimal((2**32)-1))
        
        self.assertEquals(-1,CalcularTotal(fechaIng,fechaSal,tar))
        
    def testCambioAnio(self):
        fechaIng = datetime(2015,12,31,20)
        fechaSal = datetime(2016,1,1,5)
        tar = Tarifa(Decimal(10),Decimal(20))
        
        self.assertEquals(180,CalcularTotal(fechaIng,fechaSal,tar))
        
    
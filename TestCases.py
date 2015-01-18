'''
Created on Jan 14, 2015

@author: Jorge Marcano 11-10566
@author: Maria Victoria Jorge 11-10495
'''

import unittest
from Main import *

class TestCalcularTotal(unittest.TestCase):
    
    # Casos Invalidos
    def testFinalMenorQueInicial(self):
        fechaIng = datetime(2015,1,18,17,0)
        fechaSal = datetime(2015,1,17,17,0)
        tar = Tarifa(Decimal(10),Decimal(20))
        self.assertEquals(CalcularTotal(fechaIng, fechaSal, tar),-1)
        
    def testReservaMenorQue15(self):
        fechaIng = datetime(2015,2,10,14,0)
        fechaSal = datetime(2015,2,10,14,14)
        tar = Tarifa(Decimal(20),Decimal(20))
        self.assertEquals(CalcularTotal(fechaIng, fechaSal, tar),-1)
     
    def testReservaMayorQue72(self):
        fechaIng = datetime(2015,2,1,10,0)
        fechaSal = datetime(2015,2,4,10,1)
        tar = Tarifa(Decimal(20),Decimal(10))
        self.assertEquals(CalcularTotal(fechaIng, fechaSal, tar),-1)  
        
    def testTarifaNegativa(self):
        fechaIng = datetime(2015,12,20,20,30)
        fechaSal = datetime(2015,12,21,20,35)
        tar = Tarifa(Decimal(-0.1),Decimal(10))
        self.assertEquals(CalcularTotal(fechaIng, fechaSal, tar),-1)  
      
    def testTarifaNoRepresentable(self):
        fechaIng = datetime(2015,12,20,20,30)
        fechaSal = datetime(2015,12,21,20,35)
        maxTar = (2**32)-1
        tar = Tarifa(Decimal(10),Decimal(maxTar + 0.01))
        self.assertEquals(CalcularTotal(fechaIng, fechaSal, tar),-1)              
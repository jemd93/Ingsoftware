'''

@author: Jorge Marcano 11-10566
@author: Maria Victoria Jorge 11-10495

'''

import unittest
from Main import *

class TestCalcularTotal(unittest.TestCase):
    
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
        
    def testEsqTarifaTiempoOverflow(self):
        fechaIng = datetime(2015,3,15,10,0)
        fechaSal = datetime(2015,3,18,10,0)
        maxTar = (2**32)-1 
        tar = Tarifa(Decimal(maxTar),Decimal(10))
        self.assertEquals(CalcularTotal(fechaIng, fechaSal, tar),-1)
        
    def testEsqTarifaTiempoValido(self):
        fechaIng = datetime(2015,3,15,10,0)
        fechaSal = datetime(2015,3,15,10,15)
        maxTar = (2**32)-1 
        tar = Tarifa(Decimal(maxTar),Decimal(10))
        self.assertEquals(CalcularTotal(fechaIng, fechaSal, tar),maxTar)
        
    def testReservaMinimaMixta(self):
        fechaIng = datetime(2015,1,7,17,45)
        fechaSal = datetime(2015,1,7,18,0)
        tar = Tarifa(Decimal(10),Decimal(20))
        self.assertEquals(CalcularTotal(fechaIng, fechaSal, tar),Decimal(10))             

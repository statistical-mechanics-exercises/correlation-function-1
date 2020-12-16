import unittest
from main import *

class UnitTests(unittest.TestCase) :
    def test_avspin(self) :
        for i in range(2,7) :
          for j in range(2^i) :
              num, spins = j, i*[0]
              for k in range(i) :
                 spins[k] = np.floor( num / 2**(4-k) )
                 num = num - spins[k]*2**(4-k)
                 if spins[k]==0 : spins[k] = -1
              self.assertTrue( np.abs(sum(spins)/len(spins)-average_spin(spins) )<1e-7, "The average spin that has been calculated by your program is wrong" )

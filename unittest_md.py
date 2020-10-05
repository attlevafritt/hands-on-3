import sys, unittest
from md import calcenergy
from ase.lattice.cubic import FaceCenteredCubic

class MdTests(unittest.TestCase):

    def test_calcenergy(self):
        #self.assertTrue(True)
        atoms = FaceCenteredCubic(directions=[[1, 0, 0], [0, 1, 0], [0, 0, 1]],
                          symbol="Cu",
                          size=(10, 10, 10),
                          pbc=True)
        
        from asap3 import EMT
        atoms.calc = EMT()
        epot, ekin = calcenergy(a=atoms)
        self.assertAlmostEqual(epot, -0.0006011545839374979)
        self.assertAlmostEqual(ekin, 0)
        # now we didn't use the MaxwellBoltzmannDistribution(..) therefore
        # The energy is initializes to 0.
        # if you want you could 
        # initilize momenta for the atoms themselves.



if __name__ == '__main__':
    tests = [unittest.TestLoader().loadTestsFromTestCase(MdTests)]
    testsuite = unittest.TestSuite(tests)
    result = unittest.TextTestRunner(verbosity=0).run(testsuite)
    sys.exit(not result.wasSuccessful())  

    
    


    

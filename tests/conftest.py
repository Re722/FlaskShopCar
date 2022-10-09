from pickle import TRUE
import unittest

from app import Cars

class TestCars(unittest.TestCase):
    def test_hello_world(self):
        self.assertEqual(Cars.owner('jose','jose',msg = TRUE))
        self.assert_(Cars.models=='hatch')

if __name__=='__name__':
    unittest.main()



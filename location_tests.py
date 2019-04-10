import unittest
from location import *
from math import *



class TestLab1(unittest.TestCase):

    def test_repr(self):
        loc = Location("SLO", 35.3, -120.7)
        self.assertEqual(repr(loc),"Location('SLO', 35.3, -120.7)")

    def test_repr_Same(self):
        loc1 = Location("Bakersfield", 30.43, -134.43)
        loc2 = Location("Bakersfield", 30.43, -134.43)
        self.assertEqual(repr(loc1), repr(loc2))

    def test_repr_TwoSame(self):
        """same location and lat but different lon"""
        loc1 = Location("SanDiego", 100, 150)
        loc2 = Location("SanDiego", 100, 140)
        assert not repr(loc1) == repr(loc2)
        """same location and lon but different lat"""
        loc3 = Location("India", 123, 200)
        loc4 = Location("India", 144, 200)
        assert not repr(loc3) == repr(loc4)
        """same lat and lon but different Location"""
        loc5 = Location("Canada", -133, -123)
        loc6 = Location("NotCanada", -133, -123)
        assert not repr(loc5) == repr(loc6)

    def test_repr_signDifference(self):
        """all values the same but signs are different"""
        loc1 = Location("California", -140, -230)
        loc2 = Location("California", 140, 230)
        assert not repr(loc1) == repr(loc2)
        loc3 = Location("China", 36.43, 37.46)
        loc4 = Location("China", -36.43, -37.46)
        assert not repr(loc3) == repr(loc4)

    def test_repr_closeDecimalValuesnotSame(self):
        loc1 = Location("China", 30.44, 60.77)
        loc2 = Location("China", 30.45, 60.78)
        #self.assertEqual((loc1), (loc2))
        assert not repr(loc1) == repr(loc2)
        loc12 = Location("Finland", 40.000, -50.22)
        loc13 = Location("Finland", 40.00, -50.2200)
        self.assertEqual(repr(loc12), repr(loc13))
        loc22 = Location("France", 40.0000000, 36.000000)
        loc33 = Location("France", 40.0, 36.0)
        self.assertEqual(repr(loc22), repr(loc33))

    def test_repr(self):
        loc = Location("SLO", 35.3, -120.7)
        self.assertEqual(repr(loc), "Location('SLO', 35.3, -120.7)")
        loc1 = Location("Bakersfield", 30.43, -134.43)
        self.assertEqual(repr(loc1), "Location('Bakersfield', 30.43, -134.43)")
        loc2 = Location("Canada", -133, -123)
        self.assertEqual(repr(loc2),"Location('Canada', -133, -123)")
        loc3 = Location("China", -180.3, -123.9)
        self.assertEqual(repr(loc3), "Location('China', -180.3, -123.9)")



    def test_eq(self):
       # """testing if equal"""
        loc1 = Location("Bakersfield", 30.43, -134.43)
        loc2 = Location("Bakersfield", 30.43, -134.43)
        self.assertEqual(repr(loc1), "Location('Bakersfield', 30.43, -134.43)")
       # print(repr(loc1))
       # print("Location('Bakersfield', 30.43, -134.43)")

        """same location and lat but different lon"""
        loc10 = Location("SanDiego", 100, 150)
        loc20 = Location("SanDiego", 100, 140)
        assert not repr(loc10) == "Location('SanDiego', 100, 140)"

        """same location and lon but different lat"""
        loc3 = Location("India", 123, 200)
        loc4 = Location("India", 144, 200)
        assert not repr(loc3) == "Location('India', 144, 200)"

        """same lat and lon but different Location"""
        loc5 = Location("Canada", -133, -123)
        loc6 = Location("NotCanada", -133, -123)
        assert not repr(loc5) == "Location('NotCanada', -133, -123)"
        loc7 = loc1
        loc8 = loc7
        loc9 = loc20
        loc12 = 342
        """same values but different signs"""
        loc13 = Location("NewYork", 140, 36.78)
        #self.assertEqual(repr(loc13), "Location('NewYork', 140, 36.78)")
        assert not repr(loc13) == "Location('NewYork', -140, -36.78)"
        self.assertEqual(loc1 == loc2, True)
        self.assertEqual(loc1 == loc10, False)
        self.assertEqual(loc10 == loc20, False)
        self.assertEqual(loc3 == loc4, False)
        self.assertEqual(loc7 == loc1, True)
        self.assertEqual(loc7 == loc8, True)
        self.assertEqual(loc8 == loc1, True)
        self.assertEqual(loc9 == loc20, True)
        self.assertEqual(loc9 == loc10, False)
        self.assertEqual(loc5 == loc6, False)
        self.assertEqual(loc1 == loc12, False)
        self.assertEqual(loc2 == loc12, False)

        #print(type(loc1) == Location)
        #print(loc1.name == loc2.name)
        #print(isclose(loc1.lat, loc2.lat))
        #print(isclose(loc1.lon, loc2.lon))









    # Add more tests!

if __name__ == "__main__":
        unittest.main()

import unittest
from lab1 import *

 # A few test cases.  Add more!!!
class TestLab1(unittest.TestCase):

    def test_max_list_iter(self):
        """when list is None"""
        tlist = None
        with self.assertRaises(ValueError):  # used to check for exception
            max_list_iter(tlist)


    def test_max_list_increasing(self):
        """increasing order"""
        self.assertEqual(max_list_iter([10, 11, 12, 13, 14]), 14)


    def test_max_list_decreasing(self):
        """decreasing order"""
        self.assertEqual(max_list_iter([9, 8, 7, 6, 5]), 9)


    def test_max_list_same(self):
        """same number"""
        self.assertEqual(max_list_iter([23, 23, 23, 23, 23]), 23)


    def test_max_list_duplicates(self):
        """duplicates of max value at start"""
        self.assertEqual(max_list_iter([40, 40, 40, 1, 1]), 40)
        self.assertEqual(max_list_iter([50, 50, 2, 2]), 50)
        self.assertEqual(max_list_iter([-1, -1, -2]), -1)
        """duplicates of max value at end"""
        self.assertEqual(max_list_iter([2, 5, 3, 7, 7, 7, 7]), 7)
        self.assertEqual(max_list_iter([-39, -38, -38, 0, 0]), 0)
        """one max value at start but duplicates of min value"""
        self.assertEqual(max_list_iter([19, 0, 0, 0, 0, 0, 0]), 19)
        self.assertEqual(max_list_iter([-1, -10, -10, -10, -10, -10, -10]), -1)
        """max value at end but duplicates of min value"""
        self.assertEqual(max_list_iter([1, 1, 1, 1, 1, 1, 230]), 230)
        self.assertEqual(max_list_iter([168, 168, 168, 168, 168, 168, 760]), 760)

        """max value in middle"""
        self.assertEqual(max_list_iter([1, 1, 5, 5, 5, 3, 3, 3]), 5)
        self.assertEqual(max_list_iter([-100, -100, 34, 34, 34, 32, 32, 32]), 34)


    def test_max_list_alternating(self):
        """alternating values"""
        self.assertEqual(max_list_iter([9, 8, 9, 8, 9, 8, 9]), 9)
        self.assertEqual(max_list_iter([5, 6, 5, 6]), 6)
        """alternating between negative and positive values that are the same"""
        self.assertEqual(max_list_iter([-15, 15, -15, 15, -15, 15]), 15)


    def test_max_list_emptylist(self):
        """empty list"""
        self.assertEqual(max_list_iter([]), None)


    def test_max_list_single(self):
        """list with single value"""
        self.assertEqual(max_list_iter([0]), 0)
        self.assertEqual(max_list_iter([-243]), -243)
        self.assertEqual(max_list_iter([33329]), 33329)


    def test_max_list_absolute(self):
        """checks if negative sign is taken into account when comparing values"""
        self.assertEqual(max_list_iter([23243, 0]), 23243)
        self.assertEqual(max_list_iter([23, -397243]), 23)
        self.assertEqual(max_list_iter([-2243, -1]), -1)


    def test_reverse_rec_increasing(self):
        """reverse increasing list"""
        self.assertEqual(reverse_rec([1]), [1])
        self.assertEqual(reverse_rec([1, 2, 3]),[3, 2, 1])
        self.assertEqual(reverse_rec([5, 6, 7]), [7, 6, 5])
        self.assertEqual(reverse_rec([8, 18, 100, 1231, 1222]), [1222, 1231, 100, 18, 8])
        """negative values"""
        self.assertEqual(reverse_rec([-5, -4, -3, -2, -1]), [-1, -2, -3, -4, -5])


    def test_reverse_rec_decreasing(self):
        """reverse decreasing order"""
        self.assertEqual(reverse_rec([9, 8, 7, 6, 5]), [5, 6, 7, 8, 9])
        self.assertEqual(reverse_rec([12, 11, 10, 9, 8]), [8, 9, 10, 11, 12])
        """negative values"""
        self.assertEqual(reverse_rec([-11, -22, -33, -44, -55]), [-55, -44, -33, -22, -11])

    def test_reverse_rec_single(self):
        self.assertEqual(reverse_rec([1]), [1])
        self.assertEqual(reverse_rec([0]), [0])
        self.assertEqual(reverse_rec([]), [])
        self.assertEqual(reverse_rec([1]), [1])


    def test_reverse_rec_NoneFound(self):
        with self.assertRaises(ValueError):
            reverse_rec(None)

    #def test_reverse_rec_NoneFound1(self):
    #    self.assertRaises(ValueError, reverse_rec(None))

    def test_reverse_rec_ListlengthisZero(self):
        self.assertEqual(reverse_rec([]), [])

    def test_reverse_rec_Palindrome(self):
        self.assertEqual(reverse_rec([4,3,2,2,3,4]), [4,3,2,2,3,4])
        self.assertEqual(reverse_rec([3, 2, 2, 3]), [3, 2, 2, 3])
        self.assertEqual(reverse_rec([-1,2,2,-1]), [-1,2,2,-1])


    def test_bin_search(self):
        list_val = [0, 1, 2, 3, 4, 7, 8, 9, 10]
        low = 0
        high = len(list_val)-1
        #self.assertEqual(bin_search(4, 0, len(list_val)-1, list_val), 4 )
        self.assertEqual(bin_search(4, low, high, list_val), 4)


    def test_bin_search_startingValue(self):
        list_val = [56, 59, 543, 689, 987, 43543, 445435]
        low = 0
        high = len(list_val) - 1
        self.assertEqual(bin_search(56, low, high, list_val), 0)

    def test_bin_search_lastValue(self):
        list_val = [1, 114, 134, 143, 144, 155, 176, 188, 198, 1900]
        low = 0
        high = len(list_val) - 1
        self.assertEqual(bin_search(1900, low, high, list_val), 9)

    def test_bin_search_MiddleValue(self):
        list_val = [10, 11, 12, 13, 14, 15, 16, 18, 18, 19]
        low = 0
        high = len(list_val) - 1
        self.assertEqual(bin_search(15, low, high, list_val), 5)

    def test_bin_search_EvenArray(self):
        list_val = [104, 115, 126, 173, 1444, 1555, 1678, 1897, 18777, 1978856]
        low = 0
        high = len(list_val) - 1
        self.assertEqual(bin_search(1897, low, high, list_val), 7)
        list_val1 = [1, 2, 3, 4, 5, 6]
        low1 = 0
        high1 = len(list_val1) - 1
        self.assertEqual(bin_search(2, low1, high1, list_val1), 1)

    def test_bin_search_OddArray(self):
        list_val = [96, 114, 124, 133, 145, 156, 167, 189, 198]
        low = 0
        high = len(list_val) - 1
        self.assertEqual(bin_search(133, low, high, list_val), 3)
        list_val1 = [1, 2, 3, 4, 5]
        low1 = 0
        high1 = len(list_val1) - 1
        self.assertEqual(bin_search(2, low1, high1, list_val1), 1)

    def test_bin_search_notFound(self):
        list_val = [10, 11, 12, 13, 14, 15, 16, 18, 18, 19]
        low = 0
        high = len(list_val) - 1
        self.assertEqual(bin_search(15453, low, high, list_val), None)

    def test_bin_search_differntLowHighValues(self):
        list_val = [10, 11, 12, 13, 14, 15, 16, 18, 18, 19]
        low = 2
        high = 4
        self.assertEqual(bin_search(14, low, high, list_val), 4)
        list_val = [10, 11, 12, 13, 14, 15, 16, 1233, 1823, 1933]
        low = 8
        high = 8
        self.assertEqual(bin_search(1823, low, high, list_val), 8)
        """special case when low value is greater than high"""
        list_val = [10, 11, 12, 13, 14, 15, 16, 1233, 1823, 1933]
        low = 10
        high = 2
        self.assertEqual(bin_search(10, low, high, list_val), None)
        """case in which low and high are the same and only one value"""
        list_val = [10]
        low = 0
        high = 0
        self.assertEqual(bin_search(10, low, high, list_val), 0)

    def test_bin_search_NoneInput(self):
        with self.assertRaises(ValueError):
            bin_search(100, 0, 10, None)


if __name__ == "__main__":
    unittest.main()

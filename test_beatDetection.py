import unittest
from beatDetection import *


class MyTestCase(unittest.TestCase):
    def test_getMax(self):
        arr = [100, 101, 102, 103, 104, 105, 106, 107, 108, 109, 110, 120, 122, 123, 124, 125, 126, 127, 128, 129]

        max = get_max_and_min_in_raw_data(arr)[0]
        min = get_max_and_min_in_raw_data(arr)[1]

        self.assertEqual(max, 129)
        self.assertEqual(min, 100)

if __name__ == '__main__':
    unittest.main()

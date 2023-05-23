import unittest
from beatDetection import *


class MyTestCase(unittest.TestCase):

    def test_moving_average(self):
        arr = [1, 2, 3, 4]
        window_size = 2
        result = [1.5, 2.5, 3.5]

        self.assertEqual(moving_average(arr, window_size), result)

if __name__ == '__main__':
    unittest.main()

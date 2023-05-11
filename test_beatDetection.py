import unittest
from beatDetection import *


class MyTestCase(unittest.TestCase):
    def test_getMax_1(self):
        arr = [100, 101, 102, 103, 104, 105, 106, 107, 108, 109, 110, 120, 122, 123, 124, 125, 126, 127, 128, 129]

        max = get_max_and_min_in_raw_data(arr)[0]
        min = get_max_and_min_in_raw_data(arr)[1]

        self.assertEqual(max, 129)
        self.assertEqual(min, 100)

    def test_getMax_2(self):
        arr = [100]

        max = get_max_and_min_in_raw_data(arr)[0]
        min = get_max_and_min_in_raw_data(arr)[1]

        self.assertEqual(max, 100)
        self.assertEqual(min, 100)

    def test_getMax_3(self):
        arr = []

        max = get_max_and_min_in_raw_data(arr)[0]
        min = get_max_and_min_in_raw_data(arr)[1]

        self.assertEqual(max, -1)
        self.assertEqual(min, -1)

    def test_getting_indices_between_value_and_buffer_1(self):
        arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        max = get_max_and_min_in_raw_data(arr)[0]
        self.assertEqual(max, 10)
        self.assertEqual(max * .2, 2)

        result = getting_indices_between_value_and_buffer(arr, max, max * .2)
        self.assertEqual(result, [1, 2, 3, 4, 5, 6, 7, 8, 9]) # indicies

    def test_getting_indices_between_value_and_buffer_2(self):
        arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        max = get_max_and_min_in_raw_data(arr)[0]
        self.assertEqual(max, 10)
        self.assertEqual(max * .2, 2)

        result = getting_indices_between_value_and_buffer(arr, max, max * .2)

        # testing to make sure values align between indices and arr values
        for i in range(len(result)):
            self.assertEqual(arr[result[i]], i + 2)


if __name__ == '__main__':
    unittest.main()

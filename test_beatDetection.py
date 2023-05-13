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
        self.assertEqual(result, [1, 2, 3, 4, 5, 6, 7, 8, 9])  # indicies

    def test_getting_indices_between_value_and_buffer_2(self):
        arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        max = get_max_and_min_in_raw_data(arr)[0]
        self.assertEqual(max, 10)
        self.assertEqual(max * .2, 2)

        result = getting_indices_between_value_and_buffer(arr, max, max * .2)

        # testing to make sure values align between indices and arr values
        for i in range(len(result)):
            self.assertEqual(arr[result[i]], i + 2)

    def test_getting_indices_between_value_and_buffer_3(self):
        arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        max = get_max_and_min_in_raw_data(arr)[0]
        self.assertEqual(max, 10)
        buffer = max * .8
        self.assertEqual(buffer, 8)

        result = getting_indices_between_value_and_buffer(arr, max, buffer)

        self.assertEqual(result, [7, 8, 9])

    def test_averaging_noise(self):
        arr = [100, 105, 110, 45, 55, 65, 120, 118, 34, 56, 101, 103, 98]
        max = get_max_and_min_in_raw_data(arr)[0]
        buffer = max * 0.8
        self.assertEqual(max, 120)
        self.assertEqual(buffer, 96)
        horizontal_cleaning_max = getting_indices_between_value_and_buffer(arr, max, buffer)
        self.assertEqual(horizontal_cleaning_max, [0, 1, 2, 6, 7, 10, 11, 12])

        average_noise = averaging_noise(horizontal_cleaning_max)

        self.assertEqual(average_noise, [1.0, 6.5, 11])


if __name__ == '__main__':
    unittest.main()

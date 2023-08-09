""" Design a function that takes a list of numerical data and performs calculations for mean, median and standard deviation. 
Write unit tests to verify the correctness of the statistical calculations for various inputs, including edge cases like an 
empty list or a list with one element (Use unittest module). """

import unittest
import statistics
import math

def calculate_stats(data):
    if not data:
        return None

    mean = sum(data) / len(data)
    median = statistics.median(data)
    variance = sum((x - mean) ** 2 for x in data) / len(data)
    std_dev = math.sqrt(variance)

    return {'mean': mean, 'median': median, 'std_dev': std_dev}

class TestStatisticsCalculation(unittest.TestCase):
    def test_empty_list(self):
        result = calculate_stats([])
        self.assertIsNone(result)

    def test_single_element_list(self):
        result = calculate_stats([5])
        expected_result = {'mean': 5.0, 'median': 5.0, 'std_dev': 0.0}
        self.assertEqual(result, expected_result)

    def test_multiple_elements(self):
        result = calculate_stats([1, 2, 3, 4, 5])
        self.assertEqual(result['mean'], 3.0)
        self.assertEqual(result['median'], 3.0)
        self.assertEqual(result['std_dev'], 1.4142135623730951)

if __name__ == '__main__':
    unittest.main()


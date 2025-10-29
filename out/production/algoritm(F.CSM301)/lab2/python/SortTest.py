import unittest
from Sorts import insertion_sort, merge_sort, binary_search, find_max

class TestAlgorithms(unittest.TestCase):
    def test_insertion_sort(self):
        self.assertEqual(insertion_sort([5, 2, 4, 6, 1]), [1, 2, 4, 5, 6])
        self.assertEqual(insertion_sort([]), [])
        self.assertEqual(insertion_sort([1]), [1])

    def test_merge_sort(self):
        self.assertEqual(merge_sort([5, 2, 4, 6, 1]), [1, 2, 4, 5, 6])
        self.assertEqual(merge_sort([3, 3, 3]), [3, 3, 3])
        self.assertEqual(merge_sort([]), [])

    def test_binary_search_found(self):
        sorted_arr = [1, 2, 3, 4, 5]
        self.assertEqual(binary_search(sorted_arr, 3), 2)
        self.assertEqual(binary_search(sorted_arr, 1), 0)
        self.assertEqual(binary_search(sorted_arr, 5), 4)

    def test_binary_search_not_found(self):
        sorted_arr = [1, 2, 3, 4, 5]
        self.assertEqual(binary_search(sorted_arr, 6), -1)
        self.assertEqual(binary_search(sorted_arr, 0), -1)

    def test_find_max(self):
        self.assertEqual(find_max([1, 9, 3, 7]), 9)
        self.assertEqual(find_max([5]), 5)
        self.assertEqual(find_max([-10, -5, -20]), -5)

if __name__ == '__main__':
    unittest.main()
import unittest
from insertion_sort import *
import random


class TestInsertionSort(unittest.TestCase):
    def test_sort(self):
        tab = [2, 1]
        tab1 = [5, 3, 1, 2]
        self.assertEqual([1, 2], sort(tab))
        self.assertEqual([], sort([]))
        self.assertEqual([1, 2, 3, 5], sort(tab1))

    def test_sort_random(self):
        tab1 = []
        tab2 = []
        for i in range(100):
            number = random.randint(0, 10000)
            tab1.append(number)
            tab2.append(number)

            tab1 = sort(tab1)
            tab2.sort()
            self.assertEqual(tab1, tab2)


if __name__ == '__main__':
    unittest.main()

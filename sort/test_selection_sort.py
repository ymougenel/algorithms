import random

import selection_sort
import unittest


class TestSelectionSort(unittest.TestCase):

    def testSelectionSort(self):
        tab = [2, 1]
        tab1 = [2, 1, 0]
        self.assertEqual(tab, selection_sort.sort(tab))
        self.assertEqual([0, 1, 2], selection_sort.sort(tab1))

    def testSelectionSortRandom(self):
        for k in range(20):
            tab1 = []
            tab2 = []
            for i in range(1000):
                nb = random.randint(0, 10000)
                tab1.append(nb)
                tab2.append(nb)
            tab1 = selection_sort.sort(tab1)
            tab2.sort()
            self.assertEqual(tab2, tab1)

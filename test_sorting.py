"""Tests for the quicksort implementation in sorting.py."""

import random
import unittest

from sorting import quicksort


class QuicksortTest(unittest.TestCase):
    def test_empty(self):
        self.assertEqual(quicksort([]), [])

    def test_single_element(self):
        self.assertEqual(quicksort([42]), [42])

    def test_already_sorted(self):
        self.assertEqual(quicksort([1, 2, 3, 4, 5]), [1, 2, 3, 4, 5])

    def test_reverse_sorted(self):
        self.assertEqual(quicksort([5, 4, 3, 2, 1]), [1, 2, 3, 4, 5])

    def test_duplicates(self):
        self.assertEqual(quicksort([3, 1, 3, 1, 2, 3]), [1, 1, 2, 3, 3, 3])

    def test_negatives_and_floats(self):
        self.assertEqual(quicksort([2.5, -1, 0, -3.5, 7]), [-3.5, -1, 0, 2.5, 7])

    def test_strings(self):
        self.assertEqual(quicksort(["pear", "apple", "fig"]),
                         ["apple", "fig", "pear"])

    def test_input_not_mutated(self):
        original = [3, 1, 2]
        quicksort(original)
        self.assertEqual(original, [3, 1, 2])

    def test_random_against_builtin(self):
        rng = random.Random(20261102)
        for _ in range(50):
            data = [rng.randint(-1000, 1000) for _ in range(rng.randint(0, 200))]
            self.assertEqual(quicksort(data), sorted(data))


if __name__ == "__main__":
    unittest.main()

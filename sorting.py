"""Sorting algorithms implemented in Python.

This module implements ``quicksort``, a comparison-based sorting algorithm
with an average time complexity of O(n log n) and O(log n) auxiliary stack
space on average.
"""

from __future__ import annotations

import random
from typing import List, Sequence, TypeVar

T = TypeVar("T")


def quicksort(items: Sequence[T]) -> List[T]:
    """Return a new list with the items of ``items`` in ascending order.

    The original sequence is left untouched. The sort is not stable:
    equal elements may be reordered.

    Example:
        >>> quicksort([3, 1, 2])
        [1, 2, 3]

    Args:
        items: Any sequence of mutually comparable items.

    Returns:
        A sorted copy of ``items`` as a list.
    """
    result = list(items)
    _quicksort_inplace(result, 0, len(result) - 1)
    return result


def _quicksort_inplace(items: List[T], low: int, high: int) -> None:
    """Sort ``items[low:high + 1]`` in place using randomized quicksort."""
    while low < high:
        pivot_index = _partition(items, low, high)
        # Recurse into the smaller half first so the stack stays O(log n).
        if pivot_index - low < high - pivot_index:
            _quicksort_inplace(items, low, pivot_index - 1)
            low = pivot_index + 1
        else:
            _quicksort_inplace(items, pivot_index + 1, high)
            high = pivot_index - 1


def _partition(items: List[T], low: int, high: int) -> int:
    """Partition ``items[low:high + 1]`` around a random pivot.

    After partitioning, every element left of the returned index is less
    than or equal to the pivot and every element right of it is greater.
    The pivot ends up at its final position, which is returned.
    """
    # Random pivot avoids the O(n^2) worst case on already sorted input.
    pivot_index = random.randint(low, high)
    items[pivot_index], items[high] = items[high], items[pivot_index]
    pivot = items[high]

    store_index = low
    for index in range(low, high):
        if items[index] <= pivot:
            items[store_index], items[index] = items[index], items[store_index]
            store_index += 1

    items[store_index], items[high] = items[high], items[store_index]
    return store_index


if __name__ == "__main__":
    sample = [5, 2, 9, 1, 5, 6, 0, -3]
    print("Before:", sample)
    print("After: ", quicksort(sample))

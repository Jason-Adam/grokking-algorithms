#!/usr/bin env python

from math import floor
from typing import List, Tuple


def binary_search(sorted_list: List[int], item: int) -> Tuple[int, int]:
    """Determines index location of given item in a sorted list.

        Parameters
        ----------
        sorted_list: list
            Pre-sorted list of integers that search
            will be performed on.
        item: int
            Number to search for in the list.

        Returns
        -------
        Tuple[int, int]
            Tuple containing index of item and steps
            required during search.
    """
    low: int = 0
    high: int = len(sorted_list) - 1
    steps: int = 0
    while low <= high:
        mid: int = floor((low + high) / 2)
        guess: int = sorted_list[mid]
        if guess == item:
            steps += 1
            return mid, steps
        elif guess > item:
            steps += 1
            high = mid - 1
        else:
            steps += 1
            low = mid + 1
    return None, None


if __name__ == "__main__":
    sorted_list = [1, 3, 5, 7, 9, 11, 12, 14, 22, 34, 65]
    item_index, steps = binary_search(sorted_list, 34)
    print("List length = {}".format(len(sorted_list)))
    print("Item index = {}".format(item_index))
    print("Total steps = {}".format(steps))

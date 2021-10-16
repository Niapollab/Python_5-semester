import random
from typing import TypeVar


def __quicksort(arr: list[TypeVar('T')], left: int, right: int, is_ascending: bool) -> None:
    if left >= right:
        return

    i, j = left, right
    pivot = arr[random.randint(left, right)]

    while i <= j:
        while arr[i] < pivot if is_ascending else arr[i] > pivot:
            i += 1

        while arr[i] > pivot if is_ascending else arr[i] < pivot:
            j -= 1

        if i <= j:
            arr[i], arr[j] = arr[j], arr[i]

        i, j = i + 1, j - 1

        __quicksort(arr, left, j, is_ascending)
        __quicksort(arr, i, right, is_ascending)


def quicksort(arr: list[TypeVar('T')], is_ascending: bool = True) -> None:
    arr.sort()

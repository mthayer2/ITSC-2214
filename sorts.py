"""
Sorting Algorithms
==================
This module contains implementations of common sorting algorithms.
Each function sorts a list of comparable elements.

Usage:
    from sorts import insertion_sort, merge_sort, heap_sort, quick_sort

Students: You must implement insertion_sort yourself. The remaining
algorithms are provided for reference — read through them to see how
each one works. You will study these algorithms in depth later in
the course.
"""

import heapq


# ---------------------------------------------------------------------------
# TODO: Implement this function
# ---------------------------------------------------------------------------

def insertion_sort(a_list):
    """Sort *a_list* in-place using the insertion sort algorithm.

    Insertion sort works like sorting a hand of playing cards:
      - Pick up one card at a time (starting from the second element).
      - Compare it to the cards already in your hand (the sorted portion).
      - Shift cards that are larger to the right to make room.
      - Insert the card into its correct position.

    Parameters
    ----------
    a_list : list
        The list to be sorted. Modified in-place.

    Algorithm outline:
      1. Loop through the list starting at index 1.
      2. Save the current element as `current_value`.
      3. Walk backward through the sorted portion, shifting each element
         that is greater than `current_value` one position to the right.
      4. Place `current_value` into the gap.

    Performance:
      - Best case:  O(n)   — the list is already sorted.
      - Worst case: O(n^2) — the list is in reverse order.
    """
    # TODO: Implement insertion sort here
    pass


# ---------------------------------------------------------------------------
# Provided implementations — read but do not modify
# ---------------------------------------------------------------------------

def merge_sort(a_list):
    """Return a new sorted list using the merge sort algorithm.

    Merge sort is a divide-and-conquer algorithm:
      1. Split the list in half.
      2. Recursively sort each half.
      3. Merge the two sorted halves into one sorted list.

    Unlike insertion sort, merge sort does NOT sort in-place — it builds
    and returns a new list, leaving the original unchanged.

    Parameters
    ----------
    a_list : list
        The list to sort. The original is not modified.

    Returns
    -------
    list
        A new list containing the same elements in sorted order.

    Performance:
      - All cases: O(n log n)
      - The list is split in half log(n) times, and each level of
        splitting requires n comparisons to merge back together.
    """

    # Base case: a list with 0 or 1 elements is already sorted.
    if len(a_list) <= 1:
        return list(a_list)

    # --- Split phase ---
    # Find the midpoint and divide the list into two halves.
    midpoint = len(a_list) // 2
    left_half = merge_sort(a_list[:midpoint])    # recursively sort left
    right_half = merge_sort(a_list[midpoint:])   # recursively sort right

    # --- Merge phase ---
    # Walk through both sorted halves, always picking the smaller element.
    merged_list = []
    left_index = 0
    right_index = 0

    # Compare elements from each half and append the smaller one.
    # This loop runs at most n times (once per element in the two halves).
    while left_index < len(left_half) and right_index < len(right_half):
        if left_half[left_index] <= right_half[right_index]:
            merged_list.append(left_half[left_index])
            left_index += 1
        else:
            merged_list.append(right_half[right_index])
            right_index += 1

    # One half may have remaining elements — append them all.
    merged_list.extend(left_half[left_index:])
    merged_list.extend(right_half[right_index:])

    return merged_list


def heap_sort(a_list):
    """Sort *a_list* in-place using the heap sort algorithm.

    Heap sort works in two phases:
      1. Build a min-heap from the list. A heap is a special tree structure
         where every parent is smaller than its children, so the smallest
         element is always at the top (index 0).
      2. Repeatedly remove the smallest element from the heap, which
         gives us the elements in sorted order.

    This implementation uses Python's built-in `heapq` module, which
    provides efficient heap operations.

    Parameters
    ----------
    a_list : list
        The list to be sorted. Modified in-place.

    Performance:
      - All cases: O(n log n)
      - Building the heap takes O(n), and each of the n removals
        takes O(log n) to maintain the heap property.
    """

    # Phase 1: Rearrange the list into a valid min-heap.
    # After this call, a_list[0] is the smallest element.
    heapq.heapify(a_list)

    # Phase 2: Pop elements one at a time from the heap.
    # Each heappop removes the smallest remaining element in O(log n).
    # We do this n times, so this loop runs n iterations total.
    sorted_values = []
    for _ in range(len(a_list)):
        sorted_values.append(heapq.heappop(a_list))

    # Copy the sorted values back into the original list.
    a_list[:] = sorted_values


def quick_sort(a_list):
    """Sort *a_list* in-place using the quick sort algorithm.

    Quick sort is a divide-and-conquer algorithm:
      1. Choose a "pivot" element.
      2. Partition the list so that all elements less than or equal to
         the pivot are on the left, and all greater elements are on the right.
      3. Recursively sort the left and right partitions.

    Parameters
    ----------
    a_list : list
        The list to be sorted. Modified in-place.

    Performance:
      - Average case: O(n log n)
      - Worst case:   O(n^2) — occurs when the pivot is always the
        smallest or largest element (e.g., already sorted input).
    """
    _quick_sort_recursive(a_list, 0, len(a_list) - 1)


def _quick_sort_recursive(a_list, low_index, high_index):
    """Recursively sort a_list[low_index..high_index].

    At each level of recursion, the partition step places one element
    (the pivot) into its final sorted position, then we recurse on
    the two sub-lists on either side of the pivot.
    """
    if low_index < high_index:
        # Partition the sub-list and get the final position of the pivot.
        pivot_position = _partition(a_list, low_index, high_index)

        # Recursively sort the elements before and after the pivot.
        _quick_sort_recursive(a_list, low_index, pivot_position - 1)
        _quick_sort_recursive(a_list, pivot_position + 1, high_index)


def _partition(a_list, low_index, high_index):
    """Partition a_list[low_index..high_index] around a pivot.

    Uses the last element as the pivot. After partitioning:
      - All elements at indices <= pivot_position are <= pivot.
      - All elements at indices >  pivot_position are >  pivot.

    Returns the final index of the pivot element.

    This loop iterates through every element in the sub-list once,
    so partition runs in O(n) time where n is the sub-list size.
    """
    pivot_value = a_list[high_index]

    # boundary_index tracks where the next "small" element should go.
    boundary_index = low_index - 1

    # Walk through every element except the pivot.
    # If an element is <= the pivot, swap it into the "small" side.
    for current_index in range(low_index, high_index):
        if a_list[current_index] <= pivot_value:
            boundary_index += 1
            a_list[boundary_index], a_list[current_index] = (
                a_list[current_index], a_list[boundary_index]
            )

    # Place the pivot into its correct sorted position.
    a_list[boundary_index + 1], a_list[high_index] = (
        a_list[high_index], a_list[boundary_index + 1]
    )

    return boundary_index + 1

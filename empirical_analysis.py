"""
Empirical Analysis of Sorting Algorithms
=========================================
ITSC 2214 - Data Structures

This lab measures the wall-clock runtime of five sorting algorithms
across a range of input sizes, averages multiple trials, and produces
a comparative graph.

Instructions
------------
Complete the four sorting functions marked with TODO below.
Do NOT modify the benchmarking, graphing, or main logic.
"""

import time
import random
import heapq
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt


# ---------------------------------------------------------------------------
# Sorting Algorithms — Complete these four functions
# ---------------------------------------------------------------------------

def insertion_sort(lst):
    """Sort *lst* in-place using insertion sort.

    Algorithm:
        - Iterate from index 1 to len(lst) - 1.
        - For each index, save the current value as `key`.
        - Shift elements that are greater than `key` one position to the right.
        - Place `key` in the correct position.

    Must modify the list in-place (do not return a new list).
    """
    # TODO: Implement insertion sort
    pass


def merge_sort(lst):
    """Return a **new** sorted list using merge sort.

    Algorithm:
        - Base case: a list of length 0 or 1 is already sorted — return it.
        - Split the list into two halves.
        - Recursively sort each half.
        - Merge the two sorted halves into a single sorted list and return it.

    This function should NOT modify the original list.
    """
    # TODO: Implement merge sort
    pass


def heap_sort(lst):
    """Sort *lst* in-place using heap sort via the heapq module.

    Algorithm:
        - Use heapq.heapify(lst) to turn lst into a min-heap in-place.
        - Pop all elements from the heap into a temporary list using heapq.heappop().
        - Copy the sorted elements back into lst.

    Must modify the list in-place (do not return a new list).
    """
    # TODO: Implement heap sort
    pass


def quick_sort(lst):
    """Sort *lst* in-place using quick sort.

    Algorithm:
        - Base case: if the list has 0 or 1 elements, return.
        - Choose a pivot (e.g., the last element).
        - Partition the remaining elements into two groups:
          those less than or equal to the pivot, and those greater.
        - Recursively sort each group.
        - Write the sorted result back into lst.

    Must modify the list in-place (do not return a new list).
    """
    # TODO: Implement quick sort
    pass


def builtin_sort(lst):
    """Sort using Python's built-in Timsort. (Do NOT modify this function.)"""
    lst.sort()


# ---------------------------------------------------------------------------
# Benchmarking — Do NOT modify anything below this line
# ---------------------------------------------------------------------------

def generate_random_list(size):
    """Return a list of *size* random integers."""
    return [random.randint(1, size * 10) for _ in range(size)]


def benchmark(sort_func, data, copies_input=False):
    """Time a single execution of *sort_func* on a copy of *data*.

    Parameters
    ----------
    sort_func : callable
        A sorting function. If it returns a new list (like merge_sort),
        set *copies_input* to True.
    data : list
        The unsorted input data. A fresh copy is made before each call
        so the original is never modified.
    copies_input : bool
        True if the sort function returns a new list instead of sorting
        in-place.

    Returns
    -------
    float
        Elapsed time in seconds.
    """
    lst = list(data)  # fresh copy
    start = time.perf_counter()
    if copies_input:
        _ = sort_func(lst)
    else:
        sort_func(lst)
    end = time.perf_counter()
    return end - start


# Configuration ---------------------------------------------------------------

NUM_TRIALS = 3

# Input sizes for O(n log n) sorts
NLOGN_SIZES = [1_000, 2_000, 4_000, 8_000, 16_000, 32_000,
               64_000, 128_000, 256_000, 512_000]

# Insertion sort stops early because O(n^2) is too slow for large n
INSERTION_MAX = 32_000

ALGORITHMS = [
    ("insertion", insertion_sort, False),
    ("merge",     merge_sort,     True),   # merge_sort returns a new list
    ("heap",      heap_sort,      False),
    ("quick",     quick_sort,     False),
    ("builtin",   builtin_sort,   False),
]


def run_benchmarks():
    """Run all sorting benchmarks and return the results.

    Returns
    -------
    dict
        Mapping of algorithm name -> list of (n, avg_time) tuples.
    """
    results = {name: [] for name, _, _ in ALGORITHMS}

    for n in NLOGN_SIZES:
        # Generate one random dataset per size; copy it for each algorithm
        data = generate_random_list(n)

        row_parts = [f"n={n:>7d}:"]

        for name, func, copies in ALGORITHMS:
            if name == "insertion" and n > INSERTION_MAX:
                continue  # skip insertion sort for large sizes

            trial_times = []
            for _ in range(NUM_TRIALS):
                elapsed = benchmark(func, data, copies)
                trial_times.append(elapsed)

            avg = sum(trial_times) / len(trial_times)
            results[name].append((n, avg))
            row_parts.append(f"{name}={avg:.4f}s")

        print("  ".join(row_parts))

    return results


def plot_results(results):
    """Plot all algorithm runtimes on a single graph and save to PNG."""
    plt.figure(figsize=(10, 6))

    style_map = {
        "insertion": ("o-", "Insertion Sort"),
        "merge":     ("s-", "Merge Sort"),
        "heap":      ("^-", "Heap Sort"),
        "quick":     ("D-", "Quick Sort"),
        "builtin":   ("*-", "Python sorted() [Timsort]"),
    }

    for name, data_points in results.items():
        if not data_points:
            continue
        sizes = [dp[0] for dp in data_points]
        times = [dp[1] for dp in data_points]
        marker, label = style_map[name]
        plt.plot(sizes, times, marker, label=label, markersize=5)

    plt.xlabel("Input Size (n)")
    plt.ylabel("Average Time (seconds)")
    plt.title("Empirical Analysis of Sorting Algorithm Runtimes")
    plt.legend()
    plt.grid(True, alpha=0.3)
    plt.tight_layout()
    plt.savefig("sorting_runtimes.png", dpi=150)
    print("\nGraph saved to sorting_runtimes.png")


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------

def main():
    print(f"Benchmarking sorting algorithms ({NUM_TRIALS} trials each)...\n")
    results = run_benchmarks()
    plot_results(results)


if __name__ == "__main__":
    main()

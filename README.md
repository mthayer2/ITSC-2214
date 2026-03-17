# Lab: Empirical Analysis of Sorting Algorithms

## Overview

In this lab you will **measure and graph the runtimes** of five sorting
algorithms, observe how they scale with input size, and connect your
observations to the Big-O classifications you learned in
**Chapter 2.2 – What Is Algorithm Analysis?**

In Chapter 2.2 you benchmarked three summation algorithms and discovered
that wall-clock time reveals an algorithm's growth rate: *double the input
and see whether the time doubles (linear), quadruples (quadratic), or stays
the same (constant).* This lab applies that same empirical technique to
sorting — a problem where algorithm choice has dramatic real-world impact.

## Sorting Algorithms Under Test

| Algorithm | Expected Big-O | Notes |
|---|---|---|
| Insertion Sort | O(n²) | Simple but slow on large inputs |
| Merge Sort | O(n log n) | Divide-and-conquer, stable |
| Heap Sort | O(n log n) | In-place, uses a heap |
| Quick Sort | O(n log n) average | Fast in practice, O(n²) worst-case |
| Python's built-in `sorted()` | O(n log n) | Timsort — Python's optimized hybrid sort |

## What You Will Do

1. **Implement the sorting algorithms** — Complete the four sorting functions
   in `empirical_analysis.py` (insertion sort, merge sort, heap sort, and
   quick sort). Python's built-in `sorted()` is already provided.

2. **Benchmark each algorithm** — Time each sort across multiple input sizes,
   running **3 trials** per size and averaging the results.

3. **Generate a graph** — Your program will produce a line chart
   (`sorting_runtimes.png`) showing all five algorithms on a single plot.

4. **Answer analysis questions** — Add your answers directly to this README
   in the [Analysis Questions](#analysis-questions) section at the bottom.

## Getting Started

### Prerequisites

- Python 3.12 (required)
- `matplotlib` for graphing

### Setup

```bash
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

### Running the Lab

```bash
python3 empirical_analysis.py
```

This will:
- Run all sorting benchmarks across the configured input sizes
- Print a results table to the terminal
- Save a graph to `sorting_runtimes.png`

### Sample Output

```
Benchmarking sorting algorithms (3 trials each)...

n=   1000: insertion=0.0052s  merge=0.0023s  heap=0.0031s  quick=0.0019s  builtin=0.0001s
n=   2000: insertion=0.0198s  merge=0.0049s  heap=0.0068s  quick=0.0041s  builtin=0.0002s
n=   4000: insertion=0.0782s  merge=0.0105s  heap=0.0147s  quick=0.0087s  builtin=0.0004s
...

Graph saved to sorting_runtimes.png
```

## Input Sizes

Because Python is interpreted, it runs significantly slower than compiled
languages. The input sizes have been calibrated accordingly:

| Algorithm | Sizes Tested |
|---|---|
| Merge, Heap, Quick, Built-in | 1,000 → 2,000 → 4,000 → 8,000 → 16,000 → 32,000 → 64,000 → 128,000 → 256,000 → 512,000 |
| Insertion Sort | 1,000 → 2,000 → 4,000 → 8,000 → 16,000 → 32,000 |

Insertion sort is excluded from the larger sizes because its O(n²) growth
makes it prohibitively slow beyond ~32,000 elements.

## Implementation Guide

Open `empirical_analysis.py` and complete the four `TODO` sections:

### 1. `insertion_sort(lst)`
Sort the list in-place using the insertion sort algorithm:
- Iterate from index 1 to the end of the list
- For each element, save it as a `key` and shift larger elements to the right
- Insert the `key` into its correct position

### 2. `merge_sort(lst)`
Return a new sorted list using the merge sort algorithm:
- **Base case:** a list of length 0 or 1 is already sorted
- **Recursive step:** split the list in half, recursively sort each half,
  then merge the two sorted halves together

### 3. `heap_sort(lst)`
Sort the list in-place using Python's `heapq` module:
- Use `heapq.heapify()` to convert the list into a min-heap
- Use `heapq.heappop()` to extract elements in sorted order
- Copy the sorted elements back into the original list

### 4. `quick_sort(lst)`
Sort the list in-place using the quick sort algorithm:
- **Base case:** a list of length 0 or 1 is already sorted
- **Partition:** choose a pivot, separate elements into those less than
  and greater than the pivot
- **Recurse** on the two partitions

> **Important:** Do not modify the `benchmark()`, `run_benchmarks()`,
> or `plot_results()` functions. These handle timing, averaging, and
> graphing for you.

## What to Look For

As you review your results, think about these patterns from Chapter 2.2:

- **Doubling behavior:** When `n` doubles, does the time roughly double
  (linear), quadruple (quadratic), or something in between (~2.2× for
  n log n)?
- **Insertion sort vs. the rest:** At what input size does insertion sort
  become dramatically slower?
- **Quick sort vs. merge sort vs. heap sort:** These are all O(n log n) —
  do they perform identically, or are there constant-factor differences?
- **Built-in `sorted()`:** How does Python's Timsort compare to your
  implementations? Why might it be faster even though it shares the same
  Big-O class?

## Analysis Questions

**After running your benchmarks, replace the blanks below with your answers.**

**1. How do the sorting algorithms rank (fastest to slowest)?**

```
1. (fastest) _______________
2. _______________
3. _______________
4. _______________
5. (slowest) _______________
```

**2. Do your empirical results correspond with the Big-O of each sorting
algorithm? Explain why or why not.**

```
Your answer here:


```

**3. When you doubled `n`, by approximately what factor did the runtime
increase for insertion sort? For merge sort? How do these factors relate
to their Big-O classifications?**

```
Your answer here:


```
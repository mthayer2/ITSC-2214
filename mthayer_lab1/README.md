# Lab 1: Empirical Analysis of Sorting Algorithms

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

## Files in This Repository

| File | Description |
|---|---|
| `sorts.py` | Sorting algorithm implementations. **You must implement `insertion_sort`** — the rest are provided. |
| `lab1.py` | **You create this file.** Your benchmarking program. |
| `lab1work.xlsx` | Spreadsheet for logging runtimes, auto-averaging, and graphing. |
| `requirements.txt` | Python dependencies. |

## Getting Started

### Prerequisites

- Python 3.12 (required)

### Setup

```bash
python3 -m venv venv
source venv/bin/activate
```

## What You Will Do

### Step 1: Implement Insertion Sort

Open `sorts.py` and complete the `insertion_sort` function. It is the only
`TODO` in the file. Read the docstring for the algorithm outline.

The other sorting algorithms (merge sort, heap sort, quick sort) are
provided for you. You are encouraged to read through them — the code uses
clear variable names and comments explaining what each step does and how
many times each loop iterates. You will study these algorithms in depth
later in the course.

### Step 2: Create `lab1.py`

Create a new file called `lab1.py`. This is your benchmarking program.
It should do the following:

1. **Import what you need:**
   - `time` (for measuring execution time)
   - `random` (for generating random data)
   - The sorting functions from `sorts.py`
   - Note: for Python's built-in sort, you can simply call `list.sort()`
     directly — no import from `sorts.py` needed.

2. **Write a function to generate test data:**
   - Create a function that takes a `size` parameter and returns a list
     of that many random integers.
   - Use `random.randint()` to generate each value.
   - **Important:** You must generate a fresh list (or make a copy) before
     each sort, because sorting modifies the list. Sorting an
     already-sorted list gives misleading times.

3. **Write a function to benchmark a single sort:**
   - Record the start time using `time.perf_counter()`.
   - Run the sort.
   - Record the end time.
   - Return the elapsed time.
   - Remember that `merge_sort` returns a new list while the others
     sort in-place.

4. **Run benchmarks across multiple input sizes:**
   - Use the input sizes from the table below.
   - For each size, run **3 trials** per algorithm and compute the
     **average** time.
   - Print the results to the terminal in a readable format.

### Step 3: Log Results in the Spreadsheet

Open `lab1work.xlsx` and record your runtimes:

- **[BLUE cells]** Log the execution time of each sorting algorithm for
  Trial 1, Trial 2, and Trial 3.
- **[PINK cells]** The average and graph update automatically — do not
  edit these.
- **[BLUE cells]** Answer the two questions in the spreadsheet:
  - How do the sorting algorithms rank (fastest to slowest)?
  - Do the graphs correspond with the Big-O of each sorting algorithm?

> *Only update the blue portions of the spreadsheet. All pink portions
> will be automatically updated when you fill in the info for
> Trial 1, 2, and 3.*

### Input Sizes

Because Python is interpreted, it runs significantly slower than compiled
languages. The input sizes have been calibrated accordingly:

| Algorithm | Sizes Tested |
|---|---|
| Merge, Heap, Quick, Built-in | 1,000 → 2,000 → 4,000 → 8,000 → 16,000 → 32,000 → 64,000 → 128,000 → 256,000 → 512,000 |
| Insertion Sort | 1,000 → 2,000 → 4,000 → 8,000 → 16,000 → 32,000 |

Insertion sort is excluded from the larger sizes because its O(n²) growth
makes it prohibitively slow beyond ~32,000 elements.

### Sample Output

```
Benchmarking sorting algorithms (3 trials each)...

n=   1000: insertion=0.0052s  merge=0.0023s  heap=0.0031s  quick=0.0019s  builtin=0.0001s
n=   2000: insertion=0.0198s  merge=0.0049s  heap=0.0068s  quick=0.0041s  builtin=0.0002s
n=   4000: insertion=0.0782s  merge=0.0105s  heap=0.0147s  quick=0.0087s  builtin=0.0004s
...
```

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
# Programming Fundamentals: Algorithms

Course notes from Programming Fundamentals: Algorithms by Joe Marini.

## Overview

Algorithm Characteristics

- Complexity (Space, Time)
- Inputs and output
- Classification (serial, parallel, exact, approximate, deterministic, non-deterministic)

Common Algorithms

- Search (find specific data in a structure)
- Sorting (take a dataset and place in an order)
- Computational (is given number primer)
- Collection (count, specific items, filtering data)

Algorithm Performance

- Measure how an algorithm responds to dataset size
- Big-O notation
  - Classifies performance as the input size grows
  - "O" indicates the order of operation: time scale to perform an operation

### Big-O Terms

| Notation   | Description   | Example                                                                            |
| ---------- | ------------- | ---------------------------------------------------------------------------------- |
| 0(1)       | Constant time | Looking up a single element in an array                                            |
| 0(log n)   | Logarithmic   | Finding an item in a sorted array with a binary search                             |
| 0(n)       | Linear time   | Searching an unsorted array for a specific value                                   |
| 0(n log n) | Log-linear    | Complex sorting algorithms like heap sort and merge sort                           |
| 0(n²)      | Quadratic     | Simple sorting algorithms, such as bubble sort, selection sort, and insertion sort |


## Data Structures

Used to organize data so it can be processed.

### Common data structures

- Arrays
- Linked lists
- Stacks and queues
- Trees
- Hash tables

### Arrays

Collection of elements indetified by index or key.

Common Array operations include:

- Calculate item index: O(1)
- Insert or delete item at beginning: O(n)
- Insert or delete item in middle: O(n)
- Insert or delete item at end: O(1)

### Linked lists

- Collection of data elements called nodes.
- Contain reference to the next node in the list
- Hold whatever data the application needs
- Elements can be easily inserted and removed
- Underlyng memory doesn't need tobe reorganized
- Can't do constant time random item access
- Item lookup is linear in time complexity (O(n))

Common Linked list operations include:
- Insert node
- Remove node

### Stack

- Collection that supports push and pop operations
- The last item pushed is the first one popped

Common usage:
- Expression processing
- Backtracking: browser back stack, for example

### Queues

- Collection that supports adding and removing
- First item added is the first item out

Common usege:
- Order processing
- Messaging

### Hash tables

- Key-to-value mappings are unique
- Hash tables are typically very fast
- For small datasets, arrays are usually more efficient
- Hash tables don't order entries in a predictable way


## Recursion

- Recursion is when a function calls itself.
- Recursive functions need to have a breaking condition
- This prevents infinite loops and eventual crashes
- Each time the function is called, the old arguments are saved
- This is called the "call stack"

```python
def countdown(x):
  if (x == 0):
    print("done")
    return
  else:
    print(x,"...")
    countdown(x-1)

countdown(5)
```

## Sorting

- Most modern language have sorting built in
- The bubble sort
- The merge sort
- The quicksort

### Bubble sort

- Very simple to understand and implement
- Performance: O(n²)
  - For lopps inside of for loops are usually n²
- Other sorting algorithms are generally much better
- Not considered to be a practical solution

### Merge sort

- Divide and conquer algorithm
- Breaks a dataset into individual pieces and merges them
- Uses recursion to operate on datasets
- Performs well on large sets of data
- In general has a perfomrnace of O(n log n) time complexity

### Quick sort

- Divide and conquer algorithm
- Also uses recursion to perform sorting
- Generally performs better than merge sort O(n log n)


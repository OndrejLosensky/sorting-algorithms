# Quick sort
Quicksort is a divide-and-conquer sorting algorithm that works by selecting a 'pivot' element from the array and partitioning the other elements into two sub-arrays according to whether they are less than or greater than the pivot. It then recursively sorts the sub-arrays.

### Efficiency
Quicksort is efficient for sorting large arrays or lists due to its average time complexity of **O(nlogn)**. It is particularly efficient when the pivot selection and partitioning are well-optimized. Quicksort is also an in-place sorting algorithm, meaning it doesn't require additional memory beyond the input array, making it space-efficient. However, its worst-case time complexity is **O(n^2)** when the pivot selection is poor, but this is rare with proper implementations.

### Time taken in test:
List of 1000 numbers placed randomly: **0.0051s**  
List of 10 000 numbers placed randomly: **0.0645s**  
List of 100 000 numbers placed randomly: **0.6121s**





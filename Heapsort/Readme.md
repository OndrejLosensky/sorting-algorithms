# Heapsort
Heap sort is a sorting algorithm that uses a binary heap data structure. It works by first building a max-heap or min-heap from the input array. Then, it repeatedly extracts the maximum (for max-heap) or minimum (for min-heap) element from the heap and places it at the end of the array. This process is repeated until the heap is empty, resulting in a sorted array.

### Efficiency
Heap sort is efficient for sorting large lists or arrays because it has a time complexity of **O(n log n)** for both average and worst-case scenarios. Additionally, it doesn't require additional memory space beyond the input array, making it space-efficient compared to some other sorting algorithms.

### Time taken (Simple.py):
List of 1000 numbers placed randomly: **0.0129s**  
List of 10 000 numbers placed randomly: **0.1809s**  
List of 100 000 numbers placed randomly: **2.2778s**

### Time taken with .txt file (Input.py):
Text file with 10 000 10-digit long ID's: **0.3091s**

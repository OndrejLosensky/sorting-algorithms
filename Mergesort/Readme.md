# Merge sort
Merge sort is a divide-and-conquer sorting algorithm that divides the input array into smaller subarrays, sorts each subarray recursively, and then merges them back together to produce a sorted array. It repeatedly divides the array in half until each subarray contains only one element, then merges them back together in sorted order.

### Efficiency
Merge sort is efficient for sorting large arrays or lists because it has a stable time complexity of **O(nlog n)** for both average and worst-case scenarios. It is also efficient for sorting linked lists due to its sequential access pattern. Additionally, merge sort is a stable sorting algorithm, meaning it preserves the relative order of equal elements in the input array, making it suitable for applications where maintaining the original order is important.

### Time taken in test:
List of 1000 numbers placed randomly: **0.008s**  
List of 10 000 numbers placed randomly: **0.0811s**  
List of 100 000 numbers placed randomly: **0.9293s**  

### Demonstration video:
https://github.com/OndrejLosensky/sorting_algorithms/assets/127244546/2ff78593-33a5-4176-855b-280ca5d9cc04



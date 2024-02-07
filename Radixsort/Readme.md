# Radix sort
Radix sort is a non-comparative sorting algorithm that works by distributing elements into buckets based on their individual digits or characters. It iterates through the digits or characters from the least significant to the most significant, sorting elements into buckets based on each digit or character position. After sorting, the elements are collected from the buckets and placed back into the original array. Radix sort can be applied to both integers and strings, making it versatile for different types of data.

### Efficiency
Radix sort is efficient for sorting integers or strings with fixed-length representations, where the number of digits or characters is relatively small compared to the number of elements to be sorted. It has a time complexity of **O(nk)**, where **n** is the number of elements to be sorted and 
*k* is the number of digits or characters in the input data. Radix sort is particularly useful when the range of values in the input data is limited, as it doesn't rely on comparisons between elements.

### Time taken (Simple.py):
List of 1000 numbers placed randomly: **0.0062s**  
List of 10 000 numbers placed randomly: **0.0788s**  
List of 100 000 numbers placed randomly: **0.7209s**  




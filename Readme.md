# Sorting algorithms

Repository with sorting algorithms showcase. Each of them has **simple version** & **visual with video**. Each sorting algorithm also has log.txt file that shows time taken for it to sort the list and etc. 
*The results can be different each time you run the algorithm! Those are just from my device.*
### Sorting time (Simple.py): number of elements in the list
Algorithm |100| 1000| 10 000 | 100 000 | 1 000 000 | 10 000 000 | 25 000 000 
--- | --- | --- | --- |--- |--- |--- |---
Bubblesort | 0.000713s | 0.0629s | 6.4593s | - | - | - | - |
Insertsort | 0.000507s | 0.0305s | 3.3144s | - | - | - | - | 
Selectsort | 0.000964s | 0.0459s | 4.1169s | - | - | - | - |
Mergesort  | 0.000768s | 0.008s  | 0.0811s | 0.9293s | 11.29s | 141.37s | - |
Quicksort  | 0.00062s  | 0.0051s | 0.0645s | 0.6121s | 7.89s  | 83.56s  | 423.68s |
Heapsort   | 0.001116s | 0.0129s | 0.1809s | 2.2778s | 31.28s | 407.98s | - |
Radixsort  | 0.001137s | 0.0062s | 0.0788s | 1.2946s | 13.05s | 166.52s | - | 

### Sorting time with input from txt file (Input.py): number of ID's inside the file
Algorithm |100| 1000| 10 000 | 100 000 | 1 000 000 
--- | --- | --- | --- |--- |--- 
Bubblesort | 0.001s | 0.108s | 11.2463s | - | - |
Insertsort | 0.002s | 0.0561s | 5.6124s | - | - |
Selectsort | 0.0011s | 0.0948s | 7.3281s | - | - | 
Mergesort | 0.0027s | 0.0101s | 0.1113s | 1.3748s | 14.8943s | 
Quicksort | 0.0009s | 0.0076s | 0.0892s | 1.0233s | 12.6169s | 
Heapsort |  0.0022s | 0.0208s | 0.2774s | 3.9609s  | 44.7057s | 

*input.txt with ID's is generated randomly just for the algorithm to have something to work with. All algorithms use the same file*

## How to install
*create new virtual envirorment for packages*
```
python3 -m venv myEnv
```

*activate it by typing this into terminal:*
```
source venv/bin/activate   
```

*install those modules for it to work:*
```
pip install matplotlib ipython
```
###  All available algorithms:
- [Bubblesort](https://github.com/OndrejLosensky/sorting_algorithms/blob/main/Bubblesort/Readme.md)
- [Insersort](https://github.com/OndrejLosensky/sorting_algorithms/blob/main/Insertsort/Readme.md)
- [Selectsort](https://github.com/OndrejLosensky/sorting_algorithms/blob/main/Selectsort/Readme.md)
- [Mergesort](https://github.com/OndrejLosensky/sorting_algorithms/blob/main/Mergesort/Readme.md)
- [Quicksort](https://github.com/OndrejLosensky/sorting_algorithms/blob/main/Quicksort/Readme.md)
- [Heapsort](https://github.com/OndrejLosensky/sorting_algorithms/blob/main/Heapsort/Readme.md)
- [Radixsort](https://github.com/OndrejLosensky/sorting_algorithms/blob/main/Radixsort/Readme.md)


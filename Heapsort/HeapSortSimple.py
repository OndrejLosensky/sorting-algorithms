import random
import time

def heap_sort(arr):
    n = len(arr)
    
    # Build a max heap
    for i in range(n // 2 - 1, -1, -1):
        heapify(arr, n, i)

    # Extract elements one by one
    for i in range(n - 1, 0, -1):
        arr[0], arr[i] = arr[i], arr[0]  # Swap root (max) with the last element
        heapify(arr, i, 0)  # Heapify the reduced heap

def heapify(arr, n, i):
    largest = i
    left = 2 * i + 1
    right = 2 * i + 2

    # Check if left child exists and is greater than the root
    if left < n and arr[left] > arr[largest]:
        largest = left

    # Check if right child exists and is greater than the root
    if right < n and arr[right] > arr[largest]:
        largest = right

    # Change root if needed
    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]
        heapify(arr, n, largest)

def log_to_file(log_message, log_file):
    log_entry = f"{log_message}"
    separator = '-' * len(log_entry)

    with open(log_file, 'a') as f:
        f.write(separator + "\n")
        f.write(log_entry + "\n")
        f.write(separator + "\n")

    print(f'Uložil jsem data do:  {log_file} !!')

# Example usage:
start_time = time.time()
my_list = list(range(1, 1001))
random.shuffle(my_list)

heap_sort(my_list)
end_time = round(time.time() - start_time, 4)
print("Seřazené pole:", my_list)
print("Doba trvání:", end_time, "s")

log_file = "heapsort/log.txt"
log_message = f'Doba trvání {end_time}s | Bez vizualizace| Počet čísel v listu: {len(my_list)}'
log_to_file(log_message, log_file)

import random
import time

def quick_sort(arr, low, high):
    if low < high:
        pivot_index = partition(arr, low, high)
        quick_sort(arr, low, pivot_index)
        quick_sort(arr, pivot_index + 1, high)

def partition(arr, low, high):
    pivot = arr[(low + high) // 2]
    i = low - 1
    j = high + 1
    while True:
        i += 1
        while arr[i] < pivot:
            i += 1
        j -= 1
        while arr[j] > pivot:
            j -= 1
        if i >= j:
            return j
        arr[i], arr[j] = arr[j], arr[i]

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

quick_sort(my_list, 0, len(my_list) - 1)
end_time = round(time.time() - start_time, 4)
print("Seřazené pole:", my_list)
print("Doba trvání:", end_time, "s")

log_file = "quicksort/log.txt"
log_message = f'Doba trvání: {end_time}s | Bez vizualizace | Počet čísel v listu: {len(my_list)}'
log_to_file(log_message, log_file)

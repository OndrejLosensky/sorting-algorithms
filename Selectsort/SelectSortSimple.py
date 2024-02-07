import random
import time

def select_sort(arr):
    n = len(arr)

    for i in range(n):
        min_index = i
        for j in range(i + 1, n):
            # Find the index of the minimum element in the unsorted part of the array
            if arr[j] < arr[min_index]:
                min_index = j

        # Swap the found minimum element with the first element
        arr[i], arr[min_index] = arr[min_index], arr[i]
        yield arr  # This line yields the current state of the array for visualization

def log_to_file(log_message, log_file):
    log_entry = f"{log_message}"
    separator = '-' * len(log_entry)

    with open(log_file, 'a') as f:
        f.write(separator + "\n")
        f.write(log_entry + "\n")
        f.write(separator + "\n")

    print(f'Uložil jsem data do:  {log_file} !!')

start_time = time.time()
my_list = list(range(1, 1001))
random.shuffle(my_list)

# Consume the generator values to execute the sorting algorithm
for _ in select_sort(my_list):
    pass

end_time = round(time.time() - start_time, 4)

print("Seřazené pole:", my_list)
print("Doba trvání: ", end_time, "s")

log_file = "selectsort/log.txt"
log_message = f'Doba trvání: {end_time}s | Bez vizualizace | Počet čísel v listu: {len(my_list)}'
log_to_file(log_message, log_file)

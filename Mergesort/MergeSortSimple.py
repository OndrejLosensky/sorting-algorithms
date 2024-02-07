import random
import time 

def log_to_file(log_message, log_file):

    log_entry = f"{log_message}"
    separator = '-' * len(log_entry)

    with open(log_file, 'a') as f:
        f.write(separator + "\n")
        f.write(log_entry + "\n")
        f.write(separator + "\n")

    print("Uložil data do log.txt !!")

def merge_sort(arr):
    if len(arr) > 1:
        mid = len(arr) // 2
        left_half = arr[:mid]
        right_half = arr[mid:]

        merge_sort(left_half)
        merge_sort(right_half)

        i = j = k = 0

        while i < len(left_half) and j < len(right_half):
            if left_half[i] < right_half[j]:
                arr[k] = left_half[i]
                i += 1
            else:
                arr[k] = right_half[j]
                j += 1
            k += 1

        while i < len(left_half):
            arr[k] = left_half[i]
            i += 1
            k += 1

        while j < len(right_half):
            arr[k] = right_half[j]
            j += 1
            k += 1

# Example usage:
start_time = time.time()
my_list = list(range(1, 1001))
random.shuffle(my_list)

merge_sort(my_list)
end_time = round(time.time() - start_time, 4)


print("Seřazené pole:", my_list)
print("Doba trvání: ", end_time, "s" )

log_file = "mergesort/log.txt"
log_message = f'Doba trvání: {end_time}s | Bez vizualizace | Počet čísel v listu: {len(my_list)}'
log_to_file(log_message, log_file)

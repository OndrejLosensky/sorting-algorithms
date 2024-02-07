import random
import time

def bubble_sort(arr):
    n = len(arr)

    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]

def log_to_file(log_message, log_file):

    log_entry = f"{log_message}"
    separator = '-' * len(log_entry)

    with open(log_file, 'a') as f:
        f.write(separator + "\n")
        f.write(log_entry + "\n")
        f.write(separator + "\n")

    print(f'I have saved the data into {log_file}')


start_time = time.time()
my_list = list(range(0, 10000))
random.shuffle(my_list)

bubble_sort(my_list)
end_time = round(time.time() - start_time, 4)
print("Sorted array:", my_list)
print("Time it took: ", end_time, "s" )

log_file = "bubblesort/log.txt"
log_message = f'Time it took: {end_time}s | Without visualization | number of elements in the list: {len(my_list)}'
log_to_file(log_message, log_file)
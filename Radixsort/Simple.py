import random
import time

def counting_sort(arr, exp):
    n = len(arr)
    output = [0] * n
    count = [0] * 10

    # Store count of occurrences in count[]
    for i in range(n):
        index = arr[i] // exp
        count[index % 10] += 1

    # Change count[i] so that count[i] contains the actual position of this digit in output[]
    for i in range(1, 10):
        count[i] += count[i - 1]

    # Build the output array
    i = n - 1
    while i >= 0:
        index = arr[i] // exp
        output[count[index % 10] - 1] = arr[i]
        count[index % 10] -= 1
        i -= 1

    # Copy the output array to arr[], so that arr[] now contains sorted numbers according to the current digit
    for i in range(n):
        arr[i] = output[i]

def radix_sort(arr):
    # Find the maximum number to know the number of digits
    max_num = max(arr)

    # Do counting sort for every digit. Note that instead of passing digit number, exp is passed. exp is 10^i where i is the current digit number
    exp = 1
    while max_num // exp > 0:
        counting_sort(arr, exp)
        exp *= 10

def log_to_file(log_message, log_file):
    log_entry = f"{log_message}"
    separator = '-' * len(log_entry)

    with open(log_file, 'a') as f:
        f.write(separator + "\n")
        f.write(log_entry + "\n")
        f.write(separator + "\n")

    print(f'I have saved the data into {log_file}')


# Example usage:
start_time = time.time()
my_list = [random.randint(0, 20000) for _ in range(10000)]
random.shuffle(my_list)

radix_sort(my_list)
end_time = round(time.time() - start_time, 4)
print("Sorted array:", my_list)
print("Time it took: ", end_time, "s" )

log_file = "bubblesort/log.txt"
log_message = f'Time it took: {end_time}s | Without visualization | number of elements in the list: {len(my_list)}'
log_to_file(log_message, log_file)

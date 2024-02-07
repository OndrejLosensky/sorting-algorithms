import time

def log_to_file(log_message, log_file):
    with open(log_file, 'a') as f:
        f.write(log_message + "\n")

def insertion_sort(arr):
    n = len(arr)

    for i in range(1, n):
        key = arr[i]
        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key

def sort_ids_with_insertion_sort(input_file, output_file):
    start_time = time.time()
    # Read IDs from input file
    with open(input_file, 'r') as f:
        ids = [line.strip() for line in f]

    # Sort IDs using insertion sort
    insertion_sort(ids)
    end_time = round(time.time() - start_time, 4)
    print(f'Time it took: {end_time}s')

    # Write sorted IDs to output file
    with open(output_file, 'w') as f:
        for id in ids:
            f.write(id + '\n')

    # Log sorting information
    log_file = "input_log.txt"
    log_message = f'Time it took: {end_time}s | Input: {input_file} | Number of IDs: {len(ids)}'
    log_to_file(log_message, log_file)

input_file = "insertsort/input.txt" 
output_file = "insertsort/sorted_input.txt" 
sort_ids_with_insertion_sort(input_file, output_file)

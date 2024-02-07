import time

def log_to_file(log_message, log_file):
    with open(log_file, 'a') as f:
        f.write(log_message + "\n")

def quick_sort(arr):
    if len(arr) <= 1:
        return arr

    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]

    return quick_sort(left) + middle + quick_sort(right)

def sort_ids_with_quick_sort(input_file, output_file):
    start_time = time.time()
    # Read IDs from input file
    with open(input_file, 'r') as f:
        ids = [line.strip() for line in f]

    # Sort IDs using quicksort
    sorted_ids = quick_sort(ids)
    end_time = round(time.time() - start_time, 4)
    print(f'Time it took: {end_time}s')

    # Write sorted IDs to output file
    with open(output_file, 'w') as f:
        for id in sorted_ids:
            f.write(id + '\n')

    # Log sorting information
    log_file = "input_log.txt"
    log_message = f'Time it took: {end_time}s | Input: {input_file} | Number of IDs: {len(sorted_ids)}'
    log_to_file(log_message, log_file)

input_file = "quicksort/input.txt" 
output_file = "quicksort/sorted_input.txt" 
sort_ids_with_quick_sort(input_file, output_file)

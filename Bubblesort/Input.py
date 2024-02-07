import time

def bubble_sort(arr):
    n = len(arr)

    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]

def log_to_file(log_message, log_file):
    with open(log_file, 'a') as f:
        f.write(log_message + "\n")

def sort_ids(input_file, output_file):
    # Read IDs from input file
    with open(input_file, 'r') as f:
        ids = [line.strip() for line in f]

    # Sort IDs
    start_time = time.time()
    bubble_sort(ids)
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

# Usage:
input_file = "bubblesort/input.txt"
output_file = "bubblesort/sorted_input.txt"
sort_ids(input_file, output_file)
print("Done!")


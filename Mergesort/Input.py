import time

def log_to_file(log_message, log_file):
    with open(log_file, 'a') as f:
        f.write(log_message + "\n")

def merge_sort(arr):
    if len(arr) > 1:
        mid = len(arr) // 2
        left_half = arr[:mid]
        right_half = arr[mid:]

        merge_sort(left_half)
        merge_sort(right_half)

        i = j = k = 0

        # Merge the two halves
        while i < len(left_half) and j < len(right_half):
            if left_half[i] < right_half[j]:
                arr[k] = left_half[i]
                i += 1
            else:
                arr[k] = right_half[j]
                j += 1
            k += 1

        # Check for any remaining elements in left_half and right_half
        while i < len(left_half):
            arr[k] = left_half[i]
            i += 1
            k += 1

        while j < len(right_half):
            arr[k] = right_half[j]
            j += 1
            k += 1

def sort_ids_with_merge_sort(input_file, output_file):
    start_time = time.time()
    # Read IDs from input file
    with open(input_file, 'r') as f:
        ids = [line.strip() for line in f]

    # Sort IDs using merge sort
    merge_sort(ids)
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

input_file = "mergesort/input.txt" 
output_file = "mergesort/sorted_input.txt" 
sort_ids_with_merge_sort(input_file, output_file)

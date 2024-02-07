import time

def log_to_file(log_message, log_file):
    with open(log_file, 'a') as f:
        f.write(log_message + "\n")

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

def sort_ids_with_heap_sort(input_file, output_file):
    start_time = time.time()
    # Read IDs from input file
    with open(input_file, 'r') as f:
        ids = [line.strip() for line in f]

    # Sort IDs using heap sort
    heap_sort(ids)
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


input_file = "heapsort/input.txt" 
output_file = "heapsort/sorted_input.txt" 
sort_ids_with_heap_sort(input_file, output_file)


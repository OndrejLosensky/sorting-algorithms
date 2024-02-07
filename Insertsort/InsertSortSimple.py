import random
import time 

def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key

def log_to_file(log_message, log_file):

    log_entry = f"{log_message}"
    separator = '-' * len(log_entry)

    with open(log_file, 'a') as f:
        f.write(separator + "\n")
        f.write(log_entry + "\n")
        f.write(separator + "\n")

    print("Uložil jsem data do log.txt !!")


def main():
    start_time = time.time()
    my_list = list(range(1, 1001))
    random.shuffle(my_list)

    insertion_sort(my_list)
    end_time = round(time.time() - start_time, 4)

    print("Seřazené pole:", my_list)
    print("Doba trvání: ", end_time, "s" )

    log_file = "insertsort/log.txt"
    log_message = f'Doba trvání: {end_time}s | Bez vizualizace | Počet čísel v listu: {len(my_list)}'
    log_to_file(log_message, log_file)

if __name__ == "__main__":
    main()

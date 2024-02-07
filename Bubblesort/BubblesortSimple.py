import random
import time

def bubble_sort(arr):
    n = len(arr)

    for i in range(n):
        # Poslední i prvků jsou již na svých místech
        for j in range(0, n-i-1):
            # Procházíme pole od začátku do n-i-1
            # Pokud je prvek větší než následující prvek, prohodíme je
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]

def log_to_file(log_message, log_file):

    log_entry = f"{log_message}"
    separator = '-' * len(log_entry)

    with open(log_file, 'a') as f:
        f.write(separator + "\n")
        f.write(log_entry + "\n")
        f.write(separator + "\n")

    print("Uložil data do log.txt !!")


# Příklad použití:
start_time = time.time()
my_list = list(range(1, 10001))
random.shuffle(my_list)

bubble_sort(my_list)
end_time = round(time.time() - start_time, 4)
print("Seřazené pole:", my_list)
print("Doba trvání: ", end_time, "s" )

log_file = "bubblesort/log.txt"
log_message = f'Doba trvání: {end_time}s | Bez vizualizace | Počet čísel v listu: {len(my_list)}'
log_to_file(log_message, log_file)
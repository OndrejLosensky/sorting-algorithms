import matplotlib.pyplot as plt
import matplotlib.animation as animation
from IPython.display import display, HTML
import random
import time

def merge_sort_animation(arr):
    fig, ax = plt.subplots()
    bars = ax.bar(range(len(arr)), arr, color='green')

    def merge_sort(arr, left, right):
        if left < right:
            mid = (left + right) // 2

            merge_sort(arr, left, mid)
            merge_sort(arr, mid + 1, right)

            merge(arr, left, mid, right)

    def merge(arr, left, mid, right):
        left_half = arr[left:mid + 1]
        right_half = arr[mid + 1:right + 1]

        i = j = 0
        k = left

        while i < len(left_half) and j < len(right_half):
            if left_half[i] <= right_half[j]:
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

        for bar, height in zip(bars, arr):
            bar.set_height(height)

    def update(num):
        merge_sort(arr, 0, num)
        return bars

    ani = animation.FuncAnimation(fig, update, frames=len(arr) - 1, repeat=False, blit=True)

    # Save the animation as a video
    ani.save('mergesort/mergesort.mp4', writer='ffmpeg', fps=12)

    # Display the animation within the notebook
    display(HTML(ani.to_jshtml()))

def log_to_file(log_message, log_file):

    log_entry = f"{log_message}"
    separator = '-' * len(log_entry)

    with open(log_file, 'a') as f:
        f.write(separator + "\n")
        f.write(log_entry + "\n")
        f.write(separator + "\n")

    print(f'I have saved the data into {log_file}')



start_time = time.time()
my_list = list(range(1, 101))
random.shuffle(my_list)

merge_sort_animation(my_list)
end_time = round(time.time() - start_time, 2)
print("Sorted array:", my_list)
print("Time it took: ", end_time, "s" )

log_file = "bubblesort/log.txt"
log_message = f'Time it took: {end_time}s | Without visualization | number of elements in the list: {len(my_list)}'
log_to_file(log_message, log_file)
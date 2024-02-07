import matplotlib.pyplot as plt
import matplotlib.animation as animation
from IPython.display import display, HTML
import random
import time

def selection_sort_animation(arr):
    fig, ax = plt.subplots()
    bars = ax.bar(range(len(arr)), arr, color='gray')

    def selection_sort(arr):
        for i in range(len(arr)):
            min_index = i
            for j in range(i + 1, len(arr)):
                if arr[j] < arr[min_index]:
                    min_index = j

            arr[i], arr[min_index] = arr[min_index], arr[i]

            for bar, height in zip(bars, arr):
                bar.set_height(height)
                
    def update(num):
        selection_sort(arr[:num + 1])
        return bars

    ani = animation.FuncAnimation(fig, update, frames=len(arr) - 1, repeat=False, blit=True)

    # Save the animation as a video
    ani.save('selectsort/selectsort.mp4', writer='ffmpeg', fps=12)

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

# Usage:
my_list = list(range(1, 101))
random.shuffle(my_list)

selection_sort_animation(my_list)
end_time = round(time.time() - start_time, 2)
print("Sorted array:", my_list)
print("Time it took: ", end_time, "s" )

log_file = "bubblesort/log.txt"
log_message = f'Time it took: {end_time}s | Without visualization | number of elements in the list: {len(my_list)}'
log_to_file(log_message, log_file)

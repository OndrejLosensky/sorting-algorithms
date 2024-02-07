import matplotlib.pyplot as plt
import matplotlib.animation as animation
from IPython.display import display, HTML
import random
import time

def insertion_sort_animation(arr):
    fig, ax = plt.subplots()
    bars = ax.bar(range(len(arr)), arr, color='blue')

    def update(num):
        key = arr[num]
        j = num - 1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key

        for bar, height in zip(bars, arr):
            bar.set_height(height)

        return bars

    ani = animation.FuncAnimation(fig, update, frames=len(arr), repeat=False, blit=True)
    
    # Save the animation as a video
    ani.save('insertsort/insertsort.mp4', writer='ffmpeg', fps=12)
    
    # Display the animation within the notebook
    display(HTML(ani.to_jshtml()))

def log_to_file(log_message, log_file):

    log_entry = f"{log_message}"
    separator = '-' * len(log_entry)

    with open(log_file, 'a') as f:
        f.write(separator + "\n")
        f.write(log_entry + "\n")
        f.write(separator + "\n")

    print(f'I have saved data into {log_file}')


# Usage:    
start_time = time.time()
my_list = list(range(1, 101))
random.shuffle(my_list)

insertion_sort_animation(my_list)
end_time = round(time.time() - start_time, 2)

print("Sorted array:", my_list)
print("Time it took: ", end_time, "s" )

log_file = "insertsort/log.txt"
log_message = f'Time it took: {end_time}s | Without visualization | Number of elements in the list {len(my_list)}'
log_to_file(log_message, log_file)

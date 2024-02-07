import matplotlib.pyplot as plt
import matplotlib.animation as animation
from IPython.display import display, HTML
import random
import time

def quick_sort_animation(arr):
    fig, ax = plt.subplots()
    bars = ax.bar(range(len(arr)), arr, color='blue')

    def quick_sort(arr, low, high):
        if low < high:
            pivot_index = partition(arr, low, high)
            yield from quick_sort(arr, low, pivot_index)
            yield from quick_sort(arr, pivot_index + 1, high)

    def partition(arr, low, high):
        pivot = arr[(low + high) // 2]
        i = low - 1
        j = high + 1
        while True:
            i += 1
            while arr[i] < pivot:
                i += 1
            j -= 1
            while arr[j] > pivot:
                j -= 1
            if i >= j:
                return j
            arr[i], arr[j] = arr[j], arr[i]

    def update(num):
        if num is not None:
            for bar, height in zip(bars, num):
                bar.set_height(height)
        return bars

    # Generator to yield states of the array during sorting
    def generate_states():
        yield from quick_sort(arr, 0, len(arr) - 1)
        yield arr

    # Ensure the animation has a non-zero duration
    def update_frames():
        frames = generate_states()
        first_frame = next(frames)
        while True:
            yield first_frame

    ani = animation.FuncAnimation(fig, update, frames=update_frames, repeat=False, blit=True)
    ani.save('quicksort/quicksort.mp4', writer='ffmpeg', fps=12)
    display(HTML(ani.to_jshtml()))

start_time = time.time()
my_list = list(range(1, 101))
random.shuffle(my_list)

quick_sort_animation(my_list)
end_time = round(time.time() - start_time, 2)
print("Finished!")
print("Execution time:", end_time, "s")

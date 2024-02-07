import matplotlib.pyplot as plt
import matplotlib.animation as animation
from IPython.display import display, HTML
import random
import time

def bubble_sort_animation(arr):
    fig, ax = plt.subplots()
    bars = ax.bar(range(len(arr)), arr, color='red')


    def update(num):
        for i in range(len(bars) - 1 - num):
            if arr[i] > arr[i + 1]:
                arr[i], arr[i + 1] = arr[i + 1], arr[i]
                for bar, height in zip(bars, arr):
                    bar.set_height(height)
        return bars

    ani = animation.FuncAnimation(fig, update, frames=len(arr)-1, repeat=False, blit=True)
    
    # Save the animation as a video
    ani.save('bubblesort/bubblesort.mp4', writer='ffmpeg', fps=12)
    
    # Display the animation within the notebook
    display(HTML(ani.to_jshtml()))

start_time = time.time()
# Usage:
my_list = list(range(1, 101))
random.shuffle(my_list)

bubble_sort_animation(my_list)
end_time = round(time.time() - start_time, 2)
print("Hotovo!")
print("Doba trvání: ", end_time, "s")

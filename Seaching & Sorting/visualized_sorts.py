from heapq import merge
import matplotlib.pyplot as plt
import numpy as np
import time


class Swapper:
    def __init__(self,fig = None, ax = None, type = ""):
        self.type = type
        self.fig,self.ax = plt.subplots()
        self.processor_time = 0
        self.plotting_time = 0
        self.last_return_time = None

    def swap(self,arr,i,j):
        start = time.time()
        temp = arr[j]
        arr[j] = arr[i]
        arr[i] = temp
        self.processor_time += time.time() - start
        if self.last_return_time:
            self.processor_time += time.time() - self.last_return_time
        plot_start = time.time()
        self.ax.clear()
        self.fig.suptitle(f"{self.type}\nprocessor time: {self.processor_time:.10f}, plot time: {self.plotting_time:.3f}")
        self.ax.plot(arr,'k.')
        plt.show(block = False)
        plt.pause(.0000001)
        self.plotting_time += time.time() - plot_start
        self.last_return_time = time.time()
    
    def clear(self):
        pro_time = self.processor_time
        plt_time = self.plotting_time
        self.type = ""
        self.processor_time = 0
        self.plotting_time = 0
        self.last_return_time = None
        return pro_time, plt_time


def partition(arr, swapper, lower, upper):
    median = lower + int((upper - lower)/2)
    if(arr[upper] < arr[median]):
        swapper.swap(arr,upper,median)
    if arr[median] < arr[lower]:
        swapper.swap(arr,median,lower)
    if arr[upper] < arr[median]:
        swapper.swap(arr,upper,median)

    value = arr[median]
    inc = lower
    dec = upper
    done = False
    while not done:
        while arr[inc] < value:
            inc += 1
        while arr[dec] > value:
            dec -= 1
        
        if inc >= dec:
            done = True
        else:
            swapper.swap(arr,inc,dec)
            inc += 1
            dec -= 1
    
    return dec

def quicksort(arr, swapper, lower = 0, upper = None):
    if upper == None:
        upper = len(arr) - 1
    if lower >= upper:
        return
    

    part = partition(arr, swapper,lower,upper)
    quicksort(arr, swapper,lower,part)
    quicksort(arr, swapper,part+1,upper)

def insertion(arr, swapper):
    for i in range(len(arr)):
        index = i
        while index>0 and arr[index]<arr[index-1]:
            swapper.swap(arr,index,index-1)
            index -= 1

def selection(arr, swapper):
    for i in range(len(arr)):
        lowest = i
        for j in range(i+1,len(arr)):
            if(arr[j] < arr[lowest]):
                lowest = j
        swapper.swap(arr,i,lowest)

def mergesort(arr, swapper, lower = 0, upper = None):
    if upper == None:
        upper = len(arr) - 1
    if lower >= upper:
        return

    midpoint = int((lower + upper)/2)

    mergesort(arr, swapper, lower, midpoint)
    mergesort(arr, swapper, midpoint + 1, upper)

    merge_point = midpoint + 1
    merged = False
    while merge_point <= upper:
        swap_index = merge_point - 1
        while swap_index >= lower and arr[swap_index] > arr[swap_index + 1]:
            swapper.swap(arr,swap_index,swap_index + 1)
            swap_index -= 1
        merge_point += 1

def bubblesort(arr, swapper):
    done = False
    while not done:
        done = True
        for i in range(len(arr)-1):
            if(arr[i] > arr[i+1]):
                swapper.swap(arr,i,i+1)
                done = False

def cocktail(arr, swapper):
    done = False
    while not done:
        done = True
        for i in range(len(arr) - 1):
            if(arr[i] > arr[i+1]):
                swapper.swap(arr,i,i+1)
                done = False
            
        for i in range(len(arr) - 2, 0, -1):
            if arr[i] > arr[i+1]:
                swapper.swap(arr,i,i+1)
                done = False

if __name__ == "__main__":
    swapper = Swapper()

    # cocktail sort
    swapper.type = "cocktail"
    size = 32
    arr = [i for i in range(size)]
    np.random.shuffle(arr)
    cocktail(arr, swapper)
    pro, plot = swapper.clear()
    print(f"cocktail of {size} elements took {pro:.5} sec processor time and {plot:.3} sec plotting time")

    # bubblesort
    swapper.type = "bubble"
    size = 32
    arr = [i for i in range(size)]
    np.random.shuffle(arr)
    bubblesort(arr, swapper)
    pro, plot = swapper.clear()
    print(f"bubble of {size} elements took {pro:.5f} sec processor time and {plot:.3} sec plotting time")

    # insertion sort
    swapper.type = "insertion"
    size = 32
    arr = [i for i in range(size)]
    np.random.shuffle(arr)
    insertion(arr, swapper)
    pro, plot = swapper.clear()
    print(f"insertion of {size} elements took {pro:.5f} sec processor time and {plot:.3f} sec plotting time")

    # selection sort
    swapper.type = "selection"
    size = 256
    arr = [i for i in range(size)]
    np.random.shuffle(arr)
    selection(arr, swapper)
    pro, plot = swapper.clear()
    print(f"selection of {size} elements took {pro:.5} sec processor time and {plot:.3} sec plotting time")

    # merge sort
    swapper.type = "mergesort"
    size = 64
    arr = [i for i in range(size)]
    np.random.shuffle(arr)
    mergesort(arr, swapper)
    pro, plot = swapper.clear()
    print(f"mergesort of {size} elements took {pro:.5} sec processor time and {plot:.3} sec plotting time")

    # quicksort
    swapper.type = "quicksort"
    size = 256
    arr = [i for i in range(size)]
    np.random.shuffle(arr)
    quicksort(arr, swapper)
    pro, plot = swapper.clear()
    print(f"quicksort of {size} elements took {pro:.5} sec processor time and {plot:.3} sec plotting time")
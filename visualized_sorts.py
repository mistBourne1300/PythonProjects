import matplotlib.pyplot as plt
import numpy as np

fig,ax = plt.subplots()

def swap(arr,i,j):
    ax.clear()
    temp = arr[j]
    arr[j] = arr[i]
    arr[i] = temp
    ax.plot(arr,'k.')
    plt.show(block = False)
    plt.pause(.001/len(arr))

def partition(arr, lower, upper):
    median = lower + int((upper - lower)/2)
    if(arr[upper] < arr[median]):
        swap(arr,upper,median)
    if arr[median] < arr[lower]:
        swap(arr,median,lower)
    if arr[upper] < arr[median]:
        swap(arr,upper,median)

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
            swap(arr,inc,dec)
            inc += 1
            dec -= 1
    
    return dec

def quicksort(arr, lower = 0, upper = None):
    if upper == None:
        upper = len(arr) - 1
    if lower >= upper:
        return
    

    part = partition(arr,lower,upper)
    quicksort(arr,lower,part)
    quicksort(arr,part+1,upper)

def insertion(arr):
    for i in range(len(arr)):
        index = i
        while index>0 and arr[index]<arr[index-1]:
            swap(arr,index,index-1)
            index -= 1

def selection(arr):
    for i in range(len(arr)):
        lowest = i
        for j in range(i+1,len(arr)):
            if(arr[j] < arr[lowest]):
                lowest = j
        swap(arr,i,lowest)

def mergesort(arr, lower, upper):
    if lower >= upper:
        return

    midpoint = int((lower + upper)/2)

    mergesort(arr, lower, midpoint)
    mergesort(arr, midpoint + 1, upper)

def bubblesort(arr):
    done = False
    while not done:
        done = True
        for i in range(len(arr)-1):
            if(arr[i] > arr[i+1]):
                swap(arr,i,i+1)
                done = False

def cocktail(arr):
    done = False
    while not done:
        done = True
        for i in range(len(arr) - 1):
            if(arr[i] > arr[i+1]):
                swap(arr,i,i+1)
                done = False
            
        for i in range(len(arr) - 2, 0, -1):
            if arr[i] > arr[i+1]:
                swap(arr,i,i+1)
                done = False

if __name__ == "__main__":
    size = 64
    
    arr = [i for i in range(size)]
    np.random.shuffle(arr)
    fig.suptitle("Bond, James Bond")
    cocktail(arr)

    # size = 32
    arr = [i for i in range(size)]
    np.random.shuffle(arr)
    fig.suptitle("bubbles")
    bubblesort(arr)

    # size = 32
    arr = [i for i in range(size)]
    np.random.shuffle(arr)
    fig.suptitle("insertion")
    insertion(arr)

    # size = 32
    arr = [i for i in range(size)]
    np.random.shuffle(arr)
    fig.suptitle("selection")
    selection(arr)

    # size = 32
    arr = [i for i in range(size)]
    np.random.shuffle(arr)
    fig.suptitle("quicksort")
    quicksort(arr)
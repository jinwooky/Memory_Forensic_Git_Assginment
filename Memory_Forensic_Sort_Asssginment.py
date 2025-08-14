import time
import random

def read_data(filename):
    data = []
    with open(filename, "r", encoding="utf-8") as f:
        for line in f:
            numbers = list(map(int, line.strip().split(",")))
            data.append(numbers)
    return data

def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[random.randrange(len(arr))]
    left = [x for x in arr if x < pivot]
    mid = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    return quick_sort(left) + mid + quick_sort(right)

def quick_sort_with_time(arr):
    start_time = time.perf_counter()
    sorted_arr = quick_sort(arr[:])
    end_time = time.perf_counter()
    elapsed_time = end_time - start_time
    return sorted_arr, elapsed_time

def main():

    
if __name__ == "__main__":
    main()

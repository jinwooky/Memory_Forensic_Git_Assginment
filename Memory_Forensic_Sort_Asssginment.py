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
    sorted_arr = quick_sort(arr[:])  # 원본 보호
    end_time = time.perf_counter()
    elapsed_time = end_time - start_time
    return sorted_arr, elapsed_time

def main():
    filename = "data.txt"
    data = read_data(filename)

    for i, row in enumerate(data, start=1):
        print(f"{i}번 데이터 (정렬 전): {row}")
        sorted_row, elapsed = quick_sort_with_time(row)
        print(f"{i}번 데이터 (정렬 후): {sorted_row}")
        print(f"퀵 정렬 소요 시간: {elapsed:.6f}초")
        print("-" * 50)
    

if __name__ == "__main__":
    main()
import timeit
import random

def insertion_sort(arr):
    for idx in range(1, len(arr)):
        current_value = arr[idx]
        position = idx - 1
        while position >= 0 and arr[position] > current_value:
            arr[position + 1] = arr[position]
            position -= 1
        arr[position + 1] = current_value
    return arr

def merge_sort(array):
    if len(array) <= 1:
        return array

    middle = len(array) // 2
    left_part = array[:middle]
    right_part = array[middle:]

    return merge_sorted_lists(merge_sort(left_part), merge_sort(right_part))

def merge_sorted_lists(left, right):
    merged_list = []
    left_idx, right_idx = 0, 0

    while left_idx < len(left) and right_idx < len(right):
        if left[left_idx] < right[right_idx]:
            merged_list.append(left[left_idx])
            left_idx += 1
        else:
            merged_list.append(right[right_idx])
            right_idx += 1

    merged_list.extend(left[left_idx:])
    merged_list.extend(right[right_idx:])

    return merged_list

# Generate random test data
small_dataset = [random.randint(0, 1000) for _ in range(1000)]  # Smaller array
large_dataset = [random.randint(0, 10000) for _ in range(10000)]  # Larger array

# Measure execution time for the smaller array
time_insertion_small = timeit.timeit(lambda: insertion_sort(small_dataset[:]), number=10)
time_merge_small = timeit.timeit(lambda: merge_sort(small_dataset[:]), number=10)
time_timsort_small = timeit.timeit(lambda: sorted(small_dataset[:]), number=10)

# Measure execution time for the larger array
time_insertion_large = timeit.timeit(lambda: insertion_sort(large_dataset[:]), number=10)
time_merge_large = timeit.timeit(lambda: merge_sort(large_dataset[:]), number=10)
time_timsort_large = timeit.timeit(lambda: sorted(large_dataset[:]), number=10)

# Print the results
print(f"{'Algorithm':<20} | {'Small Array':<20} | {'Large Array':<20}")
print(f"{'-'*21}+{'-'*22}+{'-'*22}")
print(f"{'Insertion Sort':<20} | {time_insertion_small:<20.5f} | {time_insertion_large:<20.5f}")
print(f"{'Merge Sort':<20} | {time_merge_small:<20.5f} | {time_merge_large:<20.5f}")
print(f"{'Timsort':<20} | {time_timsort_small:<20.5f} | {time_timsort_large:<20.5f}")

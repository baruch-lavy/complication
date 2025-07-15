import random
def bubble_sort(arr):
    lenght = len(arr) - 1

    for i in range(lenght):
        swapped = False
        for j in range(lenght - i):
            if arr[j] > arr[j + 1]:
                swap(arr,j)
                swapped = True

        if swapped == False:
            return 'sorted', arr

def swap(arr,idx):
    arr[idx], arr[idx+1] = arr[idx+1], arr[idx]

nums = [i for i in range(100)]
random.shuffle(nums)
print(f'before {nums}')

res = bubble_sort(nums)
print(f'after {res}')
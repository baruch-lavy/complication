import random
start = 0
def find_min(arr,start_idx):
    min_idx = start_idx
    for i in range(len(arr[start_idx:])):
        num = arr[start_idx + i]
        if num < 0:
            continue
        elif num < arr[min_idx]:
            min_idx = start_idx + i
    return min_idx

def swap(arr,former_idx,new_idx):
    temp = arr[former_idx]
    arr[former_idx] = arr[new_idx]
    arr[new_idx] = temp

rand_nums = [i for i in range(-10,100)]
random.shuffle(rand_nums)
print(f'before {rand_nums}')

for i in range(len(rand_nums)):
    min_idx = find_min(rand_nums,start)
    swap(rand_nums,start,min_idx)
    start += 1

print(f'after {rand_nums}')

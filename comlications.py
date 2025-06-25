# def half_print(arr):
    
#     end_index = len(arr) // 2 
#     start_index = len(arr) - end_index
    
#     for i in range(end_index):
#         print(arr[i])
        
#     for j in range(len(arr) // 2):
#         print((arr[start_index]) + j)
        
# half_print([1,2,3,4,5,6,])

def half_print(arr):
    
    for i in range(len(arr) // 2):
        print(arr[i])
    
    print(f'this is i {i}')
    for j in range(len(arr) // 2):
        print(arr[i + 1 + j])
        
# half_print([1,2,3,4,5,6,])

def double_print(arr):
    for i in range(len(arr)):
        print((str(arr[i]) + '\n') * 2, end='')
# double_print([1,2,3])

def min(arr):
    smaller = float('inf')
    
    for i in range(len(arr)):
        if arr[i] < smaller:
            smaller = arr[i]
    return smaller

# smaller = min([14,2,17,8,6,-7])
# print(smaller)

def even_sum(arr):
    sum = 0
    for i in range(len(arr)):
        if not arr[i] % 2:
            sum += arr[i]
    return sum

# sum = even_sum([1,2,3,4,5,6])
# print(sum)

sub_mat = []
def sub_list(nums):
    for i in range(len(nums)):
        for j in range(len(nums) - i):
            sub_mat.append(nums[j:j+i+1])
    print(len(sub_mat))

    for row in sub_mat:
        print(row)

# sub_list([-2,-3,4,-3,1])

longest_positive_row = []
for row in sub_mat:
    sum = 0
    for num in row:
        sum += num
    if sum > 0 and len(row) > len(longest_positive_row):
        longest_positive_row = row
    sum = 0

# print(f'this is sum {sum} and this is the longest positive row {longest_positive_row}')

def find_couples(arr):
    doubles = set()
    seen = set()
    for num in arr:
       if num in seen:
           doubles.add(num)
       else:
           seen.add(num)
    return doubles

doubles = find_couples([1,1,5,8,9,5,7,2,4,5,3]) 
print(doubles)
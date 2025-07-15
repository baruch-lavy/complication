import math
def neighbors(arr,num1,num2):
    index = ''
    for num in arr:
        if num == num1:
            index = arr.index(num)
    if arr[index + 1] == num2:
        return True
    else:
        return False
# is_neighbors = neighbors([1,2,3,5,6,8,4],3,6)
# print(is_neighbors)

def sorted_mat_binary_search(mat,num):
    
    if not len(mat):
        return False
    
    middle_len = len(mat) // 2
    middle_row = len(mat[middle_len]) // 2
    
    middle = mat[middle_len][middle_row]
    
    row_index = mat.index(mat[middle_len])
    coulmn_index = mat[row_index].index(middle)  
    
    print(row_index,coulmn_index)
    if num == middle:
        return 'found' , num
    elif num < middle:
        index = coulmn_index
        new_mat = mat[:row_index + 1]
        new_mat[len(new_mat) - 1] =  new_mat[len(new_mat) - 1][:index]
        print(new_mat)
        sorted_mat_binary_search(new_mat,num)
    elif num > middle:
        sorted_mat_binary_search(mat[row_index:][coulmn_index:],num)
           
    

mat = [[1,2,3],
       [4,5,6],
       [7,8,9]]
# sorted_mat_binary_search(mat,3)


def binary_search(arr,num):
    dup = arr.copy()

    low = 0
    high  = len(arr) - 1
    
    while low < high:
       middle = len(arr) // 2
       if arr[middle] == num:
           index = dup.index(num)
           return 'found', num , index
       elif arr[middle] > num:
           high = middle
           arr = arr[low:high]
       else:
           low = middle + 1
           arr = arr[low:high]
           low = 0
    


# nums = []
# for i in range(10001):
#     nums.append(i)          
# res = binary_search(nums,8266)
# print(res)

def binary_search(arr,num):
    if not arr:
        return False
    
    low = 0
    high  = len(arr) - 1
    middle = len(arr) // 2
    
    if arr[middle] == num:
        return 'found', num 
    
    elif arr[middle] > num:
        high = middle
        arr = arr[low:high]
        return binary_search(arr,num)
        
    else:
        low = middle + 1
        arr = arr[low:high]
        return binary_search(arr,num)
        
# nums = []
# for i in range(10001):
#     nums.append(i)          
# res = binary_search(nums,5825)
# print(res)  

def find_last_zero_index(arr, offset = 0):

    low = 0
    high = 1

    while low < high:
        
        high  = len(arr) - 1
        
        if arr[0] == 0 and arr[high] == 0:
            return offset + high
        
        middle = len(arr) // 2
       
        if arr[middle] == 1:
            high = middle
            arr[:] = arr[low:high] 
            
        elif arr[middle] == 0:
            
            low = middle
            arr[:] = arr[low:high]
            offset += middle 
            low = 0

res = find_last_zero_index([0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1])
# print(res)


def merge(arr1:list,arr2:list):
    result = []

    for i in range(len(arr1)):
        if arr1[0] <= arr2[0]:
            result.append(arr1[0])
            arr1.pop(0)
            i += 1
        else:
            result.append(arr2[0])
            arr2.pop(0)
            i += 1
    return result
print(merge([2,5,8],[4,7,8]))
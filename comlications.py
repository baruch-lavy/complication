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
double_print([1,2,3])
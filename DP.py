def max_sub_list(arr):
    max_arr_local = arr[0:1]
    max_sum = 0
    max_arr_global = []
    next_num = ''
    next_num2 = 0

    for i in range(len(arr) - 1):
        next_num = arr[i + 1]
        if next_num > sum(max_arr_local):
            max_arr_local = [next_num]
            next_num2 = arr[i + 2]
        index = arr.index(next_num) 
        if (sum(max_arr_local) + next_num2) > sum(max_arr_local):
            max_arr_local = arr[0:(i + 3)]
        if next_num < 0:
            max_arr_global = arr[index:index + 2]
            if (sum(max_arr_global) + sum(max_arr_local)) > sum(max_arr_local):
                max_arr_local += max_arr_global
            print(max_arr_global)
    return max_arr_local
        
print(max_sub_list([0,5000,8,-4,30,-60]))

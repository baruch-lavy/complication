if next_num < 0:
            max_arr_global = arr[index:index + 2]
            if (sum(max_arr_global) + sum(max_arr_local)) > sum(max_arr_local):
                max_arr_local += max_arr_global
            print(max_a
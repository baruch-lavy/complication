# base_sum = int(input('base sum: '))

# def final_sum(base_sum,duration):
#     for i in range(duration):
#         for j in range(12):
#             base_sum =  munthy_sum(base_sum)
#             print(f'{j + 1} month in the {i + 1} year sum is {base_sum} \n')
#     return base_sum

# def munthy_sum(sum):
#     return sum * (1.01) + 500

# res = final_sum(base_sum,5)
# print(f'final sum is {res}')

# def sum_of_natural_numbers(num):
#     if num <= 1:
#         return num
#     return num + sum_of_natural_numbers(num - 1)

# res = sum_of_natural_numbers(10)
# print(res)


# for i in range(100):
#     print(fib(i), end=" ")

def char_counter(char,string):
    if not string: return 0
    return (char == string[-1]) + char_counter(char,string[:-1])
# print(char_counter('b','baruchbb'))

def revers_str(string):
    if len(string) == 1:
        return string
    return string[-1] + revers_str(string[:-1])

def even_count(num):
    if not num: return 0
    return ((not (num % 10) % 2)) + even_count(num//10)
# print(even_count(152086))


def max_sub_list(arr:list):
    copy = arr.copy()
    if len(arr) == 1:
        return [arr]
    for num in arr:
        if len(arr) == 0:
            arr = copy
        print(num)
        return ([arr] + max_sub_list(arr[arr.index(num):-1]))
# print(max_sub_list([5,-3,1,9,0,-6]))


def has_consecutive(arr,i=0):
    if i == (len(arr) - 2):
        return ((arr[i] + 1) == arr[-1])
    return ((arr[i] + 1) == (arr[i + 1])) or has_consecutive(arr,i = i + 1)
print(has_consecutive([1,3,5,6]))

def most_common(arr,i=0,max_num=None,max_count=0):
    if i == len(arr) - 1:
        return arr[i]
    num = arr[i]
    return arr[i]
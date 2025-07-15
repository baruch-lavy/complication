def factorial(n):
    if n == 1:
        return 1
    return n * factorial(n - 1)
# print(factorial(5))

def sum_of_digit(num):
    if num < 10:
        return num
    return num % 10 + sum_of_digit(num // 10)
# print(sum_of_digit(12345))

def revers_str(string):
    if len(string) == 1:
        return string
    return string[-1] + revers_str(string[:-1])
# print(revers_str('hello'))

def is_palindrom(word):
    if len(word) == 1:
        return True
    return word[0] == word[-1] and is_palindrom(word[1:-1])
# print(is_palindrom('racecar'))

def climb_staris(n):
    if n <= 1:
        return 1
    return climb_staris(n - 1) + climb_staris(n - 2)
# print(climb_staris(3))

def permutations(word):
    if len(word) <= 1:
        return [word]
    result = []
    for i in range(len(word)):
        char = word[i]
        remaining = word[:i] + word[i+1:]
        print(remaining)
        for perm in permutations(remaining):
            result.append(char + perm)
    return result
# print(permutations('abc'))

def subset(arr):
    if len(arr) == 0:
        return arr
    result = []
    for num in arr:
        row = subset(arr[:num])
        result.append(row)
    return result
# print(subset([1,2]))

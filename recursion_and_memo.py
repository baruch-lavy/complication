def fib(num,memo = {}):
    if num in memo:
        return memo[num]
    if num <= 2:
        return num
    memo[num] = fib(num - 1,memo) + fib(num - 2,memo)
    return memo[num]

# res = fib(50)
# print(res)

def grid_traveler(r,c,memo = {}):
    key = str(r) + ',' + str(c)
    if key in memo: return memo[key]
    if r == 1 and c == 1: return 1
    if r == 0 or c == 0: return 0
    memo[key] = grid_traveler(r-1,c,memo) + grid_traveler(r,c-1,memo)
    return memo[key]

# print(grid_traveler(200,200)) 

def factor(n):
    if n == 1: return 1
    return n * factor(n - 1)
# print(factor(100))

def can_sum(target,arr,memo = {}):
    if target in memo: return memo[target]
    if target == 0: return True
    if target < 0: return False
    for num in arr:
        if can_sum(target - num,arr): 
            memo[target] = True
            return True
    memo[target] = False
    return False

# print(can_sum(300,[7,15]))

def how_sum(target,arr):
    if target == 0: return []
    if target < 0: return None

    for num in arr:
        res =  how_sum(target - num,arr)
        if res is not None: return res + [num]
    return None
# print(how_sum(8,[4,4]))

mat = [
    [1,0,0,0,0],
    [1,1,0,0,0],
    [0,1,1,0,0],
    [1,1,1,1,1],
    [1,1,0,0,1]
    ]

def grid_course(mat,r,c):
    if r > len(mat) - 1 or c > len(mat[0]) - 1: return False
    if r == len(mat) -1 and c == len(mat[0]) - 1: return True
    location = mat[r][c]
    if location == 0: return False
    course = []
    course.append((r,c))
    print(course)
    return grid_course(mat,r + 1,c) or grid_course(mat,r,c + 1)
# print(grid_course(mat,0,0))

def is_palindrom(string):
   if len(string) <= 1:
       return True
   return string[0] == string[-1] and is_palindrom(string = string[1:-1]) 
# print(is_palindrom('racecar'))

def palindrom_cuts(string):
    if is_palindrom(string):
        return 0
    return min(1 + palindrom_cuts(string[1:]) , 1 + palindrom_cuts(string[:-1]))
# print(palindrom_cuts('eracecarf'))


def num_len(num):
    if not num // 10:
        return 1
    return 1 + num_len(num // 10)

# print(num_len(50007))
 
def reversed_num(num):
    if not num // 10:
        return str(num)
    return '' + str(num % 10) + str(reversed_num(num // 10))

# print(reversed_num(123456789))

def climb_stairs(n: int) -> int:
    if n == 1:
        return 1
    if n == 2:
        return 2
    return climb_stairs(n - 1) + climb_stairs(n - 2)
# print(climb_stairs(5))

def best_sum(target_sum: int, numbers: list[int]) -> list[int] | None:
    if target_sum == 0: return []
    if target_sum < 0: return None
    shortest = None
    for num in numbers:
        res = best_sum(target_sum - num,numbers)
        if res is not None:
            combination = res + [num]
            if shortest is None or len(combination) < len(shortest):
                shortest = combination
    return shortest
# print(best_sum(8,[2,5,7,3]))

mat = [
    [1,0,0,0,0],
    [1,1,0,0,0],
    [0,1,1,0,0],
    [1,1,1,1,1],
    [1,1,0,0,1]
    ]
def shortest_course(mat,i,j,tries = 0):
    if i > len(mat) - 1 or j > len(mat[0]) - 1: return False
    if i == len(mat) -1 or j == len(mat[0]) - 1: return tries
    down = shortest_course(mat,i + 1,j,tries + 1)
    right = shortest_course(mat,i,j + 1,tries + 1)
    return min(down,right) 
    
# print(shortest_course(mat,0,2))

def print_move(fr,to):
    print('move from ' + str(fr) + ' to ' + str(to) )
def towers(n,fr,to,spare):
    if n == 1:
        print_move(fr,to)
    else:
        towers(n-1,fr,spare,to)
        towers(1,fr,to,spare)
        towers(n-1,spare,to,fr)
# towers(15,'A','B','C')


def can_constract(target,word_bank):
    if target == '' : return True
    for word in word_bank:
        if target.startswith(word):
            if can_constract(target[len(word):],word_bank):
                return True
    return False
# print(can_constract("abcdef", ["ab", "abc", "cd", "def", "abcd"]))



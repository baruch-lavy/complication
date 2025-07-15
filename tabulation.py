def climb_stairs(n):
    table = [0] * (n + 1)
    print(table)
    table[0] = 1  # 1 way to stand still
    for i in range(n):
        table[i + 1] += table[i]
        print(table)
        if i + 2 <= n:
            table[i + 2] += table[i]
            print(table)
    return table[n]
# print(climb_stairs(4))

def can_sum(n,nums):
    table = [False] * (n + 1)
    table[0] = True

    for i in range(n + 1):
        if table[i]:
            for num in nums:
                if i + num <= n:
                    table[i + num] = True
                    print(i,table)
    return table[n]
# print(can_sum(4,[2]))

def count_constract(target,word_bank):
    table = [0] * (len(target) + 1)
    table[0] = 1

    for i in range(len(target) + 1):
        if table[i] > 0:
            for word in word_bank:
                if target[i:i + len(word)] == word:
                    print(i,target[i:i + len(word)])
                    table[i + len(word)] += table[i]
                    print(table)
    return table[len(target)]

# print(count_constract("purple", ["purp", "p", "ur", "le", "purpl"]))

def all_construct(target, word_bank):
    table = [[] for _ in range(len(target) + 1)]
    table[0] = [[]]

    for i in range(len(target) + 1):
        for word in word_bank:
            if target[i:i + len(word)] == word:
                new_combinations = [comb + [word] for comb in table[i]]
                print(new_combinations)
                table[i + len(word)] += new_combinations

    return table[len(target)]

print(all_construct("purple", ["purp", "p", "ur", "le", "purpl"]))

def fib(n):
    table = [0] * (n + 1)
    table[1] = 1

    for i in range(n + 1):
        if table[i] != 1:
            table[i] = table[i - 1] + table[i - 2]
    return table[n]
print(fib(6))
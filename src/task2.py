def oddNumbers(start, stop):
    odd_nums = []
    for num in range(start, stop+1):
        if num % 2 != 0:
            odd_nums.append(num)
    return odd_nums

start = 2
stop = 34
result = oddNumbers(start, stop)
print(result)

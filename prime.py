def prime(num):
    list_1 = []
    if num == 2:
        return 'prime'
    for i in range(2, num):
        if num % i == 0:
            return 'not prime'
    return 'prime'


print(prime(3))

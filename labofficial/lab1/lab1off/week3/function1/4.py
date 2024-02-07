def prime(list):
    prime_nums = []
    for x in list:
        if x <= 1:
            continue
        if x <= 3:
            prime_nums.append(x)
            continue
        i = 2
        count = 0
        while i < x:
            if x%i == 0:
                count += 1
            i += 1
        if count == 0:
            prime_nums.append(x)
    print(prime_nums)
list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
prime(list)
            
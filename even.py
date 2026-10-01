def count_even(m):
    counter = 0
    for i in range(1,m+1):
        if i % 2 == 0:
            return counter+1
print(count_even(5))



def digit_sum(n):

    numbers = []
    temp = n
    n_in_string = str(n)
    for i in range(len(n_in_string)):
        numbers.append(temp % 10)
        temp = temp // 10
    print numbers

    print sum(numbers)

n = 1234
digit_sum(n)
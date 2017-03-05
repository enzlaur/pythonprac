def is_prime(x):
    count = 0
    if x <= 1:
        return False
    elif x <= 3:
        return True
    else:
        for n in range(2, x):
            if x % n == 0:
                print x, " % ", n
                return False
        else:
            return True

#print '2', is_prime(2)
print 'Number is 3: ', is_prime(3)
#print '4', is_prime(4)
print 'Number is 5: ', is_prime(5)
print 'Number is 12: ', is_prime(12)
from math import sqrt

"""
    AUTHOR = LAURENZ TOLENTINO
    This is a Bisection Method Calculator
    Please see http://planetcalc.com/3712/ for corrections
"""
__author__ = "Laurenz"
# Value for your A
a = 1
# Value for your B
b = 2
# Number of Iterations to be done
iteration = 10
# "full" to print f(a) and f(b) with a, b, and c values together
# "min" to print only the step count, value of c (written as X) and f(c) (written as F(X))
show = "full"

""" - - - - - - - - - - - - MAGIC BELOW - - - - - - - - - - - - - """
def equ(x):
    result = float((x ** 5) - 11)
    return result

def getC(a,b):
    # The one on Ms. Shirley's slides
    #c = ( ( (a* (equ(b) ) ) - (b*(equ(a) ) ) ) / ( equ(b) - equ(a) ) )
    # The one on planetcalc and previous class on AY ago
    #c = b - ( equ(b) * ( (b-a) / (equ(b) - equ(a)) ) )
    #c = b - ( ( (equ(b)*b) - (equ(b)*a) ) / (equ(b) - equ(a)) )
    # Fixed the error of floats and negative numbers not taken to effect
    b1 = float(equ(b))
    b2 = float( ( (b-a) / (equ(b) - equ(a) )))
    c = b - b1*b2
    return c

def bisection(a,b, iteration, show):
    c  = getC(a, b)
    fa = equ(a)
    fb = equ(b)
    fc = equ(c)
    if show == "full":
        print "x%d" % (iteration + 2)
        print "a = ", a, "b = ", b, "\nc or x = ", c
        print "f(a) = " , fa, "f(b) = %.4f" % (fb), "f(c) = %.4f" % (fc)
    elif show == "min":
        print "[Step: x%d] X = %.4f F(X) = %.4f" % (iteration+2, c, fc)
    else:
        print "[Step: x%d] X = %.4f F(X) = %.4f" % (iteration+2, c, fc)
    return fc

def runBisection(a,b,iteration,show):
    print "\n" \
          "REGULA FALSI METHOD" \
          "\n"
    for ite in range(iteration):
        bisec = bisection(a,b, ite, show)
        c = getC(a,b)
        if bisec <= 0:
            a = c
        else:
            b = c
        print "\n"

runBisection(a,b,iteration,show)






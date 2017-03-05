
# https://www.codecademy.com/courses/python-intermediate-en-rCQKw/2/1?curriculum_id=4f89dab3d788890003000096

#    Define a function called count that has two arguments called sequence and item.
#   Return the number of times the item occurs in the list.
#     For example: count([1,2,1,1], 1) should return 3 (because 1 appears 3 times in the list).
#
#     There is a list method in Python that you can use for this, but you should do it the long way for practice.
#     Your function should return an integer.
#     The item you input may be an integer, string, float, or even another list!
#     Be careful not to use list as a variable name in your code-it's a reserved word in Python

testSequence = [1, 2, 3, 1, 1]
testCounter  = 1

def count(sequence, counter):
    count = 0
    for item in sequence:
        if item == counter:
            count += 1
    return count

print "Count for ", testCounter, "is", count(testSequence, testCounter)
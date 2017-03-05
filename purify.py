sampleList = [1,2,3,4,4,5]

def purify(input):
    result = []
    for i in sampleList:
        if i % 2 == 0:
            result.append(i)
    return result

print purify(sampleList)
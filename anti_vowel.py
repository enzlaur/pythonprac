vowels = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']

def textToList(text):
    result = []
    for c in text:
        result.append(c)
    return result

def anti_vowel(text):
    textList = []
    # Populate list using contents from 'text" or string to
    #lists
    textList = textToList(text)
    result = []
    # Some kind of loop
    for c in textList:
        skip = False
        for vowel in vowels:
            if c == vowel:
                skip = True
                print c, skip
                break
        else:
            if skip == False:
                result.append(c)


    # Print the result
    return "".join(result)

print anti_vowel(anti_vowel("Yab Gab to Trab Yab Yab Aeiouz"))
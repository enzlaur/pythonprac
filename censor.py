def splitText(text):
    return text.split()

def censor(text, toCensor):
    # Number of letters on the word that will be replaced
    wordLength = len(toCensor)
    # Fills up the censored word with *****
    overlay = '*' * wordLength
    # Splits text into a list
    words = splitText(text)
    # Results list
    final = []
    # Conditional loop for finding words to be replaced
    for word in words:
        if word == toCensor:
            final.append(overlay)
        else:
            final.append(word)

    return " ".join(final)

print censor("this hack is wack hack", "hack")
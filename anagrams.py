def anagrams(words):
    """
    given a list of words, return a list of subsets of the words that
    are all anagrams of one another
    """

    anagrams = {}
    for word in words:
        wordAsList = "".join(sorted(list(word))).strip()
        if anagrams.has_key(wordAsList):
            anagrams[wordAsList].append(word)
        else:
            anagrams[wordAsList] = [word]

    return anagrams

print(anagrams(["bat","tab","ball","lab","cab","bac","back","eleven plus two", "twelve plus one"]))

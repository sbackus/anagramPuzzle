from math import factorial


def anagramIndex(word):
    return anagram0Index(word) + 1


def anagram0Index(word):
    if (len(word) == 1):
        return 0
    else:
        counted_anagrams = 0
        for char in alphabetically_before_first_char(word):
            counted_anagrams += num_anagrams_starting_with(word, char)
        counted_anagrams += anagram0Index(word[1:])
        return counted_anagrams


def num_anagrams_starting_with(word, char):
    char_index = word.find(char)
    char_removed = word[:char_index] + word[char_index+1:]
    return perms(char_removed)


def alphabetically_before_first_char(word):
    return set([c for c in word if c < word[0]])


def perms (word):
    multiplicities = {}
    for char in word:
        multiplicities[char] = multiplicities.get(char, 0) + 1 

    val = factorial(len(word))
    for div in multiplicities.values():
        val /= div
    return val

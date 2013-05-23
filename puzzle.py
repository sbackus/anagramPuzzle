from math import factorial


def anagramIndex(word):
    return anagram0Index(word) + 1


def anagram0Index(word):
    # Explanation of algorithm:
    #
    # Example: CABA
    #
    # AABC
    # AACB
    # ABAC
    # ABCA
    # ACAB
    # ACBA
    # BAAC
    # BACA
    # BCAA
    # CAAB
    # CABA
    # CBAA
    #
    # To find the index of CABA, we need the sum of:
    # * the number of # anagrams that start with A
    # * the number of anagrams that start B, and
    # * CABA's index within the anagrams that start with C.
    # The number of anagrams that start with A is the total number of
    # anagrams of ABC, and the number of anagrams that start with B is
    # the total number of anagrams of AAC.  CABA's index within the
    # anagrams that start with C is just ABA's index within its own list
    # of anagrams.
    #
    # More generally: for each letter that's earlier in the alphabet,
    # add the number of anagrams (permutations) of what's left of the
    # word without that letter.  Also add the index of the word without
    # its first letter.
    #
    # Complexity: (Assuming the number of different characters and the
    # length of the list are proportional.) This recurses n times, and 
    # calls an O(n) function inside an O(n) loop. O(n^3) is
    # much better than the O(n!) solution of generating the list of
    # anagrams.

    # head = word[0]
    # tail = word[1:]

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

from math import factorial

def anagramIndex(word):
	return anagram0Index(word)+1

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
    # length of the list are proportional.) This recurses n times, once
    # for each character it removes from the list.  It calls a couple
    # O(n) functions and has an O(n) loop.  O(n * (n + n + n)) = O(n^2),
    # much better than the O(n!) solution of generating the list of
    # anagrams.

	# head = word[0]
	# tail = word[1:]
	if (len(word) == 1):
		return 0
	else:
		i = 0
		for c in alphabetically_before_first_char(word):
			w = word
			w = w[:w.find(c)]+w[w.find(c)+1:] #remove c from w
			i += perms(w)
		i += anagram0Index(word[:1])
		return i



def alphabetically_before_first_char(word):
	return set([c for c in word[1:] if c < word[0]])

def perms (word):
	multiplicities = {}
	for char in word:
		multiplicities[char] = multiplicities.get(char,0) +1 
	fact = factorial(len(word))
	for key in multiplicities:
		fact = fact/factorial(multiplicities[key])	
	return fact

def val(word, head):
	word_set = set(word)
	word = list(word_set)
	word.sort()
	return word.index(head)

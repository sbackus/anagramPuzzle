from math import factorial

def anagramIndex(word):
	return anagram0Index(word)+1

def anagram0Index(word):
	# head = word[0]
	# tail = word[1:]
	if (len(word) == 1):
		return 0
	else:
		i = 0
		for c in alphabetically_before_first_char(word[0]):
			w = word.copy()
			i += perms(w.remove(c))
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
#05
def n_gram(target, n):
    result = [target[i:i + n] for i in range(len(target) - n + 1)]
    return result

letter = 'I am a NLPer'
word = letter.split()

# unigram
print(n_gram(letter, 1))
print(n_gram(word, 1))

# bigram
print(n_gram(letter, 2))
print(n_gram(word, 2))

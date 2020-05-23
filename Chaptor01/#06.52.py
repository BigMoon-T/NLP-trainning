#06.52
#From 05
def n_gram(target, n):
    result = [target[i:i + n] for i in range(len(target) - n + 1)]
    return result

sentence1 = 'hippopotomonstrosesquippedaliophobia'
sentence2 = 'phobophobia'

X = set(n_gram(sentence1, 2))
Y = set(n_gram(sentence2, 2))

pprint('Union', X | Y)
print('Intersection', X & Y)
print('Difference', X - Y)

print('If "se" is contained')
print('X:', 'se' in X)
print('Y:', 'se' in Y)

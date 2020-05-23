#04
org_sentence = 'Hi He Lied Because Boron Could Not Oxidize Fluorine. New Nations Might Also Sign Peace Security Clause. Arthur King Can.'
word_list = org_sentence.split()

atomics_sym1 = {}
for i, word in enumerate(word_list, 1):
    if i in [1, 5, 6, 7, 8, 9, 15, 16, 19]:
        atomics_sym1[word[0]] = i
    else:
        atomics_sym1[word[:2]] = i

print(atomics_sym1)

# Modified Mi to Mg
atomics_sym2 = {}
for i, word in enumerate(word_list, 1):
    if i in [1, 5, 6, 7, 8, 9, 15, 16, 19]:
        atomics_sym2[word[0]] = i
    elif i in [12]:
        atomics_sym2[word[0:3:2]] = i
    else:
        atomics_sym2[word[:2]] = i

print(atomics_sym2)


# Comprehension
atomic_sym3 = {word[0] if i in {1, 5, 6, 7, 8, 9, 15, 16, 19}\
     else word[:2]: i for i, word in enumerate(word_list, 1)}
print(atomic_sym3)

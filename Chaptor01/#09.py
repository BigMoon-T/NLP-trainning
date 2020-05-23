#09
import random

def Typoglycemia(sentence):
    result = []
    for word in sentence.split():
        if len(word) >= 4:
            char_list = list(word[1:-1])
            random.shuffle(char_list)
            result.append(word[0] + ''.join(char_list) + word[-1])
        else:
            result.append(word)

    return ' '.join(result)

sentence = input()
print(Typoglycemia(sentence))
print("Original sentence: I couldn't believe that I could\
 actually understand what I was reading : the phenomenal power of the human mind")

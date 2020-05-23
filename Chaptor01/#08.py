#08
def cipher(sentence):
    result = ''
    for i in range(0, len(sentence)):
        if sentence[i].islower():
            result += chr(219 - ord(sentence[i]))
        else:
            result += sentence[i]
    return result

print(cipher(input()))

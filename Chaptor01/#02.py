#02
list1 = list('パトカー')
list2 = list('タクシー')
new_str = ''

for l1, l2 in zip(list1, list2):
    new_str += l1 + l2

print(new_str)

#Optimised
result = [s1+s2 for s1, s2 in zip ('パトカー', 'タクシー')]
print(''.join(result))

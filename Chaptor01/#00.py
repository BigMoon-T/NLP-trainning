#00 Reverse strings
#reversed()
org_str = 'stressed'

new_str = ''.join(reversed(org_str))
print(new_str)

#tuple
new_tuple = org_str[::-1]
print(new_tuple)

#Optimised
print('stressed'[::-1])

#03
org_str = 'Now I need a drink, alcoholic of course, after the heavy lectures involving quantum mechanics.'

for word in org_str.split():
    print(len(word.strip(',.')), word.strip(',.'))

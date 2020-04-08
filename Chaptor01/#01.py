#01パタトクカシーー
org_str = 'パタトクカシーー'

new_list = list('パタトクカシーー')
#パトカー
print(''.join(new_list[::2]))
#タクシー
print(''.join(new_list[1::2]))

#Optimised
print(''.join(list('パタトクカシーー')[::2]))
print(''.join(list('パタトクカシーー')[1::2]))

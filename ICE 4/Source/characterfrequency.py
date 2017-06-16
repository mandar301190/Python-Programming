string_I = input('enter the string: ')

set = set(string_I)
print("set",set)

Z = {}

for I in set:
  Z[I] = string_I.count(str(I))
  print(Z)
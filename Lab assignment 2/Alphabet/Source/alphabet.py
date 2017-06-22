import string

alphabet = set(string.ascii_uppercase)
string1 = 'abcdefghijklmnopqrstuvwxyz'
print(set(string1.upper()) >= alphabet)
string2 = 'abcdefghijklmnostuvwxyz'
print(set(string2.upper()) >= alphabet)
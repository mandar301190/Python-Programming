import string         #Here we are importing string function to take input from user in terms of string

alphabet = set(string.ascii_uppercase)      #All the chnaracters in string is to be declared as in uppercase
string1 = 'Sphinx of black quartz, judge my vow”: Used by Adobe InDesign to display font samples' #The sentence which contains all the alphabets
print(set(string1.upper()) >= alphabet)          #Print the string
string2 = 'Sphinx of black quartz, judge my vow”: Used by Adobe InDesign to display font samples'
print(set(string2.upper()) >= alphabet)
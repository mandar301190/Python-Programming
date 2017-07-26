import nltk

f = open("big.txt")
print(f.read())

from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
example_sentence = 'The sun is a vivid creation done by the nature. Included is the important information about your specific rights and restriction.'
stop_words = set(stopwords.words("english"))

print(stop_words)

from nltk.stem import WordNetLemmatizer
#lemmtizer = WordNetLemmatizer()
#print(lemmtizer.lemmatize('stopped', pos='v'))
#print(lemmtizer.lemmatize('encoding', pos='v'))
#print(lemmtizer.lemmatize('making', pos='v'))
#print(lemmtizer.lemmatize('encoding', pos='v'))
#print(lemmtizer.lemmatize('said', pos='v'))
#print(lemmtizer.lemmatize('setting', pos='v'))

f = open("big.txt", "r")
n=[]
text = f.read()
lemmatizer = WordNetLemmatizer()
for i in word_tokenize(text):
  print(i+" "+lemmatizer.lemmatize(i,pos='v'))
  n.append(lemmatizer.lemmatize(i,pos='v'))

print(n)

import operator
txtFile = open("big.txt").readlines()
txtFile = " ".join(txtFile) # this with .readlines() replaces new lines with spaces
txtFile = "".join(char for char in txtFile if char.isalnum() or char.isspace()) # removes everything that's not alphanumeric or spaces.

word_counter = {}
for word in txtFile.split(" "): # split in every space.
    if len(word) > 0 and word != '\r\n':
        if word not in word_counter: # if 'word' not in word_counter, add it, and set value to 1
            word_counter[word] = 1
        else:
            word_counter[word] += 1 # if 'word' already in word_counter, increment it by 1

for i,word in enumerate(sorted(word_counter,key=word_counter.get,reverse=True)[:10]):
    # sorts the dict by the values, from top to botton, takes the 10 top items,
    print("%s: %s - %s"%(i+1,word,word_counter[word]))

f = open(txtFile)
print(f.read())




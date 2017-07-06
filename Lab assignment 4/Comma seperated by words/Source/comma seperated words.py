
#Bag contains number of input as list of words where user can enter their list of words.

Bag = input("Enter you Words:-")
words = [word for word in Bag.split(",")]
         #Number of words will be splitted by split function and comma. It will then arrange alphabetically.

print(",".join(sorted(list(set(words)))))
         #Prints number of words splitted by comma
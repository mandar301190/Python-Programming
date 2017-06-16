def main ():
    text = input("Please input a List of words to evaluate: ")
    longest = 0

    for words in text.split():
           if len(words) > longest:
                  longest = len(words)
    print ("The longest word is", words, "with lenght", longest)


main()

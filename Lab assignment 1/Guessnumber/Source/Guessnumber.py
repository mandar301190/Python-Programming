import random

GuessesTaken = 0

number = random.randint(1,9)
print('Guess my favourite number')

while GuessesTaken < 6:
    print('Guess it')
    Guess = input()
    Guess = int(Guess)

    GuessesTaken = GuessesTaken + 1

    if GuessesTaken < number:
        print('Guess is low')

    if GuessesTaken > number:
        print('Guess is high')

    if GuessesTaken == number:
        break

if Guess == number:
    GuessesTaken = str(GuessesTaken)
    print('Well done, You guessed correct')

if Guess != number:
    print('No, Your guess is wrong whereas my number is different')
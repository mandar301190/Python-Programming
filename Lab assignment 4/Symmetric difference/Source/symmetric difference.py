
#Both sets x and y will contain number of different names in it as mentioned below.

setx = set(["Justin", "Cliffard", "Sebastian", "Oswin", "Jeremy", "Mike", "Alfred", "Silvia"])
sety = set(["Jeremy", "Justin", "Jameson", "Latasha", "Mike", "Thomas", "George", "Bob"])

object = setx ^ sety   #setc is a functional command which is used to display symmetric contents of two different sets.
print(object)          #Prints the final computed value of setc

#Note- Names contain in both sets will keep on change position each time you print.
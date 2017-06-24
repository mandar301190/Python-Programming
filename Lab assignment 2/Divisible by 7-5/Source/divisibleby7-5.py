number=[]      #Number has been taken from user
for y in range(1500, 2700):      # Range of numbers has been specified within we have to print numbers divisible by given values
    if (y%7==0) and (y%5==0):       #Modulo function has been defined and divisor numbers such as 7 and 5
        number.append(str(y))
print (','.join(number))      #Print the final number  by concatenating all values in string
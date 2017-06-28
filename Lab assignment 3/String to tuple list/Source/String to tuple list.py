#Take the value from user in terms of numbers or letters and it should be seperated by comma
values = input("Enter your Input numbers or letters seperated by comma : ")
list = values.split(",")   #Seperating the values using split() function by comma in between and assigning to list
tuple = tuple(list)       #Seperating the values using split() function by comma in between and assigning to tuple

#Printing values assigned in list and tuple
print('List : ',list)
print('Tuple : ',tuple)
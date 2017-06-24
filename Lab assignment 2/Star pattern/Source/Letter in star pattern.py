result_str="";
print("Star pattern for the name 'Mandar' as follows:-");
for row in range(0,7):
    for column in range(0,6):
        if (column == 1 or column == 5 or (row == 2 and (column == 2 or column == 4)) or (row == 3 and column == 3)):
            result_str=result_str+"* "
        else:
            result_str=result_str+"  "   #Here star will be displayed if columns assigned above would be equal to each other.
    result_str=result_str+"\n"
print(result_str);

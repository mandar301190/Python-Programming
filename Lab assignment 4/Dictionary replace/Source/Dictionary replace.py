def sum_math_marks_marksi_average(dicts):    #Function has been defined to calculate average
    for d in dicts:
        number1 = d.pop('Marks')         #pop method is used to remove given item in list by its index value
        number2 = d.pop('MarksI')
        d['Marks+MarksI'] = (number1 + number2)/2    #formula mentioned to calculate sum of numbers
    return dicts                   #returns calculated distionary value
Mandar= [
  {'Batch' : 1, 'Course' : 'Biology', 'Marks' : 75, 'MarksI' : 85},       #List[] has been allotted by mentioning atleast three dictionaries in it
  {'Batch' : 2, 'Course' : 'Chemistry', 'Marks' : 89, 'MarksI' : 97},
  {'Batch' : 3, 'Course' : 'psycology', 'Marks' : 92, 'MarksI' : 88}
]
print(sum_math_marks_marksi_average(Mandar))           #Prints sum value


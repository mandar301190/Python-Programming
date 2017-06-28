#Last number has been defined by returing -1 value which is index value position of given tuple.
def last(number): return number[-1]

#Sorting the given tuple by using sort function and returns the sorted key value which is last number
def sort_list_last(tuples):
    return sorted(tuples, key=last)

#This is the given list which we are going to sort in ascending order.
print(sort_list_last([(1, 6), (1, 7), (4, 5), (2, 2), (1, 3)]))
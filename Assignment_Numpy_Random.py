import numpy

#Generate random 100 numbers between 1 and 500
arr =numpy.random.randint(1,500,100)
print(arr)
#Delete duplicate values using unique function
x = numpy.unique(arr)
print(x)
#sort the array using sort
y = numpy.sort(x)
print("Sorted array is given as: ", y)

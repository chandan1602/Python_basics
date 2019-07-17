#difference between lambda() and def()
def cube(y):
    return y**3

g=lambda x: x**3
print('Lambda result : ', g(7))
print('def result : ', cube(5))

#use of filter() in lambda()
#filter takes in 2 arguments
#1st => function
#2nd => arguments to be passed in a function
#and filter outs the elements for which fn returns true
li=[1,2,3,4,5,6,7,8,9]
final_list = list(filter(lambda x: (x%2 != 0), li))
print('The filter list : ',final_list)

#use of lambda() with map()
#map takes in 2 arguments
#1st => function
#2nd => arguments to be passed in a function
#and a new list is returned that contains the lambda modified items
li = [1,2,3,4,5,6,7,8,9]
final_list = list(map(lambda x: (x*2), li))
print('The map list : ',final_list)

#use of lambda() with reduce()
#reduce takes in 2 arguments
#1st => function
#2nd => arguments to be passed in a function
#and a new reduced result is returned out of repetetive op. over the
#pairs of the list
from functools import reduce
li = [1,2,3,4,5,6,7,8,9]
sum=reduce((lambda x,y:x+y),li)
print(sum)

#more than 1 arguments
x = lambda a,b: a*b
print(x(5,6))

#more uses of lambda
def myfunc(n):
    return lambda a:a*n
mydoubler = myfunc(2)
mytripler = myfunc(3)
print(mydoubler(11))
print(mytripler(11))




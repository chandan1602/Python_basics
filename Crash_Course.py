#This is a crash course on python


'''
#VARIABLES AND STRINGS
------------------------------

print("Hello World!!")

msg="Hello World!!"
print(msg)

f_name="Chandan"
age="19"
msg="Hi " + f_name + ", your Age is " + age
print(msg)
'''

'''
#LISTS
------------------------------------------

bikes = ['trek', 'redline', 'giant']
first_bike = bikes[0] #get first name in the list
last_bike = bikes[-1] #get last name in the list
print(first_bike)
print(last_bike)

#Looping through list
for bike in bikes:
    print(bike)

#Adding items to list
bikes = []
bikes.append('Yamaha')
bikes.append('Hero')
bikes.append('Honda')
bikes.insert(2, 'Harley Davidson')
bikes.insert(3, 'Bullet')
del bikes[-1]
bikes.remove('Hero')
for indian in bikes:
    print(indian)


#Popping elements
recent_bike = bikes.pop()
print('The popped recent bike is : ', recent_bike)

first_bike = bikes.pop(0)
print('The popped first bike is : ', first_bike)


#List Length
num_bikes = len(bikes)
print('We have ' + str(num_bikes) + ' bikes')

#Making numerical list
squares = []
for x in range(1, 11):
    squares.append(x**2)
for numerics in squares:
    print(numerics)

#List Comprehensions
squares = [x**3 for x in range(1, 11)]
for numerics in squares:
    print(numerics)

#Slicing a list
finishers = ['sam', 'bob', 'ada', 'bea']
first_two = finishers[:2]
print(first_two)

#Copying of a list
copy_of_bikes = bikes[:]
for indian in copy_of_bikes:
    print(indian)
'''


'''
#TUPLES(Similar to lists but the items cannot be modified)
----------------------------------


dimensions = (1920, 1980, 2040)
for years in dimensions:
    print(years)
'''


'''
#DICTIONARIES(Store connections between pieces of information. Each item in a dictionary is a key-value-pair)
#-----------------------------------------------

alien = {'color' : 'green', 'points' : '5'}

#Accessing a value
print("The alien's color is " + alien['color'] + ". So the points awarded are " + alien['points'])

#Adding a new-key-value pair
alien['x_position'] = '0'
print("The x position of the alien is : " + alien['x_position'])

#Looping through all key-value pairs
fav_numbers = {'first' : 7, 'second' : 1}
for positions, values in fav_numbers.items():
    print(positions + ' is for ' + str(values))

#Looping through all keys
fav_numbers = {'first' : 7, 'second' : 1}
for name in fav_numbers.keys():
    print(name + ' is for a good number')

#Looping through all the values
fav_numbers = {'first' : 7, 'second' : 1}
for values in fav_numbers.values():
    print('The number ' + str(values) + ' is an exception')



'''

'''
#WHILE LOOP: special case :: letting a user when to exit the loop
#-------------------------------------



msg = ' '
while msg != 'exit':
    msg = input("Whats your message : ")
    print(msg)
'''


'''
#FUNCTIONS
#---------------------------------------------

name = input('Enter your Name : ')

def hey(name = 'Chandan'): #Default values for parameters
    print('Entered name :',name)
    if name == 'Chandan':
        return 'Authorised User ' #Returning a value 
    else:
        return 'Warning!! Unauthorised User'
message = hey()
print(message)

message = hey('Abhishek') #Passing an Argument
print(message)

message = hey(name)
print(message)
'''


'''
#CLASSES
#------------------------------------


class A:
    age=90
    def __init__(self,n):
        self.name=n
    def display(self):
        print("Name is :",self.name)
        print("Age is :",__class__.age)
obj=A("anc")
obj.display()
'''




'''
#WORKING WITH FILE
#-----------------------------------

filename = 'FirstFile.txt'
with open(filename) as file_object:
    lines = file_object.readlines()

with open(filename, 'w') as file_object1:
    file_object1.write('I Love Programming!')

with open(filename, 'a') as file_object2:
    file_object2.write(' Programming is Fun')

for line in lines:
    print(line)
'''


'''
#EXCEPTION
----------------------------------

prompt = 'How many tickets do you need : '
num_tickets = input(prompt)

try:
    num_tickets = int(num_tickets)
except ValueError:
    print('Please try again!')
else:
    print('Your tickets are printing!')

'''

import numpy
from functools import reduce
n = int(input())
val = []
for i in range(0,n,1):
    plucks = int(input())
    # for i in range(0,plucks,1):
    #     net.append(int(input()))
    net = list(map(int, input().split()))
    arr=net[:]
    arr.pop()
    net.pop(0)
    net = numpy.subtract(net,arr)
    net = numpy.subtract(net,1)
    val.append(reduce((lambda x,y:x+y), net))
    
for total in val:
    print(total)








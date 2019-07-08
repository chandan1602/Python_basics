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
------------------------------

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
for indian in bikes:
    print(indian)

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
-----------------------------------------------

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
-------------------------------------

msg = ' '
while msg != 'exit':
    msg = input("Whats your message : ")
    print(msg)
'''


'''
#FUNCTIONS
-------------------------------------

name = input('Enter your Name : ')

def hey(name = 'Chandan'): #Default values for parameters
    print('Entered name : ', name)
    if name == 'Chandan':
        return 'Authorised User' #Returning a value 
    else:
        return 'Warning!! Unauthorised User'
message = hey()
print(message)

message = hey('Abhishek') #Passing an Argument
print(message)

message = hey(name)
print(message)
'''


#CLASSES









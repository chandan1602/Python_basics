'''
Loops
--------------
    are used to execute the block of statements repeatedly.

    1)for loop
    2)while loop

    1)for loop
    -----------------
        used when we known how many times loop will be executed.


        syntax
        -------------
        for var_name in range(starting,end+1,incre/dec):
                #statement

        and
        
        for var_name in arrayname:
            #statement


            
example
-----------
for i in range(1,11,1):
    print(i,end=' ')
    
for i in range(10,0,-1):
    print(i,end=' ')

for i in range(1,11,2):
    print(i,end=' ')
--------------------------------------

#table
#factorial
#fibonacci series
0  1   1    2  3 5 8
a  b  c=a+b
   a   b
#perfect number : 6 :1+2+3=6   sum of factor is same number : 6,28,496
#prime number
--------------------------------------------------------------------------

2)while loop
-------------
    used when we don't know how many times loop will be executed.

    syntax
    ----------
    initialize
    while condition:
        #statements
        incre/dec

        

example
--------
i=0
while i<=10:
    print(i)
    i=i+1
---------------------------------

1)sum of digit
2)reverse
3)palindrome number
4)armstrong number : 153 :1(3)+5(3)+3(3)=1+125+27=153
-------------------------------------------

3)nested loop
----------------
    syntax
    --------
    for var_name in range(start,end,incre/dec):
            for var_name in range(start,end,incre/dec):
                #statement


*
**
***
****
#PATTERNS
#stars case-1
for i in range(1,5,1):
    for j in range(1,i+1,1):
        print('*',end='')
    print()
'''

#FOR LOOP
#table
num=int(input("Table(Enter a number) : "))
print(num)
first=num
for i in range(1, 10, 1):
    num=first+num
    print(num)

#factorial
num=int(input("Factorial(Enter a number) : "))
factorial = 1
for i in range(num, 1, -1):
    factorial = i*factorial
print(factorial)

'''
#fibonacci series
num=int(input("Fibonacci series(Enter a number) : "))
a=0
b=1
for i in range(1, , 1):
    sum=sum+i
print(sum)
'''

#perfect number
num=int(input("Perfect number(Enter a number) : "))
perfect=0
for i in range(1, num, 1):
    if num%i==0:
        perfect=perfect+i
if num==perfect:
    print("perfect")
else:
    print("no")

#prime number
num=int(input("Prime number(Enter a number) : "))
net=0
for i in range(2, num, 1):
    if num%i==0:
        var=1
    else:
        var=0
    net=net+var
if net==0:
    print("It is a prime number")
else:
    print("It is not a prime number")
        
        

#WHILE LOOP
#sum of digit
num=int(input("Sum of the digits(Enter a number) : "))
net=0
i=0
while i<=len(str(num))+1:
    rem=num%10
    num=(num-rem)/10
    net=net+rem
    i=i+1
print("The sum of the digits is : ", int(net))


#reverse
num=int(input("Reverse(Enter a number) : "))
i=0
temp=num
reverse=0
while num>0:
    rem=num%10
    num=num//10 #num=(num-rem)/10
    reverse=(reverse*10)+rem
print("The reverse is : ",int(reverse))

#palindrome
if reverse==temp:
    print("The Entered number is a Palindrome")
else:
    print("The Entered number is not a Palindrome")

#Armstrong number
num=int(input("Armstrong number(Enter a number) : "))
net=0
i=0
while i<=len(str(num))+1:
    rem=num%10
    num=(num-rem)/10
    net=net+(rem*rem*rem)
    i=i+1
print("The Armstrong number is : ", net)

#PATTERNS
#numbers-case1
for i in range(1, 5, 1):
    for j in range(1, i+1, 1):
        print(j, end=' ')
    print()

#numbers-case2
print("--------------------------------------")
for i in range(1, 5, 1):
    for j in range(1, i+1, 1):
        print(i, end=' ')
    print()

#stars case-2
print("--------------------------------------")
for i in range(1, 5, 1):
    for j in range(5, i+1, -1):
        print(" ",end=" ")
    for k in range(1, i+1, 1):
        print("*", end="   ")
    print()

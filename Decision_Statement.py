'''
Control statements
---------------------
    1)Decision statement
    2)Loops
    3)Jumping statement

    1)Decision statements
    ---------------------
            are used to take a decision according some conditions.

            1)if statement
            2)if else statement
            3)if elif statement
            4)nested if elif statement

            1)if statement
            -------------------
                synatx
                ----------
                if condition:
                    #statement

            2)if else statement
            -------------------
                synatx
                ----------
                if condition:
                    #statement
                else:
                    #statement

example
---------------
a=int(input("Enetr First Number: "))
b=int(input("Enetr Second Number: "))


if a>b:
    print("a is greater")
else:
    print("b is greater")
-------------------------------------------------
Questions
-----------------
#even/odd number
#leap year
#-ve /+ve
#divisible by 5 and 10
#enter character and check entered character is alphabet or not
#enter character and check charcater is vowel or not

#if driver is married and gender is male and age is greater than 28
if driver is married and gender is female and age is greater than 25
if driver is unmarried and gender is male and age is greater than 32

driver is insured.
---------------------------------------------------------------------------------
3)if elif statement
-------------------
    used for multiple conditions.

    syntax
    ----------
    if condition:
        #statement
    elif condition:
        #statement
    else:
        #statement

    //greatest among three number
    

4)nested if elif statement
--------------------------
    syntax
    --------
    if condition:
        if condition:
            #statement
        else:
            #statement
    else:
        if condition:
            #statement
        else:
            #statement

    //greatest among three numbers
    
----------------------------------------
example
---------------------------------------
a=int(input("Enter First Number:"))
b=int(input("Enter Sec Number:"))
c=int(input("Enter Third Number:"))


if a>b:
    if a>c:
        print("a is greater")
    else:
        print("c is greater")
else:
    if b>c:
        print("b is greater")
    else:
        print("c is greater")
------------------------------------------
'''

#even/odd number
'''
num = float(input("ODD/EVEN(Enter a number) : "))
if isinstance(num, int):
    if num%2==0:
        print("The number is even")
    else:
        print("The number is odd")
else:
    if isinstance(num, float):
        if (num*10)%2==0:
            print("The number is even")
        else:
            print("The number is odd")
'''
num = int(input("ODD/EVEN(Enter a number) : "))
if num%2==0:
    print("The number is even")
else:
    print("The number is odd")

#leap year
year = int(input("Leap Year test(Enter your current year) : "))
if year%4==0:
    print("It is a leap year")
else:
    print("It is not a leap year")

#-ve/+ve
num = int(input("Positive Negative Test(Enter a number) : "))
if num<0:
    print("The Entered number is negative")
else:
    print("The Entered number is positive")

#divisible by 5 and 10
num = int(input("Divisibility test(Enter a number) : "))
if num%5==0 and num%10==0:
    print("The number is divisible by 5 and 10")
else:
    print("The number is not divisible by 5 and 10")

#enter character and check entered character is alphabet or not
select=input("Alphabet Test(Enter a value : )")
if (select>='a' and select<='z') or (select>='A' and select<='Z'):
    print("You have entered an alphabet")
else:
    print("Please enter an Alphabet")

#enter character and check character is vowel or not
vowel=input("Vowel test(Enter an alphabet) : ")
if vowel=='a' or vowel=='e' or vowel=='i' or vowel=='o' or vowel=='u':
    print("The character is a vowel")
else:
    print("The character is not a vowel")


        

'''
Data types
------------------  
    are used to define which type of data.

    int
    string
    float

Variable
-----------------
    is used to store data.

    Rules
    --------------
        always start with letter or underscore.
        never starts with number.
        never uses of special characters except underscore.
        keywords are not allowed.
        white spaces are not allowed instead of we can use underscore.

        valid variable name
        ---------------------
        first
        _first
        first_var
        first7

        invalid variable name
        ----------------------
          6first
          %first
          first var
          for


        syntax
        --------------
        variablename=value

        ex:
        ---
        age=90

        display the value of variable
        -----------------------------
            print(variablename)
            or
            print("message",variablename)



example
-----------------------
print("welcome")
print("hello",end=' ')
print("hii")

name="abc"
age=89
per=45.44

print(name)
print(age)
print(per)

print('Name is: ',name)
print('Age is : ',age)
print('Per marks is : ',per)
-------------------------------------------------

Input from user/read data from user
----------------------------------
    string
    ---------
        input() method is used.
        raw_input() method is used.

        syntax
        ---------
            variablename=input('message')
            or
            variablename=input()

        
    integer
    ---------------
        int() method is used to convert data string into int.

        syntax
        -----------
        variablename=int(input("message"))

    float
    -------------
        float() method

        syntax
        --------
        variablename=float(input("message"))
        
example
------------------
name=input("Enter Name: ")
a=int(input("Enter a: "))
b=int(input("Enter b: "))
per=float(input("Enter Percentage marks : "))

c=a+b

print("Name is :",name)
print("Sum is :",c)
print("Percentage marks is :",per)
--------------------------------------------------------
#swapping of two numbers using third variable
#swapping of two numbers without using third variable
#area of circle
#area of rectangle
#area of square
#simple interest
#sum of five digit number
#reverse of five digit number

*   +   -   /   //floor division    ** square root      %


'''
#swapping of two numbers using third variable
num1=int(input("Enter number1 : "))
num2=int(input("Enter number2 with which you want to swap number1 : "))                                                                                                                                                                                                                                                                                                                                                                                                                                               
print("-----Before swapping----")
print("num1 : ", num1, end=' ')
print("and num2 : ", num2)


print("-----Result of swapping(with variable)----")
temp = num1
num1 = num2
num2 = temp

print("num1 : ", num1, end=' ')
print("and num2 : ", num2)

#swapping of two numbers without using third variable

print("------Result of swapping(without variable)-----")
num2 = num1 + num2 #5+2=7
num1 = num2 - num1 #7-5=2
num2 = num2 - num1 #7-2=5

print("num1 : ", num1, end=' ')
print("and num2 : ", num2)

#Area of circle
circle=float(input("Enter radius of circle: "))
print("Area of circle is : ", 22*circle*circle/7)

#Area of rectangle
length=float(input("Enter length: "))
breadth=float(input("Enter breadth: "))
print("The Area of rectangle is : ", length*breadth)

#Sum of a 5digit number
fivedigit=int(input("Enter a 5 digit number : "))
#print(len(str(fivedigit)))

rem1 = fivedigit%10 #12345%10=5
fivedigit = fivedigit//10#12345//10=1234

rem2 = fivedigit%10
fivedigit = fivedigit//10

rem3 = fivedigit%10
fivedigit = (fivedigit)//10

rem4 = fivedigit%10
fivedigit = (fivedigit)//10

rem5 = fivedigit
net = rem1 + rem2 + rem3 + rem4 + rem5
print("The sum of all the numbers entered is : ", net)

#reverse of a five digit number
#reverse = str(int(rem1)) + str(int(rem2)) + str(int(rem3)) + str(int(rem4)) + str(int(rem5))
#print("The reverse of the number is : ", reverse)

rev=rem1*10000+rem2*1000+rem3*100+rem4*10+rem5
print("The reverse of the number is : ", rev)


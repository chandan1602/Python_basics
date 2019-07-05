'''
Operators
--------------------
    arithmetic operators
    -------------------------
    +    -    *     /       //      %   **

    10/3=3.33
    10//3=3
    10%3=1

    Relational/comparison operators
    -------------------------
        used to compare the values.
        return True or False as a result.

        >    <   >=   <=    ==   !=    <> not equals to


    Logical operators
    -----------------------
        used to apply a logic on two or more than two conditions.
        return True or False.

        and     or  not
        --------------------------------
        and : all conditions are True then result is true otherwise False.
        or: if either one condition is true then result is true otehrwise false.
        not: opposite result

example
-------------------
a=int(input("Enter First NUmber: "))
b=int(input("Enter Sec NUmber: "))
c=int(input("Enter Third NUmber: "))


d=a>b
#print(d)
print(a,">",b,"=",d)

d=a>b and b>c
print(a,">",b," and ",b,">",c,"=",d)

d=a>b or b>c
print(a,">",b," or ",b,">",c,"=",d)

d=not(a>b and b>c)
print("not(",a,">",b," and ",b,">",c,")=",d)

------------------------------------------------------

'''

'''
Inheritance
--------------------
    is used to inherit the properties of base class to derived class.
    or creating new class from old class.
    re-usability of code.
    base/parent/super class.
    derived/child/sub class.
    
    syntax
    -------------
    class Baseclass:
        #statement
    class DerivedClass(BaseClass):
        #statement

    Types of inheritance
    ------------------------
        1)Single inheritance
        2)Multiple inheritance
        3)Multilevel inheritance
        4)Hierarchical inheritance
        5)Hybrid inheritance

        1)Single inheritance
        ------------------------
            here is single base class and single derived class.

                A
                |
                B

            
            syntax
            -------------
            class Baseclass:
                #statement
            class DerivedClass(BaseClass):
                #statement

    
example
-------------
class A:
    def getA(self):
        self.a=56
class B(A):
    def display(self):
        print("a is ",self.a)

obj=B()
obj.getA()
obj.display()
--------------------------------------------------------------------------
#inherit constructor in derived  class
class A:
    def __init__(self,name,age):
        self.n=name
        self.a=age
    def getA(self):
        self.a=56
class B(A):
    def __init__(self,roll,name,age):
        self.r=roll
        A.__init__(self,name,age)
    def display(self):
        print("a is ",self.a)
        #self.n="aaa"
        print("Name is :",self.n)
        print("Age is :",self.a)
        print("Roll no is :",self.r)

obj=B(12,"ddd",34)
obj.getA()
obj.display()

#########################################################################
2)Multiple inheritance
--------------------------
    creating new child class from two or more than two base class.

        A       B
        p       r
            C
            t,si

        syntax
        ----------
        class BaseClass:
            #statement
        class BaseClass2:
            #statement
        class DerivedClass(Baseclass,BaseClass2):
            #statement

3)Multilevel inheritance
-------------------------------
    A
    |
    B
    |
    C

    level 1: A is base class for B
    level 2: B is base class for C

    
    syntax
    -------
    class BaseClas:
        #statement
    class DerivedClass(BaseClass):
        #statement
    class DerivedClass2(DerivedClass):
        #statement

4)Hierarchical inheritance
------------------------------
    is like a tree structure.

        A
    B       C

    syntax
    -----------
    class BaseClass:
        #statement
    class DerivedClass(BaseClass):
        #statement    
    class DerivedClass2(BaseClass):
        #statement

5)Hybrid inheritance
----------------------------

      A                 r
    B   C           rate   radius
      D              si      area
                        sum


    syntax
    -----------
    class BaseClass:
        #statement
    class DerivedClass(BaseClass):
        #statement    
    class DerivedClass2(BaseClass):
        #statement
    class DerivedClass3(DerivedClass,DerivedClass):
        #statement
        
'''
'''
#Example of Multiple Inheritance
class A:
    def __init__(self,rate):
        self.r=rate
class B:
    def __init__(self,principal):
        self.p=principal
class C(A, B):
    def __init__(self, time, rate, principal):
        self.t=time
        A.__init__(self,rate)
        B.__init__(self, principal)
    def interest(self):
        interest=self.r*self.p*self.t/100
        print("The Simple Interest is : ", interest)
i1=C(1, 10, 12000)
i1.interest()
'''

#Example of Hybrid Inheritance
class base:
    def __init__(self, rstart):
        self.r=rstart
        
class interest(base):
    def __init__(self, time, principal, rstart):
        self.t=time
        self.p=principal
        base.__init__(self,rstart)
    def interest(self):
        self.interest=self.t*self.p*self.r/100
        
class area(base):
    def __init__(self, pie, rstart):
        self.const=pie
        base.__init__(self, rstart)
    def area(self):
        self.area=self.const*self.r**2

class interest_area(interest, area):
    def __init__(self, time, principal, pie, rstart):
        interest.__init__(self, time, principal, rstart)
        area.__init__(self, pie, rstart)
    def net(self):
        self.net = self.area+self.interest
        print("Sum of interest and area is : ", self.net)

s1=interest_area(1, 10000, 10, 10)
s1.interest()
s1.area()
s1.net()

print(2*'bbb')

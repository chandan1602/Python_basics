'''
list
--------------
    is a collection of data.
    dynamic increase or decrease the size of list.

    syntax
    -------------
    list_var=[]

    Operations
    ------------------
        1)add item
            |
            insert()
            append()
        2)delete item
            |
            pop(): delete a specific item
            del : delete a item
        3)copy list
            |
            copy()
        4)clear the list
            |
            clear()
        5)delete whole list
            |
            del
        6)slicing
            |
            slice()


example
--------------------------
#list
list_var=[34,55,666]
print(list_var)

for x in list_var:
    print(x)

#add item
#insert(index,value)
list_var.insert(1,56)
print(list_var)
#append(value)
list_var.append(123)
print(list_var)


#delete item
#pop(index)
list_var.pop(1)
print(list_var)

#list_var.popitem()
#print(list_var)

#delete element
del list_var[1]
print(list_var)


#copy list
new_list=list_var.copy()
print(new_list)

#clear list : clear
list_var.clear()
print(list_var)



#delete list
del list_var
print(list_var)


#sorting
6 78 2 3  :  2 3 6 78(asc,desc)
#search  34 55 77 22    enter number to serach 34
#find minimum element and maximum element
=================================================================================================

tuple
--------------
    is a collection of data.
    can't change the elements

    syntax
    ------------
    tup_var=()

    operations
    ------------------
        |
        copy()
        slice()


example
----------------
tup_var=(34,656,787)
print(tup_var)
        
=========================================================================================
dictionary
-----------------
    is a collection of data in thr form key and value.

    syntax
    -----------
    dict_var={}

    operations
    -----------------
        |
        copy()
        delete
        popitem(): delete a last item
        del dict_var['key']
        clear()

        add items  
            
        
    syntax
    -------------
        dict_var={'key':'value'}

#example
--------------------------------------------
dict_var={'name':'abc','age':45}

print(dict_var)

print(dict_var['name'])

dict_var['per']=56.44
print(dict_var)

dict_var.popitem()
print(dict_var)

=========================================================================================================

'''

#Sorting
'''new_list = [12, 1222, 12222]
if new_list[0] > new_list[1]:
    if new_list[0] > new_list[2]:
        print("The Greatest : ",new_list[0])
        if new_list[1]>new_list[2]:
            print(new_list[1])
            print("The Lowest : ",new_list[2])
        else:
            print(new_list[2])
            print("The Lowest : ",new_list[1])
    else:
        print("The Greatest : ",new_list[2])
        print(new_list[0])
        print("The Lowest : ",new_list[1])

else:
    if new_list[1]>new_list[2]:
        print("The Greatest : ",new_list[1])
        if new_list[0]>new_list[2]:
            print(new_list[0])
            print("The Lowest : ",new_list[2])
        else:
            print(new_list[2])
            print("The Lowest : ",new_list[0])
    else:
        print("The Greatest : ",new_list[2])
        print(new_list[1])
        print("The Lowest : ",new_list[0])
        
#Searching
list2 = [12, 13, 21, 31]
num = int(input("Enter number to search : "))
for i in range(0, 4, 1):
    if list2[i] == num:
        print("The number is available on index : ", i)
        

'''

'''
list_var.sort()
print(list_var)

list_var.reverse()
print(list_var)
'''

'''
list_var=[]
n=int(input("Enter the number of elements "))
for i in range(0,n,1):
    ele=int(input())
    list_var.append(ele)
print(list_var)
list_var.append(-9999999999999999999999999999999999999999)

def opOnListItemFirst():
    list_var.append(list_var[i+1])
    del list_var[i+1]

def opOnListItemSecond():
    list_var.append(list_var[i])
    del list_var[i]
print("----------------The sorted loop will be---------------")
i=0
while i<n:
    for j in range(0, n-1, 1):
        if list_var[i] > list_var[i+1]:
            opOnListItemFirst()
        else:
            opOnListItemSecond()
    print(list_var[i])
    i+=1
'''        

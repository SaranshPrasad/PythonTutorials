# Lists 
myList = ["saransh", 20, True, 20.99]
print(type(myList[0]))
type(myList[0])
myList[2]

# Using list() -> List Constructor 
tup = (1,2,3,4,5)
tup_to_list = list(tup)
print(tup_to_list) # Converted tuple to list 

# Creating list with repeated elements 
a = [0] * 10 # -> creates a = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
print(a)

# Adding Elements into List
# append() ->  Adds an element at the end of the list.
myList.append("YSM")
# extends() -> Adds multiple elements to the end of the list.
myList.extend([1,2,3,4,5])
# insert() -> Adds an element at a specific position.
myList.insert(4,"A")

print(myList) # -> output of myList = ['saransh', 20, True, 20.99, 'A', 'YSM', 1, 2, 3, 4, 5]

# Updating Elements into List 
myList[2] = False

# Removing Elements from List
# remove(): Removes the first occurrence of an element.
myList.remove(20)
# pop(): Removes the element at a specific index or the last element if no index is specified.
myList.pop() #-> by default it pops out last index element if index not passed into it.
print(myList) # output -> ['saransh', False, 20.99, 'A', 'YSM', 1, 2, 3, 4]
# del statement: Deletes an element at a specified index.
# del myList # this line del complete myList because index it not specified. 

# Loop in List
for i in myList:
    print(i)

# Nested List 
matrix = [[1,2,3],[4,5,6],[7,8,9]]
print(matrix)
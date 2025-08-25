# creating a new empty list
my_list = []

# adding the following elements to my_list: 10, 20, 30, 40.
my_list.append(10)
my_list.append(20)
my_list.append(30)
my_list.append(40)

# inserting value 15 to second position
my_list.insert(1, 15)

# extending the list with values 50, 60, 70
my_list.extend([50, 60, 70])

# removing the last element
my_list.pop()

my_list.sort()

# finding the index of value 30
index_of_30 = my_list.index(30)
print(f"The index of value 30 is: {index_of_30}")
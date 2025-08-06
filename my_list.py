# 1. Empty list ,my list
my_list = []

# 2. Append elements to the list
my_list.append(10)  
my_list.append(20)
my_list.append(30)  
my_list.append(40)

# 3. insert the value at 15 at second position in the list
my_list.insert(1, 15)

# 5. remove the last element from the list.
my_list.pop()

# 6. sort the list in ascending order
my_list.sort()

# 7. find and print the index of the value 30 in the my_list
index_of_30 = my_list.index(30)
print(f"The index of 30 in my_list is: {index_of_30}")

print(f"Final my_list: {my_list}")

# TUPLE
def tuple_practice():
    # to create a tuple of numbers and print one item.
    classA = tuple(['A', 'B', 'C', 'D', 'D'])
    print("Student's name:", classA[2])

    # to unpack a tuple into several variables.
    (good, *normal, weak) = classA
    print("Good Students:", good)
    print("Normal Students:", normal)
    print("Weak Students:", weak)

    # to add an item to a tuple.
    classA_list = list(classA)
    new_student = input("Enter new student's name: ")
    classA_list.append(new_student)
    classA = tuple(classA_list)
    print("Updated Class members:", classA)

    # to find the index of an item in a tuple.
    find_mem = input('Enter member name you want to find: ')
    index = classA.index(find_mem)
    print("The student's id is", index)

    # to find the repeated items of a tuple
    x = []
    for _ in classA:
        if _ not in x:
            x.append(_)
        else:
            print(f"The student {_} is repeated!")
#================================================================
# SET
def set_practice():
    # Write a Python program to find the maximum and minimum values in a set.
    number_setA = {61, 23, 83, 14, 50, 62, 78, 8}
    print(max(number_setA))
    print(min(number_setA))

    # Write a Python program to check if a given value is present in a set or not.
    check_val = int(input("Enter the value you want to check: "))
    if check_val in number_setA:
        print(f"{check_val} in number set")
    else: print(f"No {check_val} in number set")

    # Write a Python program to check if two given sets have no elements in common.
    number_setB = {52, 24, 82, 34, 51, 72, 48, 28}
    number_setC = {21, 42, 13, 24, 50, 73, 38, 97}
    inter_set1 = number_setA.intersection(number_setB)
    inter_set2 = number_setA.intersection(number_setC)

    if len(inter_set1) == 0:
        print("No elements in common")
    else:
        print("Elements in common is", inter_set1)

    if len(inter_set2) == 0:
        print("No elements in common")
    else:
        print("Elements in common is", inter_set2)

    # Write a Python program to find all the unique words and count the frequency of occurrence from a given list of strings. Use Python set data type.
    occurrence = ["fox", "what"]
    occur_set = set(occurrence)
    string_lst = "what does the fox say".split()
    string_set = set(string_lst)

    uq_word_set = string_set - occur_set
    print(uq_word_set)

    # Given two sets of numbers, write a Python program to find the missing numbers in the second set as compared to the first and vice versa. Use the Python set.
    number_setD = {21, 44, 82, 34, 50, 62, 48, 28}
    number_setE = {21, 82, 13, 44, 50, 73, 48, 97}
    missing_setA = number_setD - number_setE
    print(f"Set D compare to set E missing: {missing_setA}")
    missing_setB = number_setE - number_setD
    print(f"Set E compare to set D missing: {missing_setB}")
#================================================================
# DICTIONARY
def dictionary_practice():
# Convert two lists into a dictionary
# Merge two Python dictionaries into one
# Print the value of key ‘history’ from the below dict
# Initialize dictionary with default values
# Create a dictionary by extracting the keys from a given dictionary
# Delete a list of keys from a dictionary
# Check if a value exists in a dictionary
# Rename key of a dictionary
# Get the key of a minimum value from the following dictionary
# Change value of a key in a nested dictionary
# Counts the number of times characters appear in a text paragraph.
# Using a dictionary containing keys starting from 1 and values ​​containing prime numbers less than a value N.
    pass

#================================================================
# Restructuring the company data: 
import copy

def restruct_comp_dat():
    employees = {
        1001: {"name": "Alice", "department": "Engineering", "salary": 75000},
        1002: {"name": "Bob", "department": "Sales", "salary": 50000},
        1003: {"name": "Charlie", "department": "Engineering", "salary": 80000},
        1004: {"name": "Dave", "department": "Marketing", "salary": 60000},
        1005: {"name": "Eve", "department": "Sales", "salary": 55000},
    }

    info_employees = copy.deepcopy(employees)
    for id, info in employees.items():
        del info_employees[id]["department"]

    dept_employees = dict()
    for id, info in employees.items():
        dept = info["department"]

        if dept != dept_employees.keys():
            dept_employees[dept] = {}
        
        dept_employees[dept][id] = info_employees[id]  

    print(dept_employees)
#================================================================
# MAIN
# tuple_practice()
# set_practice()
dictionary_practice()
# restruct_comp_dat()

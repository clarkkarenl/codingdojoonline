# Assignment: Find Characters
# Karen Clark
# 2018-06-02

# Assignment: Find Characters
# Write a program that takes a list of strings and a string containing a single character, and prints a new list of all the strings containing that character.

def find_characters(str_list, str_char):
    flag = False
    new_list = list()

    for elem in str_list:
        for i in elem:
            if i == str_char:
                flag = True
        if flag == True:
            new_list.append(elem)
            flag = False
    
    if len(new_list) > 0:
        print new_list
    else:
        print "No elements matched that character"

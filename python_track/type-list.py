# Assignment: Type List
# Karen Clark
# 2018-06-02

# Assignment: Type List
# Write a program that takes a list and prints a message for each element in the list, based on that element's data type.
# Your program input will always be a list. For each item in the list, test its data type. If the item is a string, concatenate it onto a new string. If it is a number, add it to a running sum. At the end of your program print the string, the number and an analysis of what the list contains. If it contains only one type, print that type, otherwise, print 'mixed'.

def type_list(x):
    list_item_string = ""
    list_item_sum = 0
    str_counter = 0
    int_counter = 0
    
    for element in x:
        if isinstance(element, str):
            list_item_string = list_item_string + " " + element
            str_counter += 1
        elif isinstance(element, int) or isinstance(element, float) or isinstance(element, long) or isinstance(element, complex):
            list_item_sum += element
            int_counter += 1
    
    if int_counter == 0 and str_counter > 0:
        print "The list you entered is of string type"
        print "String: " + list_item_string
    elif str_counter == 0 and int_counter > 0:
        print "The list you entered is of integer type"
        print "Sum: " + str(list_item_sum)
    elif str_counter > 0 and int_counter > 0:
        print "The list you entered is of mixed type"
        print "String: " + list_item_string
        print "Sum: " +  str(list_item_sum)
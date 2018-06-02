# Assignment: Compare Lists
# Karen Clark
# 2018-06-02

# Assignment: Compare Lists
# Write a program that compares two lists and prints a message depending on if the inputs are identical or not.

# Your program should be able to accept and compare two lists: list_one and list_two. If both lists are identical print "The lists are the same". If they are not identical print "The lists are not the same." 
def compare_lists(x, y):
    count = 0

    if len(x) != len(y):
        print "The lists are not the same"
        exit
    elif len(x) == len(y):
        for i, j in zip(x, y):
            if i != j:
                print "The lists are not the same"
                exit
            else:
                count += 1

        if count == len(x):
            print "The lists are the same"
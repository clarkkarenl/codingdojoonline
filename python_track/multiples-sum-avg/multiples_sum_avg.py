# Assignment:  Multiples, Sum, Average
# Karen Clark
# 2018-05-31

# 1. Multiples
# a. Part I - Write code that prints all the odd numbers from 1 to 1000. Use the for loop and don't use a list to do this exercise.
def print_odds():
    # all numbers from 1 to 1000
    for i in range(1, 1001):
        # not evenly divisible by 2 (or, "odd")
        if i % 2 != 0:
            print i


# b. Part II - Create another program that prints all the multiples of 5 from 5 to 1,000,000.
def print_multiples():
    # for values from 5 to 1,000,000
    for i in range(1, 200001):
    # print all multiples of 5
        print 5 * i, i


# 2. Sum List
# Create a program that prints the sum of all the values in the list: a = [1, 2, 5, 10, 255, 3]
def sum_list(x):
    # sum variable to hold the running tally
    sum = 0

    # for all values in the given list
    for i in x:
        # verify the item is a number
        try:
            temp = int(i)
        except ValueError:
            continue
        else: 
            # it's an int! sum it up
            sum += i

    print sum


# 3. Average List
# Create a program that prints the average of the values in the list: a = [1, 2, 5, 10, 255, 3]
def avg_list(x):
    # sum variable to hold the running tally    
    sum = 0

    # for all values in the given list
    for i in x:
        # verify the item is a number
        try:
            temp = int(i)
        except ValueError:
            continue
        else: 
            # it's an int! sum it up
            sum += i

    # find the avg by dividing sum by number of items
    print sum/len(x)
# Assignment:  Python String and List Practice
# Karen Clark
# 2018-05-31

# 1. Find and Replace
# In this string: words = "It's thanksgiving day. It's my birthday,too!" print the position of the first instance of the word "day". Then create a new string where the word "day" is replaced with the word "month".

words = "It's thanksgiving day. It's my birthday,too!"
first_day = words.find("day")
newstr = words.replace("day", "month", 1)
print newstr


# 2. Min and Max
# Print the min and max values in a list like this one: x = [2,54,-2,7,12,98]. Your code should work for any list.

### TO DO!
def min_and_max(x):
    max = x[0]
    min = x[0]

    for i in x:
        if i >= max:
            max = i
        elif i < min:
            min = i
    print "Max is " + str(max) + " and min is " + str(min)


# 3. First and Last
# Print the first and last values in a list like this one: x = ["hello",2,54,-2,7,12,98,"world"]. Now create a new list containing only the first and last values in the original list. Your code should work for any list.
def first_and_last(x):
    first = x[0]
    print first
    last = x[len(x) - 1]
    print last

    new_x = []
    new_x.append(first)
    new_x.append(last)
    

# 4. New List
# Start with a list like this one: x = [19,2,54,-2,7,12,98,32,10,-3,6]. Sort your list first. Then, split your list in half. Push the list created from the first half to position 0 of the list created from the second half. The output should be: [[-3, -2, 2, 6, 7], 10, 12, 19, 32, 54, 98]. Stick with it, this one is tough!
def new_list(x):
    # Sort the list
    for iter in range(len(x) - 1, 0, -1):
        for idx in range(iter):
            if x[idx] > x[idx + 1]:
                temp = x[idx]
                x[idx] = x[idx + 1]
                x[idx + 1] = temp

    # Split list in half and make a new list
    half = len(x)/2

    # populate new list with the second half of the list
    nl = x[half:]

    # Insert the first half list into list index 0
    nl.insert(0, x[:half])

    print nl

new_list([19,2,54,-2,7,12,98,32,10,-3,6])
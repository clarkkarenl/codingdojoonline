# Assignment: Filter by Type
# Karen Clark
# 2018-06-02

# Assignment: Filter by Type
# Write a program that, given some value, tests that value for its type. Here's what you should do for each type:
# Integer
# If the integer is greater than or equal to 100, print "That's a big number!" If the integer is less than 100, print "That's a small number"
# String
# If the string is greater than or equal to 50 characters print "Long sentence." If the string is shorter than 50 characters print "Short sentence."
# List
# If the length of the list is greater than or equal to 10 print "Big list!" If the list has fewer than 10 values print "Short list."

def filter_by_type(x):
    if isinstance(x, int):
        if x >= 100:
            print "That's a big number!"
        elif x < 100:
            print "That's a small number"
    elif isinstance(x, str):
        if len(x) >= 50:
            print "Long sentence"
        elif len(x) < 50:
            print "Short sentence"
    elif isinstance(x, list):
        if len(x) >= 10:
            print "Big list!"
        elif len(x) < 10:
            print "Short list"
    else:
        print "Type cannot be determined. Please try again."

# example vars to test
sI = 45
mI = 100
bI = 455
eI = 0
spI = -23
sS = "Rubber baby buggy bumpers"
mS = "Experience is simply the name we give our mistakes"
bS = "Tell me and I forget. Teach me and I remember. Involve me and I learn."
eS = ""
aL = [1,7,4,21]
mL = [3,5,7,34,3,2,113,65,8,89]
lL = [4,34,22,68,9,13,3,5,7,9,2,12,45,923]
eL = []
spL = ['name','address','phone number','social security number']

# invocations
filter_by_type(sI)
filter_by_type(mI)
filter_by_type(bI)
filter_by_type(eI)
filter_by_type(spI)
filter_by_type(sS)
filter_by_type(mS)
filter_by_type(bS)
filter_by_type(eS)
filter_by_type(aL)
filter_by_type(mL)
filter_by_type(lL)
filter_by_type(eL)
filter_by_type(spL)

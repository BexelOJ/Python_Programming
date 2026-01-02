############################################
# for loop
for i in range(10): # default starts from 0, ends at 9
    print(i, end=' ') # end='\n\n' prints a new line
print()  # print a new line

# for loop
for j in range(0,10):  # starts from 0 (inclusive zero), ends at 9 (exclusive 10)
    print(j, end=' ')
print()  # print a new line
    
# for loop    
for k in range(0,10,2): # starts from 0, ends at 9, step by 2
    print(k, end=' ')
print()  # print a new line

############################################    
set = {1, 2, 3, 4, 5} # set
for i in set:
    print(i, end=' ')
print()  # print a new line

# for loop
l = [1, 2, 3, 4, 5] # list
for x in l:
    print(x, end=' ')
print()  # print a new line

t = (1, 2, 3, 4, 5) # tuple
for y in t:
    print(y, end=' ')
print()  # print a new line

d = {1: 'one', 2: 'two', 3: 'three'} # dictionary
#for key in d:
#    print(d[key], end=' ')
print()  # print a new line
print(d.values(), end = "\n\n")
print(d.items(), end='\n\n')
############################################
    
    
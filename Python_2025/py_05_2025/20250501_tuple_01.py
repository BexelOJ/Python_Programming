t = () # empty tuple
t1 = tuple() # empty tuple

t1 = (1,2,2,3,3,4,5,5)
s = len(t1)
print(f"Size of Tuple t1 is {s}")


# tuple is not mutable, once created
# tuple is indexable
# count the number of times, an element is repreated

print(t1.count(2)) # 2 ## number of 2
print(t1.index(3)) # 3 ## index of first occurance of 3



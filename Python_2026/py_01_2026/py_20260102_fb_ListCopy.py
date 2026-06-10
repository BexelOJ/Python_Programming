import copy

x = [1,2,3]
print(f" x = {x}")

a = x # creates 'a' as refernce of 'x'

b = copy.copy(x) # independent memory
c = x[:] # creates shallow copy of list x

print(f" a = {a}")
print(f" b = {b}")
print(f" c = {c}")

y = x
y[1] = 4 # update value at index 1 as 4

print()
print(f' x = {x}')
print(f" a = {a}")
print(f' b = {b}')
print(f" c = {c}")




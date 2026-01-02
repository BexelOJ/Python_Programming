# Different Set Methods:
a = {1, 2, 3}
b = {1, 2, 3, 4, 5}

# Method way
print(a.union(b))            # {1, 2, 3, 4, 5}
c = a.union(b)
print(c)                     # {1, 2, 3, 4, 5}

print(a.intersection(b))     # {1, 2, 3}
print(a ^ b)                 # {4, 5}

# Operator way
print(a | b)                 # {1, 2, 3, 4, 5}
print(a & b)                 # {3}





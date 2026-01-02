s1 = set() # empty set
  
s1.add(10)
s1.add(20)
s1.add(30)

s2 = {10, 20, 30, 40, 50} # set

print(f"Length of Set 1: {len(s1)}")
print(f"Length of set 2: {len(s2)}")

print(s1)
print(s2)

s1.remove(20)

print(s1 == s2)
s1 = s2
print(s1 == s2)
print(s1)
print(s2)
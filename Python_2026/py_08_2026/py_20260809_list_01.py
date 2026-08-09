#!/usr/bin/python3

l1 = [ "Drake", "Derp", "Derek", "Dominique" ]


l2=["a","b","c"] 

print(f"{l1} is a python list")
print(l1[0])
print(l1[1])
print(l1[2])

print(l2[0]+" bc")
print(l2[1]+" cd")
print(l2[2]+" de")
#!/usr/bin/python3

l1.append("Victoria")  # add element.
print(l1)              # print all elements
# ['Drake', 'Derp', 'Derek', 'Dominique', 'Victoria']

l1.remove("Derp")      # 
l1.remove("Drake")     # 
print(l1)              # ['Derek', 'Dominique', 'Victoria']

l1.remove(l1[0])       # 
print(l1)
# ['Dominique', 'Victoria']

l1.append("Drake")
l1.append("Derp")
l1.append("Derek")
print(l1)
# ['Dominique', 'Victoria', 'Drake', 'Derp', 'Derek']

l1.sort()
print(l1)
# ['Derek', 'Derp', 'Dominique', 'Drake', 'Victoria']

l1.reverse() # reverse order
print(l1)

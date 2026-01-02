n = int(input("Enter the size of List: "))

l1 = [] # empty list
l2 = list() # empty list

'''
for i in range(n):
    val = int(input())
    l1.append(val)
    
'''
for _ in range(n):
    l1.append(int(input("Enter element: ")))
    
#'''

size = len(l1) # size of list
print(f"List Size : {len(l1)}")
print(f"Original List: {l1}")

l1.insert(0, 100) # insert 100 at index 0
l1.insert(1, 200) # insert 200 at index 1
l1.insert(2, 300) # insert 300 at index 2

print(f"Updated  List: {l1}")

'''
for i in l1: # iterate through list     
    print(i, end=' ')
print()
    
''' 

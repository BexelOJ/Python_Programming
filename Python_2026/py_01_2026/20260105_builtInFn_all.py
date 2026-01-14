'''Python's all() built-in function returns True if every element in an iterable is truthy, and False otherwise.
Empty iterables always return True. 
It short-circuits like and, stopping at the first falsy value.'''

l_1 = [1,2,3]

t_1 =(1,2,3)
t_2 = (1,2,0,4)

s_1 = {1,2,3,4,5}
s_2 = {}
s_3 = {1,0,2,3,4}

dic_1 = {1:'a', 2:'b'}
dic_2 = {1:'a', 2:'b', 3:'0'}
#dic_3 = 

print(f" l_1 = {all(l_1)}\n")            # True
print(all([1,2,3]))        # True
print(f" t_1 = {all(t_1)}")
print(f" t_2 = {all(t_2)}\n")

print(f" s_1 = {all(s_1)}")
print(f" s_2 = {all(s_2)}")
print(f" s_3 = {all(s_3)}\n")

print(f" dic_1 = {all(dic_1)}")
print(f" dic_2 = {all(dic_2)}\n")

print(all([1, 0, 3]))      # False
print(all([]))             # True (empty)
print(all(""))             # True (empty string)
print(all("abc"))          # True (non-empty string)
print(all({1: 'a', 2: 'b'}))  # True (keys truthy)

print(dic_2.keys())
print(dic_2.values())

print(l_1[0])
print(t_1[0])
print(t_2[-5])




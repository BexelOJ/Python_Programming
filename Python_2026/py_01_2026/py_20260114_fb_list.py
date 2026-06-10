t = (1,2,3)
print(t)
for i in t:
    i = i * 2
    print(i)
print(t)


t_list = list(t)  # [1, 2, 3]
for i in range(len(t_list)):
    t_list[i] = t_list[i] * 2
t = tuple(t_list)  # Back to (2, 4, 6)
print(t)

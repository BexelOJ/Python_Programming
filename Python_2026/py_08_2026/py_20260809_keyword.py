#!/usr/bin/python3

import keyword

print(keyword.iskeyword("pass"))

print(keyword.kwlist)
print(f"\nNumber of Python Keywords : {len(keyword.kwlist)}")
print()
i=1
for kw in keyword.kwlist:
    print(f"{i} : {kw}")
    i += 1
print()
j=1
for kw in keyword.softkwlist:
    print(f"{j} : {kw}")
    j += 1
print()




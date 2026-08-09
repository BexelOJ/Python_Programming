#!/usr/bin/python3

z = 10
def afunction():
    global z
    print(z)
    z=20
    print(f"z = {z}")
    global e
    
    #print(e)
print(f"gz = {z}")
#print(e)
afunction()
e=55
print(f"af gz = {z}")
print(f"af le = {e}")

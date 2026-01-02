a = 10
b = 3.14
c = 'Hello'

d = 15
e = 3.123456789
f = "World"

def printType():
    print(type(a))
    print(type(b))
    print(type(c))
    print()
    print(type(d))
    print(type(e))
    print(type(f))

def merge():
    print(a + d)
    print(b + e)
    #print(f"{c} {f}, now the date is {a}")
    print(f"{c} and {f}")

def main():
    printType()
    merge()

main()




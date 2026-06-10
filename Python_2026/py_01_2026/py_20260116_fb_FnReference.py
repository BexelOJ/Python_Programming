def calc(x, y):
    x = x + 2
    y = y * 2

    print(f"Inside: id(x)={id(x)}, id(y)={id(y)}")  # Local IDs
    return x + y

a = 3
b = 4
print(f"Outside before: id(a)={id(a)}, id(b)={id(b)}")  # Different outer IDs
result = calc(a, b)
print(a, b, result)
print(f"Outside after: id(a)={id(a)}, id(b)={id(b)}")   # Unchanged

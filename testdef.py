def test(a, b, c):
    a += 1
    b = 22
    c += 3
    print()
    print(a, b, c)
    return x , y , z
x = 3
y = 7
z = 11
print(x, y, z)
print(test(x, y, z))
print(test(z, y, x))